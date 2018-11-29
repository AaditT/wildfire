# https://stackoverflow.com/questions/19068862/how-to-overplot-a-line-on-a-scatter-plot-in-python
# playground to test different machine learning models

import numpy
from scipy import stats
import matplotlib as plt
import numpy as np

x_vals = [1,2,3,4,5,6,7,8,9,10]
y_vals = [2,4,5,7,9,12,14,16,18,22]

class linearRegression:

    # numpy; returns coefficient
    def _numpy_(x_vals,y_vals):
        return numpy.polyfit(x_vals, y_vals, 1)[0]

    # scipy; returns coefficient, intercept, rvalue, pvalue, stderr
    def _scipy_(x_vals,y_vals):
        return stats.linregress(x_vals, y_vals)
