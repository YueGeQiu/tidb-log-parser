# -*- coding: utf-8 -*-

LOG_FILE = '../logs/tidb_log_example.log'

from tidb_log_parser import InvalidTiDBLogError
from tidb_log_parser import TiDBLog

with open(LOG_FILE) as f:
    # FIXME: now only test with top 5 lines
    count = 0
    for line in f:
        if count == 5:
            break
        try:
            tidb_log = TiDBLog(line)
            # debug:
            print(tidb_log.date)
            print(tidb_log.source_file)
            print(tidb_log.level)
            print(tidb_log.log_msg)
            print('-' * 5)
        except InvalidTiDBLogError as e:
            print(e)
            continue
        count += 1
