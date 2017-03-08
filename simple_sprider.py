#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from pyquery import PyQuery as pq


def main():
    page = 1
    url = 'http://www.qiushibaike.com/hot/page/' + str(page)
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, sdch",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Host": "www.qiushibaike.com",
        "Proxy-Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    }
    d = pq(url, headers=headers)
    with open("/Users/huweijie/Documents/usernames.txt", "w+") as f:
        parm = "div[class='author clearfix']"
        for item in d(parm):
            for aitems in pq(item).find("a[title]"):
                f.write(pq(aitems).attr("title") + "\n")


if __name__ == '__main__':
    main()
