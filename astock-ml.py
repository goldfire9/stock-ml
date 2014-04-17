#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from _log import logger
from myquant.datasource.DataSource import DataSource
from myquant.series.BarSeries import BarSeries
from myquant.tester.StrategyTester import StrategyTester
from myquant.strategy.LogisticStrategy import LogisticStrategy

def main(argv):
    #print argv
    infile = argv[0]
    bar = DataSource.load('csv', BarSeries, file_path=infile)
    logger.info('load %d bars from %s' % (bar.length(), infile))
    #print dir(bar)
    strategy = LogisticStrategy()
    #print dir(strategy)
    tester = StrategyTester.create('test')
    #print dir(tester)
    tester.run(strategy, bar)

if __name__ == '__main__':
    main(sys.argv[1:])
