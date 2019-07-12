#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-06-27 01:50:08
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import json
import threading
import threadpool
from constants import USER_LIST, DATA_PATH, USER


class VarContainer(object):
    """
    常数的封装，用于可变对象的引用
    """

    def __init__(self, var=None):
        self.var = var


class Count(object):
    def __init__(self, follower_count=0, male_count=0, female_count=0, unknown_gender_count=0):
        self.follower_count = follower_count
        self.male_count = male_count
        self.female_count = female_count
        self.unknown_gender_count = unknown_gender_count


class Counter(threading.Thread):
    """
    下载URL内容的线程
    """

    def __init__(self, file=None, d=None):
        """
        构造器

        @param urls 需要下载的URL列表
        @param output 写URL内容的输出文件
        """
        threading.Thread.__init__(self)
        self.file = file
        # self.d = d

    def run(self, file, count):
        """
        根据json文件
        统计粉丝数信息
        """
        # 确保是读！蛤！
        with open(file, "r", encoding="utf-8") as f:
            d = json.loads(f.read())
            data = d["data"]
            for _ in data:
                count["follower_count"] += 1
                name, gender = _["name"], _["gender"]
                if gender == 0:
                    count["female_count"] += 1
                elif gender == 1:
                    count["male_count"] += 1
                elif gender == -1:
                    count["unknown_gender_count"] += 1
                print(count)


def main():
    # user_slug = USER["知乎小管家"]
    user_slug = "tian-ji-shun"
    user_slug_path = os.path.join(DATA_PATH, "followers", user_slug)
    import glob
    json_files = [f for f in glob.glob(os.path.join(user_slug_path, "*.json"))]

    '''
    # 改成对象传递
    follower_count = VarContainer(0)
    male_count = VarContainer(0)
    female_count = VarContainer(0)
    unknown_gender_count = VarContainer(0)
    '''
    # counter = {"follower_count": 0, "male_count": 0,
    #    "female_count": 0, "unknown_gender_count": 0}
    count = Count()
    """
    一个文件池子
    如果是n=4线程
    每次读4个文件
    """
    queue = [(file, count, ) for file in json_files]
    print(len(queue))
    # return
    thread_pool = threadpool.ThreadPool(4)
    requests_ = threadpool.makeRequests(
        Counter.run, queue)
    [thread_pool.putRequest(req) for req in requests_]

    thread_pool.wait()

    print("女性粉丝有{}个，男性粉丝有{}个, 未写性别{}个".format(
        d["female_count"], d["male_count"], d["unknown_gender_count"]))
    print("一共%d个粉丝😆" %
          (d["female_count"]+d["male_count"]+d["unknown_gender_count"]))
    print("女粉丝ratio: %f" % (d["female_count"]/d["male_count"]))


if __name__ == "__main__":
    main()
