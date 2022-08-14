"""
不同于缓冲区的概率，传统架构中缓存的目的主要是为了加速请求，减少平均响应时间
另一方面也起到了减轻数据库的压力的目的
如最常用的mysql , 内置的缓存查询模块，在大部分业务的情况下，命中率太低，所以在 8.0 版本去掉了
在业务侧手动实现缓存组件，是常见也最好的优化手段

常见的缓存可以简单的分为对静态数据和动态数据的缓存，搭配不同的业务场景，是需要开发人员自行确定和实现

本案例从本地 和 分布式的情况考虑，基于不同的架构模式 和 常见的缓存场景，提供一些通用的方案

本地缓存(只是为了应对性能危机):
通常使用内存作为本地缓存的常用结构，相比于磁盘一次寻址只需要100ns
适用于极端高并发下热点数据的查询请求，以减轻 分布式缓存节点 和 数据库的压力
由于是内存结构且与业务在同一个线程，所以速度是极快的
1, 提供 lru+ttl 通过限制hashmap的最大长度以及lru算法，让热点数据尽可能的保持缓存 但又可以提高内存的利用率
2, guava cache 模式，提前写入缓存，应对即将而来的高并发请求，
例如某一数据查询需要复杂的运算，且有更新的可能，但是又允许一定时间数据延迟，
可以先使用guava cache缓存这部分数据，并且设定一个刷新时间，定期更新缓存内容

分布式缓存(更偏向于分布式，和缓存数据)
最常用的是Redis作为缓存节点
完全可以作为一个热点数据库，用来集中缓存热点数据，所有web节点都读同一份数据，便于统一管理缓存和保证数据一致性
在分布式的整体架构中，也提供如 分布式锁，又或者作为缓冲区，完成类似高并发计数的工作

至于缓存和数据库的读写策略，保持数据一致性的问题，就需要开发者个人按照情况来设计

通过下面的例子，可以明显的看出 同步与协程，以及协程配合缓存使用的速度
    
"""


import asyncio
import random
import time
from simple_starlette.args import QueryParams
from simple_starlette import (
    SimpleStarlette,
    Request,
    Response,
    ResTypeEnum,
)
from simple_starlette.cache.memory_cache import (
    LruCache,
    lru_cache_decorator,
    lru_cache_decorator_async,
)

from simple_starlette.cache.memory_cache import local_g
from simple_starlette.cache.guava_cache import GuavaCache


app = SimpleStarlette(__name__)

# wrk 工具进行单机并发测试
#  2 threads and 1000 connections 10s
#  ./wrk -s ../simple-starlette/example/local_cache/wrk_local_cache_urls.lua http://127.0.0.1:9091 -c 1000 -d 10
# 本地机器测试，不同机器环境配置不一致，数据集不一样，结果会有误差，但是结论不变：热点数据多 -> 命中率越大 -> 缓存组件的作用就越大


@lru_cache_decorator(maxsize=100, cache_ttl=10 * 60)
def gen_resp(user_id: int):
    # 不使用协程的情况下
    # Requests/sec:  1301.42
    # 当然如果sql指明使用缓存，是不会有这么大的延迟，这里模拟没有数据库缓存的情况（查询树磁盘网络io延迟)
    time.sleep(random.random())
    return {
        "user_id": user_id,
        "avatar": f"http://img.cdn/{random.randint(1,1000)}",
    }


async def gen_resp_async_no_cache(user_id: int):
    # async
    # Requests/sec:   1918.01
    # 当然如果sql指明使用缓存，是不会有这么大的延迟，这里模拟没有数据库缓存的情况 （查询树磁盘网络io延迟)
    await asyncio.sleep(random.random())
    return {
        "user_id": user_id,
        "avatar": f"http://img.cdn/{random.randint(1,1000)}",
    }


@lru_cache_decorator_async(maxsize=100, cache_ttl=10 * 60)
async def gen_resp_async(user_id: int):
    # async cache
    # Requests/sec:   4066.06
    # 可见如果瞬时涌入大量热点数据查询，可以应付较大的qps
    # 但是如果

    # 当然如果sql指明使用缓存，是不会有这么大的延迟，这里模拟没有数据库缓存的情况 （查询树磁盘网络io延迟)
    await asyncio.sleep(random.random())
    return {
        "user_id": user_id,
        "avatar": f"http://img.cdn/{random.randint(1,1000)}",
    }


def refresh_hot_user_info():
    _d = {}
    for i in range(1,11):
        _d[i] = {
            "user_id": i,
            "avatar": f"http://img.cdn/{random.randint(1,1000)}",
        }
    print(f"完成更新: {_d}")
    local_g["user_info"] = _d


gc = GuavaCache(interval=5, refresh_callable=refresh_hot_user_info)
gc.start() # 注释取消使用guava


@app.route("/user/info")
class UserInfo:
    class UserInfoQuery(QueryParams):
        user_id: int

    async def get(self, request: Request, q: UserInfoQuery):
        """
        示例查询 用户主页信息
        """
        if user_info_dict := local_g.get("user_info"):
            if user_info := user_info_dict.get(q.user_id):
                return Response(
                    content=user_info_dict, res_type=ResTypeEnum.JSON
                )

        # user_info_dict = gen_resp(q.user_id)
        # user_info_dict = await gen_resp_async(q.user_id)
        user_info_dict = await gen_resp_async_no_cache(q.user_id)
        return Response(
            content=user_info_dict, res_type=ResTypeEnum.JSON
        )


if __name__ == "__main__":
    app.run()
