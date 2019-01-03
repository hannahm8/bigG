import numpy as np 
from scipy.stats import kstest,chi2,norm
import matplotlib.pyplot as plt

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

        
        #compute the fisher combined statistic 
        p = -2.*np.sum(np.log(confidence_levels))



        
        # find out if this is chi-squared distributed with 2*NExp degrees of freedom using the survival function. 
        #print "sf: ", chi2.sf(p,2.*len(confidence_levels))
        sfValue = chi2.sf(p,2.*len(confidence_levels)) 
        
        """
        print "the confidence levels are: \n", confidence_levels
        print "this gives a global pvalue of ", p
        print "the survival function for this is ", sfValue
        x = np.arange(0.0, 50, 0.01)
        plt.plot(x, chi2.sf(x,2*len(confidence_levels)))
        plt.axvline(p)
        plt.show()
        """
        return sfValue



def getOverallPValue(pValueData,chooseStat):
    pValueData = np.atleast_1d(pValueData)
    overallPValue = pValue(pValueData, statistics = chooseStat) 
    return overallPValue
