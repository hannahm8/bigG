import numpy as np
import matplotlib.pyplot as plt

import computePercentile
import pValue
import readInExperiments



def computePValues(Gs,sigmas,theoryGs):
    
  pVals = np.zeros(len(theoryGs))

  for j, tG in enumerate(theoryGs):

    # get array of percentile values for each experiment given a theory value
    percentiles = computePercentile.getPercentile(tG,Gs,sigmas)


    # get the symmetric percentiles for each 
    symmPercentiles = [ computePercentile.symmPercentile(p) for p in percentiles ]

    # compute the overall p-value
    pVals[j] = pValue.getOverallPValue(symmPercentiles,'chi2')

  return pVals


# read in the data and return exp values and sigmas
expG, expGSigma = readInExperiments.readInData('../data/experimentValues.dat')



theoryGRange = np.arange(6.672, 6.675, 0.0000001)
pValues = computePValues(expG,expGSigma,theoryGRange)


print 'pvalues as a fn of theory G: ', pValues

plt.plot(theoryGRange,pValues,lw=2,color='r')
#plt.ysc
#plt.show()















"""
exit()
# below is old versions of the same code - I have put things into functions above now




theoryG = 6.673

percentiles = computePercentile.getPercentile(theoryG, expG, expGSigma)










print percentiles

symmPercentiles = np.zeros(len(expG))

for i,p in enumerate(percentiles):
    symmPercentiles[i] = computePercentile.symmPercentile(p)
    print expG[i],symmPercentiles[i]

print pValue.getOverallPValue(symmPercentiles,'chi2')


theoryGRange = np.arange(6.672, 6.675, 0.0000001)
pVals = np.zeros(len(theoryGRange))
print theoryGRange
for j,tG in enumerate(theoryGRange):
    percentiles = computePercentile.getPercentile(tG, expG, expGSigma)

    symmPercentiles = np.zeros(len(expG))

    for i,p in enumerate(percentiles):
        symmPercentiles[i] = computePercentile.symmPercentile(p)
    
    pVals[j] = pValue.getOverallPValue(symmPercentiles,'chi2')

import matplotlib.pyplot as plt

#plt.clf()
plt.plot(theoryGRange, pVals)
plt.yscale('log')
plt.show()"""

