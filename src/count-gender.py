#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-19 13:25:00
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import json

from constants import USER_LIST, DATA_PATH, USER


def main():
    # user_slug = USER["知乎小管家"]
    user_slug = "tian-ji-shun"
    user_slug_path = os.path.join(DATA_PATH, "followers", user_slug)

    follower_count = 0
    male_count = 0
    female_count = 0
    unknown_gender_count = 0

    will_break = False
    i = 0
    while True:
        json_file = os.path.join(
            user_slug_path, "followers_{}.json".format(i))
        with open(json_file, "r", encoding="utf-8") as f:
            d = json.loads(f.read())
            if d["paging"]["is_end"]:
                will_break = True
            data = d["data"]
            for _ in data:
                follower_count += 1
                name, gender = _["name"], _["gender"]
                if gender == 0:
                    female_count += 1
                elif gender == 1:
                    male_count += 1
                elif gender == -1:
                    unknown_gender_count += 1
                print(name, gender, follower_count)
            i += 1
            if will_break:
                break

    print("女性粉丝有{}个，男性粉丝有{}个, 未写性别{}个".format(
        female_count, male_count, unknown_gender_count))
    print("一共%d个粉丝😆" % (female_count+male_count+unknown_gender_count))
    print("女粉丝ratio: %f" % (female_count/male_count))


if __name__ == "__main__":
    main()
