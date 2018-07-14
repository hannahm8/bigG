import numpy as np

import symmPValue
import computePercentile
import pValue


def readInData(filename):
    data = np.genfromtxt(filename,names=True)
    experimentG = data['value'] 
    experimentSigma = data['sigma'] 
    return experimentG, experimentSigma


# read in data
expG, expGSigma = readInData('../data/experimentValues.dat')

theoryG = 6.674


percentiles = computePercentile.getPercentile(theoryG, expG, expGSigma)

print percentiles

symmPercentiles = np.zeros(len(expG))

for i,p in enumerate(percentiles):
    symmPercentiles[i] = computePercentile.symmPercentile(p)
    print expG[i],symmPercentiles[i]

print pValue.getOverallPValue(symmPercentiles,'chi2')
