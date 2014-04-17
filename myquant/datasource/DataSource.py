#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
from ..series.BarSeries import BarSeries

class DataSource:
	@classmethod
	def load(cls, src, data_type, **config):
		raw_data = []
		names = {}
		if src == 'csv':
			reader = csv.reader(open(config['file_path'], 'r'))
			for line in reader:
				raw_data.append(line)
			names = {'time': 0,
			         'open': 1,
			         'high': 2,
			         'low': 3,
			         'close': 4,
			         'volumn': 5}

		if data_type == BarSeries:
			columns = {}
			for name, index in names.iteritems():
				columns[name] = [ row[index] for row in raw_data ]
			data = BarSeries(columns['time'], columns['open'], columns['high'],
				             columns['low'], columns['close'], columns['volumn'])

		return data

