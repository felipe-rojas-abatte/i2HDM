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



# Added by Marc Thomas (22/09/2016) 
# get_up_low_sig_bound() is used by get_sig_at_95CL() to get an upper and
# lower bound on the signal value with CL = 0.95
def get_up_low_sig_bound(NumObserved, ExpectedBG, BGError, NumToyExperiments):
    # set starting values for variables
    start_val=1.0
    sig=start_val
    upper_bound=0.0
    lower_bound=sig
    CL=0.0

    # increase lower_bound until CL > 0.95, and set upper_bound to the first
    # value of signal with CL > 0.95
    while (CL < 0.95):
        lower_bound=upper_bound
        upper_bound=sig
        CL=CLs(NumObserved, ExpectedBG, BGError, sig, NumToyExperiments)
        sig = sig*10
    return lower_bound, upper_bound


# Added by Marc Thomas (22/09/2016)
# get_sig_at_95CL() loops to find the value signal value that gives CL ~ 0.95
# Accuracy can be increased mainly by altering the value NumToyExperiments
# (and also by altering the values in "while CL < 0.949 or CL > 0.951")
def get_sig_at_95CL(NumObserved, ExpectedBG, BGError, NumToyExperiments):

    # get starting lower/upper values of signal which have CLs below/above 0.95
    lower_bound_sig,upper_bound_sig=get_up_low_sig_bound(NumObserved, ExpectedBG, BGError, NumToyExperiments)
    sig=lower_bound_sig
    CL=0.0

    # loop to find CL in range around 0.95
    while CL < 0.949 or CL > 0.951:
        CL=CLs(NumObserved, ExpectedBG, BGError, sig, NumToyExperiments)
        
        # if CL < 0.95, increase lower bound to current signal value
        # if CL < 0.95, decrease lower bound to current signal value
        # put new signal value half way between new upper and lower bounds
        if CL < 0.95:
            lower_bound_sig=sig
            sig= (lower_bound_sig + upper_bound_sig)/2.0
        elif CL > 0.95:
            upper_bound_sig=sig
            sig= (lower_bound_sig + upper_bound_sig)/2.0
        else:
            # print error if CL not < 0.95 or > 0.95
            print "ERROR!"

        # comment/uncomment line below to watch convergence
        #print "sig =",sig, " CL =", CL 

    #print "BG=",NumObserved,"   ", "SIG =", sig
    return  sig

# example of use of
# get_sig_at_95CL(NumObserved, ExpectedBG, BGError, NumToyExperiments):

CSBG=100
CSSIG=50
LUMI=10

while LUMI < 1000:
	LUMI=LUMI+10
	BG=CSBG*LUMI
	print get_sig_at_95CL(BG,BG,max(0.01*BG,math.sqrt(BG)),10000)/(CSSIG*LUMI)




