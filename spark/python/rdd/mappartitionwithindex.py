# -*- coding:utf-8 -*-

from pyspark import SparkConf, SparkContext

conf = (SparkConf()
    .setMaster('local')
    .setAppName("mappartitionswithindex transform")
    .set("spark.executor.memory", "2g")
)
sc = SparkContext(conf=conf)

x = sc.parallelize([1, 2, 3, 4], 2) 
def f(splitIndex, iterator): 
    yield (splitIndex, sum(iterator))

y = x.mapPartitionsWithIndex(f)
print 'x原来分区信息：{0}'.format(x.glom().collect())
print 'x经过f计算后的结果：{}'.format(y.glom().collect())

#x原来分区信息：[[1, 2], [3, 4]]
#x经过f计算后的结果：[[(0, 3)], [(1, 7)]]


