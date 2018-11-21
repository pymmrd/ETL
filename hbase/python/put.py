# -*- coding:utf-8 -*-

"""
Hbase Trift2 put API

TPut属性：
  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'row', None, None, ), # 1
    (2, TType.LIST, 'columnValues', (TType.STRUCT,(TColumnValue, TColumnValue.thrift_spec)), None, ), # 2
    (3, TType.I64, 'timestamp', None, None, ), # 3
    None, # 4
    (5, TType.MAP, 'attributes', (TType.STRING,None,TType.STRING,None), None, ), # 5
    (6, TType.I32, 'durability', None, None, ), # 6
    (7, TType.STRUCT, 'cellVisibility', (TCellVisibility, TCellVisibility.thrift_spec), None, ), # 7
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
"""

# Third-party imports
from thrift.transport import TSocket, TTransport
#from thrift.protocol import TBinaryProtocol
from thrift.protocol import TCompactProtocol

from hbase import THBaseService
from hbase.ttypes import TPut, TColumnValue

from datetime import datetime

transport = TSocket.TSocket('localhost', 9999)
transport = TTransport.TFramedTransport(transport)
protocol = TCompactProtocol.TCompactProtocol(transport)
client = THBaseService.Client(protocol)

table = 't1'
rowkey = 'r4'
transport.open() 
columnvalues = [
    TColumnValue(
        family='f1',
        qualifier='c4',
        value='v4',
    ),
    TColumnValue(
        family='f1',
        qualifier='c42',
        value='v42',
    ),
    TColumnValue(
        family='f1',
        qualifier='c42',
        value='v42',
    )
]
put = TPut(
    row=rowkey,
    columnValues=columnvalues,
)
client.put(table, put)
transport.close() 
