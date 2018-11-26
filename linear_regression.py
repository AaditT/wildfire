# https://stackoverflow.com/questions/19068862/how-to-overplot-a-line-on-a-scatter-plot-in-python
# playground to test different machine learning models

import numpy

x_vals = [1,2,3,4,5,6,7,8,9,10]
y_vals = [2,4,5,7,9,12,14,16,18,22]

def getC(x_vals,y_vals):
    coefficient = numpy.polyfit(x_vals, y_vals, 1)[0]
    return coefficient
