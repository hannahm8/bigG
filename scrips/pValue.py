import numpy as np 
from scipy.stats import kstest,chi2,norm


# from Walter's code
def pValue(confidence_levels, statistics = "chi2"):
    if statistics is None:
        print("no test statistics specified. choose between ks or chi2")
        exit()
    elif statistics=="ks":
        """
        The KS statistics is relevant for the 
        actual confidence regions
        """
        return kstest(confidence_levels,'uniform')[1]
    elif statistics=="chi2":
        """
        The Fisher method chi2 statistics acts
        on the p-values, defined as 1-CL
        """
        #print confidence_levels
        #print np.log(confidence_levels)
        
        #compute the fisher combined statistic 
        p = -2.*np.sum(np.log(confidence_levels))
        #print p
        
        # find out if this is chi-squared distributed with 2*NExp degrees of freedom using the survival function. 
        #print "sf: ", chi2.sf(p,2.*len(confidence_levels))
        return chi2.sf(p,2.*len(confidence_levels))



def getOverallPValue(pValueData,chooseStat):
    pValueData = np.atleast_1d(pValueData)
    overallPValue = pValue(pValueData, statistics = chooseStat) 
    return overallPValue
