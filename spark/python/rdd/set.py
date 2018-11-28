# -*- coding:utf-8 -*-

"""
两个RDD做集合操作
union() 生成包含两个RDD中所有元素的RDD
intersection() 求两个RDD中的共同元素的RDD
subtract() 移出一个RDD中的内容
cartesian() 两个RDD的笛卡尔积
"""
from pyspark import SparkConf, SparkContext

conf = (SparkConf()
    .setMaster('local')
    .setAppName("set transform")
    .set("spark.executor.memory", "2g")
)
sc = SparkContext(conf=conf)

alist = [1, 2, 3]
blist = [3, 4, 5]
ardd = sc.parallelize(alist)
brdd = sc.parallelize(blist)
print ardd.union(brdd).collect()
print ardd.intersection(brdd).collect()
print ardd.subtract(brdd).collect()
print ardd.cartesian(brdd).collect()
