# -*- coding:utf-8 -*-


"""
aggregate() 时,需要提供我们期待返回的类型的初始值。然后
通过一个函数把 RDD 中的元素合并起来放入累加器。考虑到每个节点是在本地进行累加
的,最终,还需要提供第二个函数来将累加器两两合并。
"""

from pyspark import SparkConf, SparkContext

conf = (SparkConf()
    .setMaster('local')
    .setAppName("rdd aggregate action transform")
    .set("spark.executor.memory", "2g")
)

sc = SparkContext(conf=conf)

alist = [1, 2, 3, 3]

rdd = sc.parallelize(alist)

def seqOp(x, y):
    """
    x---> (0, 0)
    y---> 1
    x---> (1, 1)
    y---> 2
    x---> (3, 2)
    y---> 3
    x---> (6, 3)
    y---> 3

    """
    print 'x--->', x
    print 'y--->', y
    return (x[0] + y, x[1] + 1) 

def accOp(acc1, acc2):
    """
    acc1----> (0, 0)
    acc2----> (9, 4)
    """
    print 'acc1---->', acc1
    print 'acc2---->', acc2
    return (acc1[0] + acc2[0], acc1[1] + acc2[1])

print rdd.aggregate(
    (0, 0),
    seqOp,
    accOp
)
