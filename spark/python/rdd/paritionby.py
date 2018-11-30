# -*- coding:utf-8 -*-

import urlparse
from pyspark import SparkConf, SparkContext

conf = (SparkConf()
    .setMaster('local')
    .setAppName("parititionby transform")
    .set("spark.executor.memory", "2g")
)
sc = SparkContext(conf=conf)
rdd = sc.parallelize([
    'www.baidu.com',
    'www.google.com', 
    'www.sina.com.cn',
    'www.youku.com',
    'www.163.com',
    'www.jd.com',
    'www.renren.com',
    'www.mi.com',
    'mp3.baidu.com',
    'music.baidu.com',
    'fang.sina.com.cn',
    'www.sogou.com',
    'www.sohu.com',
    'tv.sohu.com',
    'www.iqiyi.com',
    'www.pptv.com',
    'www.jianshu.com',
    'www.qq.com',
    'weixin.qq.com',
    'www.zhihu.com',
    'www.douban.com',
    'www.huaban.com',
    'www.jumei.com',
    'www.meituan.com',
]

def hash_domain(url):
    return hash(urlparse.urlparse(url).netloc)

rdd.partitionBy(20, hash_domain) # 创建20个分区
