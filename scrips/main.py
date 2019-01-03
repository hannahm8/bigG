import numpy as np
import matplotlib.pyplot as plt

import computePercentile
import pValue
import readInExperiments



def computePValues(Gs,sigmas,theoryGs):
    
  pVals = np.zeros(len(theoryGs))
  #fisherStat = np.zeros(len(theoryGs))


  for j, tG in enumerate(theoryGs):

    # get array of percentile values for each experiment given a theory value
    percentiles = computePercentile.getPercentile(tG,Gs,sigmas)


    # get the symmetric percentiles for each 
    symmPercentiles = [ computePercentile.symmPercentile(p) for p in percentiles ]
    #print min(symmPercentiles), max(symmPercentiles)

    # compute the overall p-value
    pVals[j] = pValue.getOverallPValue(symmPercentiles, 'chi2')



  return pVals#, fisherStat


# read in the data and return exp values and sigmas
expG, expGSigma = readInExperiments.readInData('../data/experimentValues.dat')
#expG, expGSigma = readInExperiments.readInData('../data/fakeValues.dat')


theoryGRange = np.arange(6.671, 6.677, 0.0000001)
#theoryGRange = np.arange(6.674, 6.677, 0.00001)
pValues,fisherStat = computePValues(expG,expGSigma,theoryGRange)



print 'pvalues as a fn of theory G: ', pValues

"""
plt.plot(theoryGRange,fisherStat,lw=2,color='r')
plt.ylabel('fisher stat')
plt.yscale('log')
#plt.ysc
plt.show()
"""



orange = "#E69F00"
green = "#009E73"

plt.clf()
fig, ax1 = plt.subplots()
# Make the y-axis label, ticks and tick labels match the line color.
ax1.set_ylabel('Chi2 Statistic', color=orange)
ax1.tick_params('y', colors=orange)

ax2 = ax1.twinx()
ax2.errorbar(expG,np.arange(len(expG),0,-1),xerr=expGSigma,fmt='o',color=green,alpha=0.5)
ax2.set_ylabel('Experiment number', color=green)
ax2.set_ylim(-1, 13)
ax2.set_yticks(np.arange(1,12,step=1))
ax2.tick_params('y', colors=green)

ax1.plot(theoryGRange, pValues, color=orange)
ax1.set_xlabel(r'$G / (10^{-11}\mathrm{kg}^{-1}\mathrm{m}^{3}\mathrm{s}^{-2})$')

fig.tight_layout()
#plt.savefig('chi2.pdf')
plt.show()











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

