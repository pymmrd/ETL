#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import print_function
import re
import sys
from pyspark import SparkContext
from pyspark.streaming import StreamingContext

def get_ip(rdd):
    # print(rdd)
    ip = ''
    regx = re.compile("(?P<id>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})")
    match = regx.search(rdd)
    if match is not None:
        ip = match.group('id')
    return ip 


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: error_count.py <hostname> <port>", file=sys.stderr)
        #exit(-1)
    sc = SparkContext(appName="PythonStreamingErrorCount")

    # 每5秒计算一次
    ssc = StreamingContext(sc, 2)
    ssc.checkpoint("hdfs://localhost:8020/checkpoint_window")

    lines = ssc.socketTextStream(sys.argv[1], int(sys.argv[2]))
    # 该操作由一个DStream对象调用，传入一个窗口长度参数，
    # 一个窗口移动速率参数，然后将当前时刻当前长度窗口中
    # 的元素取出形成一个新的DStream。
    #window = lines.window(6, 4)
    #window.pprint()

    # 返回指定长度窗口中的元素个数。
    #countw = lines.countByWindow(6, 4)
    #countw.pprint()

    pairs = lines.map(get_ip).map(lambda ip:(ip, 1))
    windowpairs = pairs.reduceByKeyAndWindow(lambda a, b: a+b, lambda a, b: a-b, 6, 4)
    windowpairs.pprint()
    #error_lines = lines.filter(lambda line: 'error' in line)
    #error_lines.pprint()

    ssc.start()
    ssc.awaitTermination()
