# -*- coding:utf-8 -*-


from pyspark import SparkConf, SparkContext

"""
fold操作解析
"""



conf = (SparkConf()
    .setMaster('local')
    .setAppName("rdd fold action transform")
    .set("spark.executor.memory", "2g")
)
sc = SparkContext(conf=conf)

def add(x, y):
    """
    x---> 0
    y---> 1
    x---> 1
    y---> 2
    x---> 3
    y---> 3
    """
    print 'x--->', x
    print 'y--->', y
    return x + y

alist = [1, 2, 3]
print sc.parallelize(alist).fold(0, add)
