# -*- coding: utf-8 -*-

import re
from tidb_log_parser import TiDBLog
from tidb_log_parser import TiDBLogError

SLOW_QUERY_REGEX = r'.*cost_time\:(.*?)\s+.*sql\:(.*)'


class SlowQueryFormatError(TiDBLogError):
    pass


class SlowQueryLog(TiDBLog):
    """ class representing slow query """

    def __init__(self, log_text):
        # slow query attributes
        self.cost_time = None
        self.sql = None
        super(SlowQueryLog, self).__init__(log_text)

    def _parse(self, log_text):
        super(SlowQueryLog, self)._parse(log_text)
        # extract slow query information from log message
        m = re.match(SLOW_QUERY_REGEX, self.log_msg)
        if not m:
            print(self.log_msg)
            raise SlowQueryFormatError('slow query log format not matched')
        self.cost_time = m.group(1)
        self.sql = m.group(2)
