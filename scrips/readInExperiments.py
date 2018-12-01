
import numpy as np
import sys

def readInData(filename):

    # try to read in and give an error if cannot 
    try:
        data = np.genfromtxt(filename,names=True)
    except IOError: 
        print("Error: file '{0}' could not be opened".format(filename))
        sys.exit(1)

    experimentG = data['value'] 
    experimentSigma = data['sigma'] 

    return experimentG, experimentSigma


