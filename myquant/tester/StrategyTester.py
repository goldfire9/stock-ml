# -*- coding: utf-8 -*-

class StrategyTester:
	def __init__(self, name):
		self.__name = name

	def run(self, strategy, quote):
		try:
			strategy.run(quote)
		except:
			raise

	@classmethod
	def create(cls, name):
		return StrategyTester(name)
