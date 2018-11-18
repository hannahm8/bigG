
import numpy as np

def readInData(filename):
    data = np.genfromtxt(filename,names=True)
    experimentG = data['value'] 
    experimentSigma = data['sigma'] 
    return experimentG, experimentSigma


