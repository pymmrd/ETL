# -*- coding:utf-8 -*-

"""
wholeTextFiles以文件名为键， 以文件整体内容为值
"""

import os

from pyspark import SparkConf, SparkContext

def read_file():
    file_path = os.path.abspath(
        os.path.join(
            os.path.dirname(
                os.path.dirname(__file__),
            ),
        'data',
        'README.md'
        )
    )
    inputRDD = sc.wholeTextFiles("file://%s" % file_path)
    print inputRDD.collect()
    return inputRDD


def read_directory():
    dir_path = os.path.abspath(
        os.path.join(
            os.path.dirname(
                os.path.dirname(__file__)
            ),
            'data',
            'fake_logs',
        )
    )
    inputRDD = sc.wholeTextFiles("file://%s" % dir_path)
    print inputRDD.count()
    return inputRDD


def read_with_wildcard():
    log_files = os.path.abspath(
        os.path.join(
            os.path.dirname(
                os.path.dirname(__file__)
            ),
            'data',
            'fake_logs',
            '*.log'
        )
    )
    inputRDD = sc.wholeTextFiles("file://%s" % log_files)
    print inputRDD.collect()
    return inputRDD



def output(result):
    outputpath = os.path.abspath(
        os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            'data',
            'output',
        )
    )
    result.saveAsTextFile(outputpath)


if __name__ == "__main__":
    conf = (SparkConf()
        .setMaster('local')
        .setAppName("wholeTextFiles input")
        .set("spark.executor.memory", "2g")
    )
    sc = SparkContext(conf=conf)
    #inputRDD = read_file()
    #inputRDD = read_directory()
    inputRDD = read_with_wildcard()
    output(inputRDD)
