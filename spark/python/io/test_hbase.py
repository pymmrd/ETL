# -*- coding:utf-8 -*-

from pyspark import SparkContext,SparkConf


conf = SparkConf()
sc = SparkContext(conf=conf)
host = 'localhost'
table = 'hbase_lecture10'

def read_hbase():
    conf = {"hbase.zookeeper.quorum": host, "hbase.mapreduce.inputtable": table}
    keyConv = "org.apache.spark.examples.pythonconverters.ImmutableBytesWritableToStringConverter"
    valueConv = "org.apache.spark.examples.pythonconverters.HBaseResultToStringConverter"

    hbase_rdd = sc.newAPIHadoopRDD(
        "org.apache.hadoop.hbase.mapreduce.TableInputFormat",
        "org.apache.hadoop.hbase.io.ImmutableBytesWritable",
        "org.apache.hadoop.hbase.client.Result",
        keyConverter=keyConv,
        valueConverter=valueConv,
        conf=conf
    )
    count = hbase_rdd.count()
    hbase_rdd.cache()
    output = hbase_rdd.collect()
    for (k, v) in output:
        print (k, v)


def write_hbase():
    keyConv = "org.apache.spark.examples.pythonconverters.StringToImmutableBytesWritableConverter"
    valueConv = "org.apache.spark.examples.pythonconverters.StringListToPutConverter"
    conf = {
        "hbase.zookeeper.quorum": host,
        "hbase.mapred.outputtable": table,
        "mapreduce.outputformat.class": "org.apache.hadoop.hbase.mapreduce.TableOutputFormat",
        "mapreduce.job.output.key.class": "org.apache.hadoop.hbase.io.ImmutableBytesWritable",
        "mapreduce.job.output.value.class": "org.apache.hadoop.io.Writable"
    }
    rawData = ['wangwu,cf1,score,80','zhuoqi,cf1,score,90']
    #( rowkey , [ row key , column family , column name , value ] )
    sc.parallelize(rawData).map(
        lambda x: (x[0], x.split(','))
    ).saveAsNewAPIHadoopDataset(
        conf=conf,
        keyConverter=keyConv,
        valueConverter=valueConv
    )


if __name__ == "__main__":
    write_hbase()


