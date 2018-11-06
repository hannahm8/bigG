import numpy as np
from scipy.special import erf


#return integral from -inf to experimental G
def getPercentile(theoryG, experimentalG, sigmaExperimentalG):

    # change intgration variable
    T = ( theoryG - experimentalG ) / ( np.sqrt(2.) * sigmaExperimentalG )

    # integral value
    integral = 0.5 + erf(T) / 2.

    return integral



# returns the summetric p value from the integration value
def symmPercentile(value):
    return (2.*(min(value,1.-value)))



#print getPercentile(.13, 0.4, 0.9)
