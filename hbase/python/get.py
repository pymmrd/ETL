# -*- coding:utf-8 -*-

"""
HBase Thrift2 get函数API说明

TGet属性:
  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'row', None, None, ), # 1
    (2, TType.LIST, 'columns', (TType.STRUCT,(TColumn, TColumn.thrift_spec)), None, ), # 2
    (3, TType.I64, 'timestamp', None, None, ), # 3
    (4, TType.STRUCT, 'timeRange', (TTimeRange, TTimeRange.thrift_spec), None, ), # 4
    (5, TType.I32, 'maxVersions', None, None, ), # 5
    (6, TType.STRING, 'filterString', None, None, ), # 6
    (7, TType.MAP, 'attributes', (TType.STRING,None,TType.STRING,None), None, ), # 7
    (8, TType.STRUCT, 'authorizations', (TAuthorization, TAuthorization.thrift_spec), None, ), # 8
  )

TColumn属性:
  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'family', None, None, ), # 1
    (2, TType.STRING, 'qualifier', None, None, ), # 2
    (3, TType.I64, 'timestamp', None, None, ), # 3
  )

TColumnValue属性:
  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'family', None, None, ), # 1
    (2, TType.STRING, 'qualifier', None, None, ), # 2
    (3, TType.STRING, 'value', None, None, ), # 3
    (4, TType.I64, 'timestamp', None, None, ), # 4
    (5, TType.STRING, 'tags', None, None, ), # 5
  )

TGet返回值：
    [
        TColumnValue(
            value='v4',
            tags=None,
            qualifier='c4',
            family='f1',
            timestamp=1542761774049
        ),
        TColumnValue(
            value='v42',
            tags=None,
            qualifier='c42',
            family='f1',
            timestamp=1542761774049
        )
    ]
"""

# Third-party imports
from thrift.transport import TSocket, TTransport
#from thrift.protocol import TBinaryProtocol
from thrift.protocol import TCompactProtocol

from hbase import THBaseService
from hbase.ttypes import TGet, TColumn

from datetime import datetime

transport = TSocket.TSocket('localhost', 9999)
transport = TTransport.TFramedTransport(transport)
protocol = TCompactProtocol.TCompactProtocol(transport)
client = THBaseService.Client(protocol)

table = 't1'
rowkey = 'r4'
get = TGet(
    row=rowkey,
    columns=[
        #TColumn(family='f1', qualifier='c1') # 取出列簇f1的c1列
        TColumn(family='f1') # 取出列簇f1的所有列
    ],
    maxVersions=2,
)
transport.open() 
result = client.get(table,get)
values = result.columnValues
adict = {}
for val in values:
    adict[val.qualifier] = val.value
print adict
transport.close() 

