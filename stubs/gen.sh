
#!/bin/bash

set -e 

G='\033[0;32m' # green color
Y='\033[1;33m' # yellow color
N='\033[0m' # No Color

echo -e "${G}安装依赖...${N}"

pip3.8 install mypy==0.901
#pip3 install -r need_stub.txt -i https://mirrors.aliyun.com/pypi/simple/

echo -e "${Y}生成存根文件${N}"

for line in `cat need_stub.txt`
do
    echo -e "${G}正在生成模块${line}${N}"
    stubgen -p $line -o . && continue
done
