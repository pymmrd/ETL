# -*- coding:utf-8 -*-
"""
    计算网络数据流中单词的个数, 在本地使用步骤
    (1) $ nc -lk 9999
    (2) $ bin/spark-submit examples/src/main/python/streaming/stateful_network_wordcount.py \
        localhost 9999

    执行情况：
    (1) 默认情况, 程序初始化两个单词
    单词world的updateFunc参数情况:new_values的值[], last_sum的值为1
    单词hello的updateFunc参数情况:new_values的值为[], last_sum的值为1
    -------------------------------------------
    Time: 2018-12-05 21:57:45
    -------------------------------------------
    (u'world', 1)
    (u'hello', 1)

    (2) nc 输出“hello word"的执行情况，此时输入的hello计算值已经
    在上一次保存，word为新增单词。所以不重复单词数量为3

    单词word的updateFunc参数情况:  new_values的值[1], last_sum的值None
    单词world的updateFunc参数情况: new_values的值[], last_sum的值1
    单词hello的updateFunc参数情况: new_values的值[1], last_sum的值1
    -------------------------------------------
    Time: 2018-12-05 21:57:50
    -------------------------------------------
    (u'word', 1)
    (u'world', 1)
    (u'hello', 2)

    (3) nc输入"x y z"后的执行情况
    单词y的updateFunc参数情况: new_values的值[1], last_sum的值None
    单词word的updateFunc参数情况: new_values的值[], last_sum的值1
    单词world的updateFunc参数情况: new_values的值[], last_sum的值1
    单词hello的updateFunc参数情况: new_values的值[], last_sum的值2
    单词x的updateFunc的参数情况: new_values的值[1], last_sum的值None
    单词z的updateFunc的参数情况: new_values的值[1], last_sum的值None
    -------------------------------------------
    Time: 2018-12-05 21:57:55
    -------------------------------------------
    (u'y', 1)
    (u'word', 1)
    (u'world', 1)
    (u'hello', 2)
    (u'x', 1)
    (u'z', 1)

"""
from __future__ import print_function

import sys

from pyspark import SparkContext
from pyspark.streaming import StreamingContext

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: stateful_network_wordcount.py <hostname> <port>", file=sys.stderr)
        exit(-1)
    sc = SparkContext(appName="PythonStreamingStatefulNetworkWordCount")
    ssc = StreamingContext(sc, 5)
    ssc.checkpoint("hdfs://localhost:8020/checkpoint")

    # RDD with initial state (key, value) pairs
    initialStateRDD = sc.parallelize([(u'hello', 1), (u'world', 1)])

    def updateFunc(new_values, last_sum):
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>', new_values, last_sum)
        return sum(new_values) + (last_sum or 0)

    lines = ssc.socketTextStream(sys.argv[1], int(sys.argv[2]))
    running_counts = lines.flatMap(lambda line: line.split(" "))\
                          .map(lambda word: (word, 1))\
                          .updateStateByKey(updateFunc, initialRDD=initialStateRDD)

    running_counts.pprint()

    ssc.start()
    ssc.awaitTermination()
