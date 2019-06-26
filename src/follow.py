#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-06-26 20:14:07
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import logging
import os

import json

from zhihu import Zhihu
from zhihu import Answer
from zhihu import Account
from zhihu import Collection
from zhihu.url import URL
from constants import USER_LIST, DATA_PATH

"""
先登陆，存cookies
"""
# 我的已经登录好了
# account = Account()
# account.login("youremail", "yourpassword")

zhihu = Zhihu()

'''
to_follow = "onlymyflower"
data = zhihu.follow(user_slug=to_follow)
print(data)  # {'follower_count': 1, 'followed': True}
'''


def main():
    c = Collection(collection_id=243540505)
    r = c._execute(
        method="get", url="https://api.zhihu.com/collections/32755791")
    data = r
    print(data)


if __name__ == "__main__":
    main()
