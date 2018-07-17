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
        self._cost_time = None
        self.sql = None
        super(SlowQueryLog, self).__init__(log_text)

    def _parse(self, log_text):
        super(SlowQueryLog, self)._parse(log_text)
        # extract slow query information from log message
        m = re.match(SLOW_QUERY_REGEX, self.log_msg)
        if not m:
            print(self.log_msg)
            raise SlowQueryFormatError('slow query log format not matched')
        self._cost_time = m.group(1)
        self.sql = m.group(2)

    def __str__(self):
        text = '---\n'
        text += 'Timestamp: %s\n' % self.timestamp
        text += 'Cost (ms): %f\n' % self.cost_time
        text += 'SQL: %s' % self.sql
        return text

    @property
    def cost_time(self):
        try:
            if self._cost_time.endswith('ms'):
                return float(self._cost_time[:-2])
            elif self._cost_time.endswith('s'):
                return float(self._cost_time[:-1]) * 1000
            else:
                raise ValueError
        except ValueError:
            print("unknown time unit: %s" % self._cost_time)
            return -1


