#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import print_function
import sys
from pyspark import SparkContext
from pyspark.streaming import StreamingContext


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: error_count.py <hostname> <port>", file=sys.stderr)
        #exit(-1)
    sc = SparkContext(appName="PythonStreamingErrorCount")

    # 每5秒计算一次
    ssc = StreamingContext(sc, 5)

    lines = ssc.socketTextStream(sys.argv[1], int(sys.argv[2]))
    lines.pprint()
    #error_lines = lines.filter(lambda line: 'error' in line)

    #error_lines.pprint()

    ssc.start()
    ssc.awaitTermination()
