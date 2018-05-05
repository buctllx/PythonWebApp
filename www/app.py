#!/usr/bin/env python
#coding:utf-8
"""
  Author:  luo linxin --<>
  Purpose: just for test
  Created: 2018/5/5
"""

# import logging; logging.basicConfig(level = logging.INFO)
import logging; logging.basicConfig(level = logging.INFO)
import asyncio, os, json, time
from datetime import datetime
from aiohttp import web

from datetime import datetime

#----------------------------------------------------------------------
def index(request):
    """"""
    return web.Response(body = u'<h1>Hello World！</h1>', content_type='text/html',charset='utf-8')

@asyncio.coroutine
def init(loop):
    """"""
    app = web.Application(loop = loop)
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server stared at http:127.0.0.1:9000...')
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()