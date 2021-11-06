#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import requests
import sys
from datetime import datetime


USER_IDS = [
    "1851755225",  # 浙江大学
    "1768409523",  # 南京大学
    "3237705130",  # 北京大学
    "1676317545",  # 清华大学
    "1729332983",  # 复旦大学
    "1739746697",  # 上海交通大学
    "2975787954",  # 中国人民大学
    "1823887605",  # 中科大
    "1865154537",  # 同济大学
    "1666177401",  # 武汉大学
    "1879192935",  # 厦门大学
    "3624694175",  # 四川大学
    "1851774145",  # 南开大学
    "1663414103",  # 华中科技大学
    "1871729063",  # 天津大学
    "1892723783",  # 中山大学
    "1873625985",  # 哈尔滨工业大学
    "1862928653",  # 西安交通大学
    "1703010470",  # 东南大学
    "1865345137",  # 北京交通大学
    "5396134858",  # 北京航天航空大学
    "1805101535",  # 南京航天航空大学
    "5016338752",  # 郑州大学
    "3552074150",  # 牛津大学
]

README_TEMPLATE = """
# 中国高校微博排行

按官方微博粉丝数量进行排名。

Python 3 单文件脚本（ `run.py` ），仅依赖 [requests](https://github.com/psf/requests) 进行数据爬取。

输出样例（{}获取）：

```
{}
```

目前高校数量：24。如需添加，可在 issue 中提出。
"""


def get_json(params):
    url = "https://m.weibo.cn/api/container/getIndex?"
    r = requests.get(url, params=params)
    return r.json()


def progress(current, total):
    max_len = 80
    filled = current * max_len // total
    print("\r[", end="")
    for _ in range(filled):
        print("=", end="")
    for _ in range(max_len - filled):
        print(" ", end="")
    print("]", end="")


def parse(s):
    if s.endswith("万"):
        return int(float(s[:-1]) * 10000)
    else:
        return int(s)


def parse_inv(n):
    if n < 10000:
        return str(n)
    else:
        return str(n / 10000) + "万"


if __name__ == "__main__":
    run_in_github_actions = len(sys.argv) > 1 and sys.argv[1] == "--run-in-gh"

    schools = []
    count = 0
    for user_id in USER_IDS:
        count += 1
        params = {"containerid": "100505" + user_id}
        js = get_json(params)
        if js["ok"]:
            info = js["data"]["userInfo"]
            school = {}
            school["name"] = info.get("screen_name", "")
            school["s_count"] = info.get("statuses_count", 0)
            school["f_count"] = parse(info.get("followers_count", 0))
            schools.append(school)
            if not run_in_github_actions:
                progress(count, len(USER_IDS))
        else:
            print("ERROR in %s" % user_id)

    schools.sort(key=lambda x: x["f_count"], reverse=True)

    output = ""

    header = "\n{1:>2}{2:{0}^12}{3:>12}{4:>12}".format(
        chr(12288), "排名", "校名", "微博数", "粉丝数"
    )
    if not run_in_github_actions:
        print(header)
    else:
        output += header + "\n"

    rank = 1
    for s in schools:
        line = "{1:>3}{2:{0}^12}{3:>14,}{4:>12}".format(
            chr(12288), rank, s["name"], s["s_count"], parse_inv(s["f_count"])
        )
        if not run_in_github_actions:
            print(line)
        else:
            output += line + "\n"
        rank += 1

    if not run_in_github_actions:
        print("\nDone.")
    else:
        with open("README.md", "w") as f:
            f.write(
                README_TEMPLATE.format(
                    datetime.today().strftime("%Y年%m月%d日%H时%M分%S秒"), output
                )
            )
