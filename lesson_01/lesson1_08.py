import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas_use
import scipy.optimize as spo

def f(X):
    Y=(X-1.5)**2+0.5
    print("X={}, Y={}".format(X,Y))
    return Y

def optimizer():
    Xguess = 2.0
    min_result =spo.minimize(f, Xguess, method = 'SLSQp')
    print("Minima found at:")
    print("X={}, Y={}".format(min_result.x,min_result.fun))