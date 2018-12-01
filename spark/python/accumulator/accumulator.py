# -*- coding:utf-8 -*-

"""
    累加器,提供了将工作节点中的值聚合到驱动器程序中的简单语法。
累加器的一个常见用途是在调试时对作业执行过程中的事件进行计数。
例如,假设我们在从文件中读取呼号列表对应的日志,同时也想知道输入
文件中有多少空行。
    执行完转化操作之后,就打印出累加器中的值。注意,只有在运行
saveAsTextFile()行动操作后才能看到正确的计数,因为行动操作前
的转化操作flatMap()是惰性的,所以作为计算副产品的累加器只有
在惰性的转化操作flatMap()被saveAsTextFile()行动操作强制触发
时才会开始求值。
    总结起来,累加器的用法如下所示。
•通过在驱动器中调用SparkContext.accumulator(initialValue)方法,创建出存有初
始值的累加器。返回值为org.apache.spark.Accumulator[T]对象,其中T是初始值
initialValue的类型。

•Spark闭包里的执行器代码可以使用累加器的+=方法(在Java中是add)增加累加器的值。

•驱动器程序可以调用累加器的value属性(在Java中使用value()或setValue())来访
问累加器的值
"""


import os
import sys

from pyspark import SparkConf, SparkContext

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print "Error usage: accumulator [sparkmaster] [inputfile] [outputfile]"
    master = sys.argv[1]
    inputFile = sys.argv[2]
    outputFile = sys.argv[3]
    conf = (SparkConf()
        .setMaster(master)
        .setAppName("acumulator")
        .set("spark.executor.memory", "2g")
    )
    sc = SparkContext(conf=conf)
    inputRDD = sc.textFile(inputFile)
    # 创建Accumulator[Int]并初始化为0
    blankLines = sc.accumulator(0)

    def extractCallSigns(line):
        global blankLines # 访问全局变量
        if (line == ""):
            blankLines += 1
        return line.split(" ")

    callSigns = inputRDD.flatMap(extractCallSigns)
    callSigns.saveAsTextFile(outputFile + "/callsigns")
    print "Blank lines: %d" % blankLines.value
