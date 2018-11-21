# -*- coding:utf-8 -*-

"""
TScan属性:
  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'startRow', None, None, ), # 1
    (2, TType.STRING, 'stopRow', None, None, ), # 2
    (3, TType.LIST, 'columns', (TType.STRUCT,(TColumn, TColumn.thrift_spec)), None, ), # 3
    (4, TType.I32, 'caching', None, None, ), # 4
    (5, TType.I32, 'maxVersions', None, 1, ), # 5
    (6, TType.STRUCT, 'timeRange', (TTimeRange, TTimeRange.thrift_spec), None, ), # 6
    (7, TType.STRING, 'filterString', None, None, ), # 7
    (8, TType.I32, 'batchSize', None, None, ), # 8
    (9, TType.MAP, 'attributes', (TType.STRING,None,TType.STRING,None), None, ), # 9
    (10, TType.STRUCT, 'authorizations', (TAuthorization, TAuthorization.thrift_spec), None, ), # 10
    (11, TType.BOOL, 'reversed', None, None, ), # 11
    (12, TType.BOOL, 'cacheBlocks', None, None, ), # 12
    (13, TType.MAP, 'colFamTimeRangeMap', (TType.STRING,None,TType.STRUCT,(TTimeRange, TTimeRange.thrift_spec)), None, ), # 13
    (14, TType.I32, 'readType', None, None, ), # 14
    (15, TType.I32, 'limit', None, None, ), # 15
  )
"""

# Third-party imports
from thrift.transport import TSocket, TTransport
#from thrift.protocol import TBinaryProtocol
from thrift.protocol import TCompactProtocol

from hbase import THBaseService
from hbase.ttypes import TScan

from datetime import datetime

transport = TSocket.TSocket('localhost', 9999)
transport = TTransport.TFramedTransport(transport)
protocol = TCompactProtocol.TCompactProtocol(transport)
client = THBaseService.Client(protocol)

table = 't1'
transport.open() 
filterString = "ValueFilter(=, 'binary:v11')"
filterString = "ColumnPrefixFilter('c') AND ( ValueFilter(=,'substring:v2') OR ValueFilter(=,'substring:v4') )" 
#filterString = "RowFilter.new(CompareFilter::CompareOp.valueOf('EQUAL'), SubstringComparator.new('r'))"
scanner_id = client.openScanner(
    table=table,
    tscan=TScan(
        startRow='r1',
        stopRow='r5',
        filterString=filterString
        #columns=[TColumn('cf', '1015')]
    )
)
try:
    num_rows = 10
    while True:
        tresults = client.getScannerRows(scanner_id, num_rows)
        for tresult in tresults:
            print(tresult.columnValues)
        if len(tresults) < num_rows:
            break
finally:
    client.closeScanner(scanner_id)
transport.close() 


