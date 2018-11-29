# -*- coding:utf-8 -*-

"""
    combineByKey() 会遍历分区中的所有元素,因此每个元素的键要么
还没有遇到过,要么就和之前的某个元素的键相同。如果这是一个新的
元素, combineByKey() 会使用一个叫作createCombiner()的函数来创
建那个键对应的累加器的初始值。
   需要注意的是,这一过程会在每个分区中第一次出现各个键时发生,
而不是在整个RDD中第一次出现一个键时发生。

   如果这是一个在处理当前分区之前已经遇到的键,它会使用mergeValue()
方法将该键的累加器对应的当前值与这个新的值进行合并。

   由于每个分区都是独立处理的,因此对于同一个键可以有多个累加器。
如果有两个或者更多的分区都有对应同一个键的累加器,就需要使用用户
提供的mergeCombiners()方法将各个分区的结果进行合并。
  
  下面的程序求每个键的平均值
"""

from pyspark import SparkConf, SparkContext

conf = (SparkConf()
    .setMaster('local')
    .setAppName("pairrdd  combinebykey transform")
    .set("spark.executor.memory", "2g")
)
sc = SparkContext(conf=conf)



alist = [(1, 2), (2, 4), (3, 6), (1, 4), (2, 3), (1, 3)]
rdd = sc.parallelize(alist, 3)


def createCombiner(x):
    """
    把在分区中第一次出现的键值作为参数传过来
    """
    return (x, 1)


def mergeValue(x, y):
    """
    当分区中已经出现过相同的键，把键值作为参数传过来
    """
    # 把createCombiner返回的值进行迭代处理
    # 值求和作为x[0] + y(相同键的值), 次数求和x[1] + 1
    return (x[0] + y, x[1] + 1)


def mergeCombiners(x, y):
    """
    当数据处于不同分区时，进行迭代器数据汇总处理, 有
    多少个分区会调用多次。
    """
    return (x[0] + y[0], x[1] + y[1])

def avg(item): 
    return (item[0], item[1][0]/ item[1][1]) 

sumCount = rdd.combineByKey(createCombiner, mergeValue, mergeCombiners)
sumCount.map(avg).collectAsMap()
