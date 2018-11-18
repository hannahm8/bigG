import numpy as np

import computePercentile
import pValue


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
