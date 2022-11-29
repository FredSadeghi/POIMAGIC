# calculate a 5-number summary
from numpy import percentile
import numpy as np

def fiveNumSum(data):
    
    data = np.array(data)
    # generate data sample
    # calculate quartiles
    quartiles = percentile(data, [25, 50, 75])
    # calculate min/max
    data_min, data_max = data.min(), data.max()
    # print 5-number summary
    # print('Min: %.3f' % data_min)
    # print('Q1: %.3f' % quartiles[0])
    # print('Median: %.3f' % quartiles[1])
    # print('Q3: %.3f' % quartiles[2])
    # print('Max: %.3f' % data_max)
    
    return [data_min, quartiles[0], quartiles[1], quartiles[2], data_max]