# -*- coding: utf-8 -*-

import numpy as np
import sklearn_view as sv
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.lda import LDA
from sklearn.qda import QDA
from myquant.feature.FeatureGenerator import FeatureGenerator

class LogisticStrategy:
    def __init__(self):
        feat_gen = FeatureGenerator()
        feat_gen.enable('close')
        feat_gen.enable('amp')
        pass

    def run(self, bars):
        nshuffle = 4

        #close = bars.get_close()
        #feature, target = self.__gen_dataset(close)
        #print feature, target
        feautre = feat_gen.generate(bars)
        rising = price[1:] - price[:-1]
        target = np.r_[np.tile(np.nan, 1), np.array(rising>0, dtype=np.int32)]

        datasets_ori = [(feature, target)]
        #datasets_expand, indicies = sv.expand_2d(datasets_ori)
        datasets_expand, indicies = datasets_ori, range(len(datasets_ori))
        #print datasets_expand
        datasets = sv.preprocess(datasets_expand, scale=True, max_samples=10000, nshuffle=nshuffle)
        #print datasets
        print len(datasets)
        clf = [
            LogisticRegression(),
            KNeighborsClassifier(3),
            SVC(kernel="linear", C=0.025),
            SVC(gamma=2, C=1),
            DecisionTreeClassifier(max_depth=5),
            RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),
            AdaBoostClassifier(),
            GaussianNB(),
            LDA(),
            QDA()]
        data_names = [ 'X' + str(i) + '#' + str(j) for i in indicies for j in range(nshuffle) ]
        clf_names = ['LR', 'KNN', 'LSVM', 'RBF', "Tree",
                     "RForest", "AdaBoost", "NB", "LDA", "QDA"]
        #sv.plot_classifiers(datasets, clf, data_names=data_names, clf_names=clf_names)
        sv.plot_classifiers_roc(datasets, clf, data_names=data_names, clf_names=clf_names)

    def __gen_dataset(self, price):
        rising = price[1:] - price[:-1]
        #feature = np.c_[price[0:-3], price[1:-2], price[2:-1]]
        #target = np.array(price[3:] - price[2:-1] > 0, dtype=np.int32)
        feature = np.c_[rising[0:-4], rising[1:-3], rising[2:-2], rising[3:-1]]
        target = np.array(rising[4:]>0, dtype=np.int32)
        return feature, target

