"""
缓存主要用来解决高并发问题
由于mysql8.0之后去掉了缓存查询模块，即便是之前的版本，对于动态数据库在数据库的server层做 缓存，命中率都比较低，而且会提高部分成本
所以大部分情况下是 在 业务的使用缓存组件，变相绕过一部分数据库瓶颈 

如果你的业务读多写少，且数据具有热点属性，使用缓存的优势更大

1, 静态缓存（如果你拥有一张 静态表 - 很少写入，且有查询需求）
    这种情况可以直接使用 数据库自带的缓存模块
    也可以提前加载到本地内存中，按照规则定时刷新

2, 动态缓存
    - 本地缓存 (
            性能强大: 用于应对短暂时间大量请求涌入，没有网络延迟 网络io，速度和性能更快
            寿命短:  对于动态数据缓存而言 ,这类缓存不应该有过长的寿命，以免造成数据不一致的情况
            长度控制: 应该适当控制缓存长度，以免服务出现OOM 导致重启 造成服务不可用
            服务重启: 服务重启或者容器重新部署，内存会消失，最好避免在热点时间此类操作
        )
        简单来说，如果你有一个随时可能会爆发大量请求的接口
        那么就应该在这样的接口加上本地缓存，当然也要分析热点数据的占比
        本案例中提供了 OrderDict + lru + ttl + maxsize 的方式 , 基于lru淘汰算法，ttl过期机制，maxsize控制最大的长度
        使用者唯一需要考虑的是，业务中哪些地方需要

    - 分布式缓存 (
        所有容器服务可共用一份缓存数据，
        相比本地缓存，可以保证重启服务后缓存还在，且能保持大量的数据
        且所有容器都读同一套缓存，一定意义上保证了数据一致性
        实现分布式锁 , 动态读取配置信息等额外的功能
    )
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
    lru_cache_decorator,
    lru_cache_decorator_async,
)


app = SimpleStarlette(__name__)

# wrk 工具进行单机并发测试
#  2 threads and 1000 connections 10s
#  ./wrk -s ../simple-starlette/example/local_cache/wrk_local_cache_urls.lua http://127.0.0.1:9091 -c 1000 -d 10
# 本地机器测试，不同机器环境配置不一致，结果会有误差，但是结论不变


@lru_cache_decorator(maxsize=100, cache_ttl=10 * 60)
def gen_resp(user_id: int):
    # 同步模式下 cache
    # Requests/sec:  1801.42
    # 当然如果sql指明使用缓存，是不会有这么大的延迟，这里模拟没有数据库缓存的情况（查询树磁盘网络io延迟)
    time.sleep(random.random())
    return {"user_id": user_id}


async def gen_resp_async_no_cache(user_id: int):
    # async
    # Requests/sec:   1918.01
    # 当然如果sql指明使用缓存，是不会有这么大的延迟，这里模拟没有数据库缓存的情况 （查询树磁盘网络io延迟)
    await asyncio.sleep(random.random())
    return {"user_id": user_id}


@lru_cache_decorator_async(maxsize=100, cache_ttl=10 * 60)
async def gen_resp_async(user_id: int):
    # async cache
    # Requests/sec:   4066.06
    # 可见如果瞬时涌入大量热点数据查询，可以应付较大的qps，减轻对数据库压力，即使数据库层有缓存，也会占用大量连接

    # 当然如果sql指明使用缓存，是不会有这么大的延迟，这里模拟没有数据库缓存的情况 （查询树磁盘网络io延迟)
    await asyncio.sleep(random.random())
    return {"user_id": user_id}


@app.route("/user/info")
class UserInfo:
    class UserInfoQuery(QueryParams):
        user_id: int

    async def get(self, request: Request, q: UserInfoQuery):
        """
        示例查询 用户主页信息
        """
        # user_info_dict = gen_resp(q.user_id)
        user_info_dict = await gen_resp_async(q.user_id)
        # user_info_dict = await gen_resp_async_no_cache(q.user_id)
        return Response(
            content=user_info_dict, res_type=ResTypeEnum.JSON
        )


if __name__ == "__main__":
    app.run()
