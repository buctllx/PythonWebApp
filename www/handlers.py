#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Author:  luo linxin --<>
  Purpose: url handlers
  Created: 2018/5/6
"""


import re, time, json, logging, hashlib, base64, asyncio

from coroweb import get, post

from models import User, Comment, Blog, next_id

@get('/')
async def index(request):
    users = await User.findAll()
    return {
        '__template__': 'test.html',
        'users': users
    }