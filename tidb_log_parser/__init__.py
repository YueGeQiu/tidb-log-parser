# -*- coding: utf-8 -*-

import re

# FIXME: find better way to make this configurable and flexible
# ? is for non-greedy matching
LOG_REGEX = r'(.*?)\:\s*(\[.*?\])\s*(.*)'


class TiDBLogError(Exception):
    pass


class InvalidTiDBLogError(TiDBLogError):
    pass


class TiDBLog(object):

    def __init__(self, log_text):
        """ constructor with one ling log text

        :param log_text: whole line of the log text
        """
        if not log_text:
            raise TiDBLogError("Empty log text")
        log_text = str.strip(log_text)
        # attributes
        self.date = None
        self.source_file = None
        self.level = None
        self.log_msg = ''
        self._parse(log_text)

    def _parse(self, log_text):
        """ parse the log text, extract attributes from the text

        :param log_text:
        :return:
        """
        m = re.match(LOG_REGEX, log_text)
        if not m:
            raise InvalidTiDBLogError("log pattern not matched")
        # split date time
        date_time_source = m.group(1).split(' ')
        if len(date_time_source) != 3:
            raise InvalidTiDBLogError("Datetime format cannot match")
        self.date = date_time_source[0] + ' ' + date_time_source[1]
        self.source_file = date_time_source[2]
        self.level = m.group(2)[1:-1]
        self.log_msg = m.group(3)
