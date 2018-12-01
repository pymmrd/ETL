#! /usr/bin/env python
# -*- codign:utf-8 -*-

"""
    Spark 的第二种共享变量类型是广播变量,它可以让程序高效地向所有工作节点
发送一个较大的只读值,以供一个或多个 Spark 操作使用。比如,如果你的应用需要
向所有节点发送一个较大的只读查询表,甚至是机器学习算法中的一个很大的特征向
量,广播变量用起来都很顺手。
    (1) 通过对一个类型 T 的对象调用 SparkContext.broadcast 创建出一个 Broadcast[T] 对象。
    任何可序列化的类型都可以这么实现。
    (2) 通过 value 属性访问该对象的值(在 Java 中为 value() 方法)。
    (3) 变量只会被发到各个节点一次,应作为只读值处理(修改这个值不会影响到别的节点)
"""

# 查询RDD contactCounts中的呼号的对应位置。将呼号前缀
# 读取为国家代码来进行查询
signPrefixes = sc.broadcast(loadCallSignTable())
def processSignCount(sign_count, signPrefixes):
    country = lookupCountry(sign_count[0], signPrefixes.value)
    count = sign_count[1]
    return (country, count)

countryContactCounts = (
    contactCounts
    .map(processSignCount)
    .reduceByKey((lambda x, y: x+ y))
)
countryContactCounts.saveAsTextFile(outputDir + "/countries.txt")
