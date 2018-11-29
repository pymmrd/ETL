# -*- coding:utf-8 -*-


from pyspark import SparkConf, SparkContext

conf = (SparkConf()
    .setMaster('local')
    .setAppName("pairrdd transform")
    .set("spark.executor.memory", "2g")
)
sc = SparkContext(conf=conf)

alist = [(1, 2), (3, 4), (3, 6)]
other = [(3, 9)]

def reducebykey(x, y):
    """
    x--->4
    y--->6
    """
    print 'x--->', x
    print 'y--->', y
    return x + y

rdd = sc.parallelize(alist)

other_rdd = sc.parallelize(other)

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
# 以字符串顺序对整数进行自定义排序
rdd.sortByKey(
    ascending=True,
    numPartitions=None,
    keyfunc=lambda x: str(x)
).collect() # [(1, 2), (3, 4), (3, 6)]

# 删除RDD中键与other RDD中的键相同的元素
rdd.subtactByKey(other_rdd).collect() # [(1, 2)]

# 对两个RDD进行内连接
rdd.join(other_rdd).collect() # [(3, (4, 9)), (3, (6, 9))]

# 对两个RDD进行连接操作，确保第一个RDD的键必须存在
rdd.rightOuterJoin(other_rdd).collect() # [(3, (4, 9)), (3, (6, 9))]

# 对两个RDD进行连接操作，确保第二哥RDD的键必须存在
rdd.leftOuterJoin(other_rdd).collect() # [(1, (2, None)), (3, (4, 9)), (3, (6, 9))]

#将两个RDD中拥有相同键的数据分组
rdd.cogroup(other_rdd).collect() # [(1, ([2], [])), (3, ([4, 6], [9]))]

