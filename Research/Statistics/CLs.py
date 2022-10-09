numtoyexperiments = 1000000

import os, sys, math
try:
    from lxml import ET
except:
    import xml.etree.ElementTree as ET
import scipy.stats

def CLs(NumObserved, ExpectedBG, BGError, SigHypothesis, NumToyExperiments):
    # generate a set of expected-number-of-background-events, one for each toy
    # experiment, distributed according to a Gaussian with the specified mean
    # and uncertainty
    ExpectedBGs = scipy.stats.norm.rvs(loc=ExpectedBG, \
    scale=BGError, size=NumToyExperiments)

    # Ignore values in the tail of the Gaussian extending to negative numbers
    ExpectedBGs = [value for value in ExpectedBGs if value > 0]

    # For each toy experiment, get the actual number of background events by
    # taking one value from a Poisson distribution created using the expected
    # number of events.
    ToyBGs = scipy.stats.poisson.rvs(ExpectedBGs)
    ToyBGs = map(float, ToyBGs)

    # The probability for the background alone to fluctutate as LOW as
    # observed = the fraction of the toy experiments with backgrounds as low as
    # observed = p_b.
    # NB (1 - this p_b) corresponds to what is usually called p_b for CLs.
    p_b = scipy.stats.percentileofscore(ToyBGs, NumObserved, kind='weak')*.01

    # Toy MC for background+signal
    ExpectedBGandS = [expectedbg + SigHypothesis for expectedbg in ExpectedBGs]
    ToyBplusS = scipy.stats.poisson.rvs(ExpectedBGandS)
    ToyBplusS = map(float, ToyBplusS)

    # Calculate the fraction of these that are >= the number observed,
    # giving p_(S+B). Divide by (1 - p_b) a la the CLs prescription.
    p_SplusB = scipy.stats.percentileofscore(ToyBplusS, NumObserved, kind='weak')*.01
    
    return 1.-(p_SplusB / p_b) # 1 - CLs
  
# def CLs(NumObserved, ExpectedBG, BGError, SigHypothesis, NumToyExperiments):  
print 'expected CLs'
print 'SR10', CLs(  36200,  36200,   362,  620, 100000)
print 'SR12', CLs(  8300,   8300,    83,   200,  100000)
