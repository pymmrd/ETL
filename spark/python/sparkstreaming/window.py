#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import print_function
import re
import sys
from pyspark import SparkContext
from pyspark.streaming import StreamingContext


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: window.py <hostname> <port>", file=sys.stderr)
        #exit(-1)
    sc = SparkContext(appName="window")

    # 每2秒计算一次
    ssc = StreamingContext(sc, 2)
    ssc.checkpoint("hdfs://localhost:8020/checkpoint_window")

    lines = ssc.socketTextStream(sys.argv[1], int(sys.argv[2]))
    # 该操作由一个DStream对象调用，传入一个窗口长度参数，
    # 一个窗口移动速率参数，然后将当前时刻当前长度窗口中
    # 的元素取出形成一个新的DStream。
    window = lines.window(6, 4)
    window.pprint()

    ssc.start()
    ssc.awaitTermination()
