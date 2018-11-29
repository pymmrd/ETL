# -*- coding:utf-8 -*-


from pyspark import SparkConf, SparkContext

conf = (SparkConf()
    .setMaster('local')
    .setAppName("pairrdd transform")
    .set("spark.executor.memory", "2g")
)
sc = SparkContext(conf=conf)

alist = [(1, 2), (3, 4), (3, 6)]

def reducebykey(x, y):
    """
    x--->4
    y--->6
    """
    print 'x--->', x
    print 'y--->', y
    return x + y

rdd = sc.parallelize(alist)
# 合并具有相同的键
rdd.reduceBykey(lambda x, y: x+y).collect() # [(1, 2), (3, 10)]

# 对具有相同键的值进行分组
"""
[(1, <pyspark.resultiterable.ResultIterable at 0x7f9be85c3050>),
 (3, <pyspark.resultiterable.ResultIterable at 0x7f9be85d0190>)]
"""
rdd.groupByKey().collect() # [(1, [2]), (3, [4, 6])]

# 使用不同的返回类型合并具有相同键的值
#TODO combineByKey(createCombiner, mergeCombiners, partitioner)

# 对pari RDD中的每个值应用一个函数而不改变键
rdd.mapValues(lambda x: x+1).collect() # [(1, 3), (3, 5), (3, 7)]

# 对pari RDD中的每个值应用一个返回迭代器的函数，然后对返回的每个元素
# 都生成一个对应原键的键值对记录。通常用户符号化

rdd.flatMapValues(lambda x: range(x, 6)).collect() 
# [(1, 2), (1, 3), (1, 4), (1, 5), (3, 4), (3, 5)]

rdd.keys().collect() # [1, 3, 3]

rdd.values().collect() #  [2, 4, 6]

# 返回一个根据键排序的RDD
rdd.sortByKey().collect() # [(1, 2), (3, 4), (3, 6)]

