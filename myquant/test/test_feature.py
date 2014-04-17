from ..series.BarSeries import BarSeries
from ..feature.FeatureGenerator import FeatureGenerator

def main():
    bs = BarSeries.random(10)
    bs.print_readable()

    fg = FeatureGenerator()
    #print dir(fg)
    #fg.enable('close')
    #fg.enable('amp')
    #fg.config('sma', 'timeperiod', 2)
    #fg.config('macd', {'fastperiod':2, 'slowperiod':4, 'signalperiod':2})
    fg.config('rsi', 'timeperiod', [2, 4, 7])
    fg.print_config()

    feat = fg.generate(bs)
    for name, value in feat.iteritems():
        print name, value

if __name__ == '__main__':
    main()
