#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import sys

class BarSeries:
    def __init__(self, time, open, high, low, close, volumn,
                 amount=None):
        length = len(time)
        for s in (open, high, low, close, volumn):
            if len(s) != length:
                raise ValueError('lists size doesnot match')
        self.__time = np.array(time)
        self.__open = np.array(open, dtype=np.float_)
        self.__high = np.array(high, dtype=np.float_)
        self.__low = np.array(low, dtype=np.float_)
        self.__close = np.array(close, dtype=np.float_)
        self.__volumn = np.array(volumn, dtype=np.float_)
        if amount is not None and len(amount) == length:
            self.__amount = np.array(amount, dtype=np.float_)
        else:
            self.__amount = None
        self.__data_dict = {'time': self.__time,
                'open': self.__open,
                'high': self.__high,
                'low': self.__low,
                'close': self.__close,
                'volumn': self.__volumn,
                'amount': self.__amount }

    def length(self):
        return len(self.__time)

    def get(self, field):
        return self.__data_dict.get(field, None)

    def get_time(self):
        return self.__time

    def get_open(self):
        return self.__open

    def get_high(self):
        return self.__high

    def get_low(self):
        return self.__low

    def get_close(self):
        return self.__close

    def get_volumn(self):
        return self.__volumn

    def print_readable(self, out=sys.stdout, prefix=''):
        print >> out, 'time: ', self.__time
        print >> out, 'open: ', self.__open
        print >> out, 'high: ', self.__high
        print >> out, 'low: ', self.__low
        print >> out, 'close: ', self.__close
        print >> out, 'volumn: ', self.__volumn
        print >> out, 'amount: ', self.__amount

    @classmethod
    def random(cls, length=8, amp=100):
        return BarSeries(range(0, length),
                         np.random.random(length) * amp,
                         np.random.random(length) * amp,
                         np.random.random(length) * amp,
                         np.random.random(length) * amp,
                         np.random.random(length) * amp,
                         np.random.random(length) * amp)

