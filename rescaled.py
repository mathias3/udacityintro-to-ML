# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 22:39:39 2016

@author: MO
"""

from   sklearn.preprocessing import MinMaxScaler
import numpy 
weights = numpy.array([[200000.],[1111258.], [477.]])
scaler = MinMaxScaler()
rescaled_weight = scaler.fit_transform(weights)
print  "this is rescaled rescaled salary "
print rescaled_weight


weights = numpy.array([[1000000.],[34348384.], [3285.]])
scaler = MinMaxScaler()
rescaled_weight = scaler.fit_transform(weights)
print  "this is rescaled rescaled stock option "
print rescaled_weight