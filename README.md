

## 添加Dockerfile

```bash
#使用方法
#创建image
docker build -t proxy .
#运行, 6666为本地监听端口
docker run -it -p 6666:5555 proxy
```

## 修改了requirements

新版本python的redis库运行存在问题，将requirements.txt中redis版本降低了。

## 添加了一个获取全部代理的api

`/get_all/`

感谢原作者的优秀项目，以下为原README

***

# ProxyPool

## 安装

### 安装Python

至少Python3.5以上

### 安装Redis

安装好之后将Redis服务开启

### 配置代理池

```
cd proxypool
```

进入proxypool目录，修改settings.py文件

PASSWORD为Redis密码，如果为空，则设置为None

#### 安装依赖

```
pip3 install -r requirements.txt
```

#### 打开代理池和API

```
python3 run.py
```

## 获取代理


利用requests获取方法如下

```python
import requests

PROXY_POOL_URL = 'http://localhost:5555/random'

def get_proxy():
    try:
        response = requests.get(PROXY_POOL_URL)
        if response.status_code == 200:
            return response.text
    except ConnectionError:
        return None
```
