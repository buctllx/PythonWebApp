#!/usr/bin/env python
#coding:utf-8

import orm
import asyncio
from models import User, Blog, Comment

async  def test():
    await orm.create_pool(loop= loop, user='root', password='password', db='awesome')

    u = User(name='llx', email='llxtest@example.com', passwd='1234567890', image='about:blank')

    await u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test())
loop.close()
data = User.findAll()
for d in data:
    print(d)
