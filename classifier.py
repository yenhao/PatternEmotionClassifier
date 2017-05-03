import pandas as pd
import numpy as np
import sklearn.metrics

from sklearn import preprocessing
from sklearn.externals import joblib

#import PatternVectorizer and SimpleClassifier
from pattern_classifier import  SimpleClassifier, PatternVectorizer


if __name__ == '__main__':
    
    cls = joblib.load(cls_persistence)
    pv = joblib.load(pv_persistence)

    