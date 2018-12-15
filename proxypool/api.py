from flask import Flask, g
from .db import RedisClient
import json

__all__ = ['app']

app = Flask(__name__)


def get_conn():
    if not hasattr(g, 'redis'):
        g.redis = RedisClient()
    return g.redis


@app.route('/')
def index():
    return '<h2>Welcome to Proxy Pool System</h2>'


@app.route('/random')
def get_proxy():
    """
    Get a proxy
    :return: 随机代理
    """
    conn = get_conn()
    return conn.random()


@app.route('/count')
def get_counts():
    """redis==2.10.5
    Get the count of proxies
    :return: 代理池总量
    """
    conn = get_conn()
    return str(conn.count())


@app.route('/get_all/')
def get_all():
    conn = get_conn()
    all_proxy = json.dumps(conn.all())
    return all_proxy


if __name__ == '__main__':
    app.run()
