#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
-------------------------------------------
Time: 2018-12-05 22:29:30
-------------------------------------------
(u'192.168.0.6', 1)

-------------------------------------------
Time: 2018-12-05 22:29:34
-------------------------------------------
(u'192.168.0.7', 1)


"""

from __future__ import print_function
import re
import sys
from pyspark import SparkContext
from pyspark.streaming import StreamingContext

def parse_ip(rdd):
    # print(rdd)
    ip = ''
    regx = re.compile("(?P<id>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})")
    match = regx.search(rdd)
    if match is not None:
        ip = match.group('id')
    return ip 


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: reducebykeyandwindow.py <hostname> <port>", file=sys.stderr)
        #exit(-1)
    sc = SparkContext(appName="reducebykeyandwinow")

    # 每2秒计算一次
    ssc = StreamingContext(sc, 2)
    ssc.checkpoint("hdfs://localhost:8020/checkpoint_window")
    lines = ssc.socketTextStream(sys.argv[1], int(sys.argv[2]))
    pairs = lines.map(parse_ip).map(lambda ip:(ip, 1))
    #TODO 下面这种情况发现执行的时间和流统计时间同步, 每两秒执行一次
    #noinvpairs = pairs.reduceByKeyAndWindow(lambda a, b: a+b, 6, 4)
    #noinvpairs.pprint()

    #TODO 下面这种情况和窗口滑动长度一样，每4秒执行一次
    windowpairs = pairs.reduceByKeyAndWindow(
        lambda a, b: a+b,
        lambda a, b: a-b,
        6,
        4
    )
    windowpairs.pprint()
    ssc.start()
    ssc.awaitTermination()
