# -*- coding: utf-8 -*-

from tidb_log_parser import InvalidTiDBLogError
from tidb_log_parser.slowquerylog import SlowQueryLog

LOG_FILE = '../logs/tidb_log_example.log'


class TiDBLogParser(object):

    @classmethod
    def parse(cls, log_file):
        with open(log_file) as f:
            slow_query_logs = []
            for line in f:
                if 'SLOW_QUERY' in line:
                    try:
                        slow_query_log = SlowQueryLog(line)
                        # debug:
                        print(slow_query_log)
                        slow_query_logs.append(slow_query_log)
                    except InvalidTiDBLogError as e:
                        print(e)
                        continue
            print('total slow query count: %d' % len(slow_query_logs))


if __name__ == '__main__':
    TiDBLogParser.parse(LOG_FILE)
