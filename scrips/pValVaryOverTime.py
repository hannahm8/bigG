import numpy as np
import matplotlib.pyplot as plt

import readInExperiments
import computePValuesAsFnTheoryG




def adjustFigAspect(fig,aspect=1):
    '''
    Adjust the subplot parameters so that the figure has the correct
    aspect ratio.
    '''
    xsize,ysize = fig.get_size_inches()
    minsize = min(xsize,ysize)
    xlim = .4*minsize/xsize
    ylim = .4*minsize/ysize
    if aspect < 1:
        xlim *= aspect
    else:
        ylim /= aspect
    fig.subplots_adjust(left=.5-xlim,
                        right=.5+xlim,
                        bottom=.5-ylim,
                        top=.5+ylim)



def main():

    dataFileName = str('../data/experimentValues.dat')
    expG,expGSigma = readInExperiments.readInData(dataFileName)
 
    noToInclude = np.arange(2,len(expG)+1,1)

    means = np.zeros(len(expG)-1)
    print(means)
    theoryGRange = np.arange(6.671, 6.676, 0.000001)#0.0000001)
    i=0


    fig = plt.figure()
    adjustFigAspect(fig,aspect=2.5)
    ax = fig.add_subplot(111)

    for noExps in (noToInclude): 
        experimentGs = expG[:noExps]
        experimentSigmas = expGSigma[:noExps] 
        means[i] = sum(experimentGs) / len(experimentGs)
        i+=1
        
        pValues = computePValuesAsFnTheoryG.computePValues(experimentGs,\
                                                           experimentSigmas,\
                                                           theoryGRange)
        ax.plot(pValues+(i*5)+2.5, theoryGRange)



    expNumberOne = np.arange(1,len(expG),1)
    expNumberZero = np.arange(0,len(expG),1)
    plt.plot(expNumberOne*5,means,alpha=0.7)
    ax.errorbar(expNumberZero*5, expG, yerr=expGSigma, fmt='o', lw=1)
    ax.set_ylim(6.671,6.676)
    #plt.tight_layout()
    #plt.show()


if __name__ == '__main__':
    main()
    










