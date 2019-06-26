#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-17 22:16:35
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import logging
import os

import json

from zhihu import Zhihu
from zhihu import Answer
from zhihu import Account
from zhihu.url import URL
from constants import USER_LIST, DATA_PATH

"""
先登陆，存cookies
"""
# 我的已经登录好了
# account = Account()
# account.login("youremail", "yourpassword")

zhihu = Zhihu()
# print(zhihu.cookies)

# 获取用户基本信息
'''
profile = zhihu.profile(user_slug="huangkan")
print(profile)
with open("./profile.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(profile, ensure_ascii=False))
'''

# 粉丝数量
'''
for i in range(10):
    follower_list = zhihu.followers(user_slug="huangkan", limit=100, offset=0)
    with open("./followers_{0}.json".format(i), "w", encoding="utf-8") as f:
        f.write(json.dumps(follower_list, ensure_ascii=False))
    print(follower_list)
'''


def main():
    user_slug = "tian-ji-shun"
    i = 0
    will_break = False
    user_slug_path = os.path.join(DATA_PATH, "followers", user_slug)
    os.makedirs(user_slug_path, exist_ok=True)
    while True:
        json_file = os.path.join(
            user_slug_path, "followers_{}.json".format(i))
        if os.path.isfile(json_file):
            print("skip %d" % i)
            i += 1
            continue
        follower_list = zhihu.followers(
            user_slug=user_slug, limit=20, offset=str(20*i))
        if follower_list["paging"]["is_end"]:
            will_break = True
        with open(json_file, "w", encoding="utf-8") as f:
            f.write(json.dumps(follower_list, ensure_ascii=False))
        print("下一个爬取链接")
        print(follower_list["paging"]["next"])
        i += 1
        if will_break:
            break


if __name__ == "__main__":
    main()
