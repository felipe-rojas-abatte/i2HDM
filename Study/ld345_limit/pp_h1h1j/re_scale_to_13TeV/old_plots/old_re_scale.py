import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.interpolate
import sys
import matplotlib.patches as mpatches
from scipy.interpolate import interp1d

#Read the data file and save it in the variables
Mh1_8, ld345_8, cs8 = np.genfromtxt ("cs_8TeV_ld345_limit.dat",dtype=float,unpack=True,skip_header=True) 
Mh1_13, ld345_13, cs13 = np.genfromtxt ("cs_13TeV_ld345_limit.dat",dtype=float,unpack=True,skip_header=True) 
Mh1a, ld345a, csa = np.genfromtxt ("cs_13TeV_ld345=0.1.dat",dtype=float,unpack=True,skip_header=True) 
Mh1b, ld345b, csb = np.genfromtxt ("cs_13TeV_ld345=-0.01.dat",dtype=float,unpack=True,skip_header=True) 

#atlas_conf_2012_147 Monojet + missing energy analisis at 10 fb^(-1)
#atlas_1407_0608 Monojet + missing energy analisis at 20 fb^(-1)
#atlas_1502_01518 Monojet analisis at 20 fb^(-1)    (BEST)
#cms_1408_3583 Monojet + missing energy analysis at 19.5 fb^(-1)

Mh1y,ld345y,csy,best_SRy,MC_Eventsy,N_eventsy,ry,Accy,Lumy,error_Sy,S_expy,cs_limy  = np.genfromtxt ("CH_MATE_ATLAS_1502.01518.txt",dtype=float,unpack=True,skip_header=True) 

SIG_LIM = interp1d(Mh1y, cs_limy, kind='linear')
SIG = SIG_LIM(Mh1a) 

## Re-scale CheckMATE limits
lum_in = 20    # Inicial luminosity
lum_end = 3000  # Final luminosity
lum_ends = '3000'  #string
lum = lum_end/lum_in  
CS_frac = cs13/cs8
f = 1/(lum*CS_frac)**(1/2)
cs_R = SIG*f  # CheckMATE limits re-scaled

## Plot of cross section vs Mh1 for 3 values of ld345 (0.1,-0.01,limit) with the Re-scaled CheckMATE limits at 13 TeV

fig = plt.subplots()
plt.xlabel("Mh$_1$ (GeV)", fontsize=15)
plt.ylabel("$\\sigma(pp\\rightarrow h_1h_1j)$ (fb) with $P_{Tjet}>100$ (GeV)", fontsize=15)
plt.title('Cross Section Limit at parton level \n for monojet + Missing Energy Analysis', fontsize=15)
plt.xlim(10,200)
plt.yscale('log')

plt.plot(Mh1a, csa, linestyle='--',color='b',linewidth=2, label="$\\lambda_{345}=0.1$")
plt.plot(Mh1b, csb, linestyle='--',color='y',linewidth=2, label="$\\lambda_{345}=-0.01$")
plt.plot(Mh1_13, cs13, linestyle='--',color='g',linewidth=2, label="$\\lambda_{345}=$limit")
plt.plot(Mh1_13, cs_R, linestyle='-',color='r',linewidth=2, label="CM ATLAS_1502.01518 $\\sigma_{lim}$")
plt.legend(loc="lower left", borderaxespad=0.1,fancybox=True, shadow=True,fontsize = 'medium')

plt.text(150, 0.8, '$M_{h1}=M_{h2}$, $\\sqrt{s}=13$ TeV, \n $\\mathscr{L}='+lum_ends+' (fb^{-1})$',
        verticalalignment='top', horizontalalignment='center', color='black', fontsize=15)

plt.grid()
plt.savefig('Mh1_ld345_limit_L='+lum_ends+'.pdf')

plt.clf()



