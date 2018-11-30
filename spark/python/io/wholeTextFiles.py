# -*- coding:utf-8 -*-

"""
wholeTextFiles以文件名为键， 以文件整体内容为值
"""

import os

from pyspark import SparkConf, SparkContext

conf = (SparkConf()
    .setMaster('local')
    .setAppName("wholeTextFiles input")
    .set("spark.executor.memory", "2g")
)
sc = SparkContext(conf=conf)

file_path = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    'data',
    'README.md'
))

inputRDD = sc.wholeTextFiles("file://%s" % file_path)
print inputRDD.collect()
