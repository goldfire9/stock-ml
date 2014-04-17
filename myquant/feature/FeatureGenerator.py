# -*- coding: utf-8 -*-

import sys
import copy
import numpy as np
import talib as ta
from myquant.series.BarSeries import BarSeries
from myquant._log import logger

class FeatureGenerator:

    def __gen_close(quotation, config):
        feat = {}
        length = quotation.length()
        close = quotation.get_close()
        win_len = config['window']
        for i in range(1, win_len + 1):
            name = 'close.' + str(i)
            if i > length:
                feat[name] = np.tile(np.nan, length)
                logger.warn('Window offset %d in feature %s is larger than length of input %d' %
                        (i, name, length))
            else:
                feat[name] = np.r_[np.tile(np.nan, i), close[:-i]]
        return feat

    def __gen_amp(quot, conf):
        feat = {}
        length = quot.length()
        amp = quot.get_high() - quot.get_low()
        win_len = conf['window']
        for i in range(1, win_len + 1):
            name = 'amp.' + str(i)
            if i > length:
                feat[name] = np.tile(np.nan, length)
                logger.warn('Window offset %d in feature %s is larger than length of input %d' %
                        (i, name, length))
            else:
                feat[name] = np.r_[np.tile(np.nan, i), amp[:-i]]
        return feat

    def __gen_sma(quot, conf):
        timeperiod = conf['timeperiod']
        price = quot.get(conf.get('price', 'close'))
        sma = ta.SMA(price, timeperiod)
        return {'sma': sma}

    def __gen_macd(quot, conf):
        fastperiod = conf.get('fastperiod', 12)
        slowperiod = conf.get('slowperiod', 26)
        signalperiod = conf.get('signalperiod', 9)
        price = quot.get(conf.get('price', 'close'))
        macd, macdsignal, macdhist = ta.MACD(price, fastperiod, slowperiod, signalperiod)
        return {'macd': macd, 'macdsignal': macdsignal, 'macdhist': macdhist}

    def __gen_rsi(quot, conf):
        timeperiod = conf['timeperiod']
        if not isinstance(timeperiod, (list, tuple)):
            timeperiod = [timeperiod]
        price = quot.get(conf.get('price', 'close'))
        rsi_dict = {}
        for p in timeperiod:
            name = 'rsi.%d' % p
            rsi = ta.SMA(price, p)
            rsi_dict[name] = rsi
        return rsi_dict

    __feature_func = {
        'close': __gen_close,
        'amp': __gen_amp,
        'sma': __gen_sma,
        'macd': __gen_macd,
        'rsi': __gen_rsi
    }

    __config_default = {
        'close': {
            'window': 5
        },
        'high': {
            'window': 5
        },
        'amp': {
            'window': 5
        },
        'sma': {
            'timeperiod': 5
        },
        'ema': {
            'alpha': 0.99,
            'timeperiod': 5
        },
        'macd': {
            'fastperiod': 12,
            'slowperiod': 26,
            'signalperiod': 9
        },
        'rsi': {
            'timeperiod': 14
        },
        'kdj': {

        },
        'bollinger': {

        }

    }
    __features_default = __config_default.keys()


    def __init__(self):
        self.__features = []
        self.__config = copy.deepcopy(FeatureGenerator.__config_default);

    def enable_all(self):
        self.__features = copy.deepcopy(FeatureGenerator.__features_default)

    def enable(self, feature_name):
        if feature_name in FeatureGenerator.__features_default:
            self.__features.append(feature_name)
        else:
            raise KeyError('No such feature: ' + feature_name)

    def config(self, feature, parameter, value=None):
        if isinstance(parameter, dict):
            self.__config[feature].update(parameter)
        elif isinstance(parameter, str):
            self.__config[feature][parameter] = value;
        else:
            raise TypeError('Illegal type of parameter: ' + repr(parameter))
        self.enable(feature)

    def print_config(self, out=sys.stdout, prefix='    '):
        '''print configuration of current feature generator'''

        prefix2 = prefix + '    '
        print >> out, '%sEnabled features: ' % prefix, self.__features
        for feature, config in self.__config.iteritems():
            print >> out, '%sIndicator %s' % (prefix, feature)
            for parameter, value in config.iteritems():
                print >> out, '%s%s = %s' % (prefix2, parameter, value)

    def generate(self, quotation):
        '''
        Generate features according to class of quotation data
        @Param quotation
        @Return header - feauture names
                features - value of features
        '''
        #if isinstance(quotation, BarSeries):
        #    return self.generate_from_bar_series(quotation)
        #else:
        #    raise TypeError('Unknown quotation type: ' + type(quotation))
        if not isinstance(quotation, BarSeries):
            raise TypeError('Unknown quotation type: ' + type(quotation))

        header = []
        features = {}

        self.__add_feature('time', {'time': quotation.get_time()}, header, features)
        for feat in self.__features:
            self.__add_feature(feat, self.__calc_feature(quotation, feat), header, features)
        #return features, header
        return features

    def __add_feature(self, name, values, header, features):
        for feat, value in values.iteritems():
            header.append(feat)
            features[feat] = value

    def __calc_feature(self, quotation, feature_name):
        return FeatureGenerator.__feature_func[feature_name](quotation, self.__config[feature_name])


