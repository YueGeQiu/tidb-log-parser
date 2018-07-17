# -*- coding: utf-8 -*-

from tidb_log_parser import InvalidTiDBLogError
from tidb_log_parser.slowquerylog import SlowQueryLog

LOG_FILE = '../logs/tidb_log_example.log'

with open(LOG_FILE) as f:
    slow_query_logs = []
    for line in f:
        if 'SLOW_QUERY' in line:
            try:
                slow_query_log = SlowQueryLog(line)
                # debug:
                print(slow_query_log.date)
                print(slow_query_log.source_file)
                print(slow_query_log.level)
                print(slow_query_log.log_msg)
                print('cost: ' + slow_query_log.cost_time)
                print('sql: ' + slow_query_log.sql)
                print('-' * 5)
                slow_query_logs.append(slow_query_log)
            except InvalidTiDBLogError as e:
                print(e)
                continue
    print('total slow query count: %d' % len(slow_query_logs))
