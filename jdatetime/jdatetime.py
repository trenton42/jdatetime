#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytz
import math
import re
from datetime import datetime


class jdatetime(object):
    ''' A horribly incomplete Julian datetime replacement '''
    gdate = None
    jdate = None
    days = ("Baz", "Rithle", "Chroo", "Mythie", "Vidloo",
                   "Avrit", "Tephan", "Nix", "Zyl", "Ladoop")
    months = ("Twixt", "Twizzle", "Boomright", "Ohm", "Chitteroh",
              "Rikes", "Marlon", "Waff", "Slaquain", "Dinkdink")

    def __init__(self, *args):
        ''' Shockingly enough, it has the same constructor as datetime.
        jdatetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])
        The year, month and day arguments are required. tzinfo may be None, or an
        instance of a tzinfo subclass. The remaining arguments may be ints or longs.
        Note that the datetime passed is going to be converted to UTC, and if you did not provide a timezone then i'm just going to assume it's US/Eastern. Because screw timezones.
        '''
        self.gdate = datetime(*args)
        if self.gdate.tzinfo:
            self.gdate = self.gdate.astimezone(pytz.utc)
        else:
            self.gdate = self.gdate.replace(tzinfo=pytz.timezone('US/Eastern')).astimezone(pytz.utc)
        self._tojdate()

    @classmethod
    def now(cls):
        ''' Return the current jdatetime '''
        n = datetime.utcnow().replace(tzinfo=pytz.utc)
        return cls(n.year, n.month, n.day, n.hour, n.minute, n.second, n.microsecond, n.tzinfo)

    today = now

    def _tojdate(self):
        ''' Aledgedly, this can calculate the correct Julian date. i am yet to be convinced '''
        if not self.gdate:
            return
        d = self.gdate
        year = d.year + 1900 if d.year < 1000 else d.year
        month = d.month
        day = d.day
        hour = d.hour
        min_ = d.minute
        sec = d.second
        univTime = hour + (min_ / 60.0) + (sec / 3600.0)
        sign = 1 if (100 * year + month - 190002.5) >= 0 else -1
        part1 = 367 * year
        part2 = math.floor((7.0 * (year + math.floor(month + 9) / 12.0)) / 4.0)
        part3 = day + math.floor((275 * month) / 9.0)
        part4 = 1721013.5 + (univTime / 24.0)
        part5 = 0.5 * sign
        jd = part1 - part2 + part3 + part4 - part5 + 1.5
        self.jdate = jd

    def _ordinal(self, number):
        if 10 <= number % 100 < 20:
            return 'th'
        return (['st', 'nd', 'rd'] + ['th'] * 7)[number % 10 - 1]

    @property
    def ordinal(self):
        return self._ordinal(self.day)

    @property
    def day(self):
        return int(math.floor(self.jdate) % 100)

    @property
    def dayname(self):
        return self.days[self.weekday]

    @property
    def month(self):
        return int(math.floor(self.jdate / 100) % 10)

    @property
    def monthname(self):
        return self.months[self.month]

    @property
    def week(self):
        return int(math.floor(self.jdate / 10) % 10)

    @property
    def weekday(self):
        return int(math.floor(self.jdate) % 10)

    @property
    def year(self):
        return int(math.floor(self.jdate / 1000) % 10000)

    @property
    def yearday(self):
        return int(math.floor(self.jdate) % 1000)

    @property
    def hour(self):
        return int(math.floor(self.jdate * 100.0) % 100)

    @property
    def minute(self):
        return int(math.floor(self.jdate * 10000.0) % 100)

    @property
    def second(self):
        return int(math.floor(self.jdate * 1000000.0) % 100)

    _fmt = {'A': 'dayname', 'w': 'weekday', 'd': '2day', 'm': '2month',
            'y': '2year', 'Y': 'year', 'H': '2hour', 'I': '2hour',
            'M': '2minute', 'S': '2second', 'j': 'yearday', 'U': '2week',
            'W': '2week', 'B': 'monthname', 'o': 'ordinal'}

    def __format__(self, fmt):
        def rep(match):
            pad = False
            g = match.groups()[0]
            if g in self._fmt:
                val = self._fmt[g]
                if val.startswith('2'):
                    pad = True
                    val = val[1:]
                tmp = getattr(self, val)
                if pad:
                    tmp = str(tmp % 100).rjust(2, '0')
                else:
                    tmp = str(tmp)
                return tmp
            return match.group()

        return re.sub(r'%([a-zA-Z]{1})', rep, fmt)
