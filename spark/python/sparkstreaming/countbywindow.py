#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import print_function
import sys
from pyspark import SparkContext
from pyspark.streaming import StreamingContext


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: countbywindow.py <hostname> <port>", file=sys.stderr)
        #exit(-1)
    sc = SparkContext(appName="countbywindow")

    # 每2秒计算一次
    ssc = StreamingContext(sc, 2)
    ssc.checkpoint("hdfs://localhost:8020/checkpoint_window")
    lines = ssc.socketTextStream(sys.argv[1], int(sys.argv[2]))
    # 返回指定长度窗口中的元素个数。
    countw = lines.countByWindow(6, 4)
    countw.pprint()
    ssc.start()
    ssc.awaitTermination()
