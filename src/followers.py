#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-06-26 02:25:59
# @Author  : Kelly Hwong (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
from zhihu import Zhihu, Account
from bs4 import BeautifulSoup


def check(target_url):
    account = Account()
    # account.login("hahaha@hahaha.com", "hahaha)
    zhihu = Zhihu()
    print(zhihu.cookies)

    r = zhihu.get(url=target_url)
    with open("debug.html", "w", encoding="utf-8") as f:
        f.write(r.text)
    soup = BeautifulSoup(r.text, "lxml")
    num = soup.find_all("strong", {"class": "NumberBoard-itemValue"})
    print(num)
    return num[1].text


def main():
    """
    api返回的粉丝数并不是实时的值，这是为什么？
    由于前端看到的粉丝数才是实时的，因此从前端爬取粉丝数

    Zhihu <- Model <- requests.Session
    所以直接调用session的get方法
    """
    target_url = "https://www.zhihu.com/people/huangkan/activities"
    if os.path.exists("./local.py"):
        from local import TARGET_URL
        target_url = TARGET_URL
    print(target_url)
    check(target_url)


if __name__ == "__main__":
    main()
