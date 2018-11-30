# -*- coding:utf-8 -*-

"""
textFile以行为单位读取文件内容作为RDD元素
"""
import os

from pyspark import SparkConf, SparkContext

conf = (SparkConf()
    .setMaster('local')
    .setAppName("textFile input")
    .set("spark.executor.memory", "2g")
)
sc = SparkContext(conf=conf)

file_path = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    'data',
    'README.md'
))

inputRDD = sc.textFile("file://%s" % file_path)
print inputRDD.collect()
