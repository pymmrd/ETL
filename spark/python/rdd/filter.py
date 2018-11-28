# -*- coding:utf-8 -*-

import os

from pyspark import SparkConf, SparkContext

conf = (SparkConf()
    .setMaster('local')
    .setAppName("filter transform")
    .set("spark.executor.memory", "2g")
)
sc = SparkContext(conf=conf)
file_path = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    'data',
    'README.md'
))

fileRDD = sc.textFile("file://%s" % file_path)
apacheRDD = fileRDD.filter(lambda line: "Apache" in line)
apacheRDD.cache()
print apacheRDD.count()
print apacheRDD.first()
print apacheRDD.collect()


