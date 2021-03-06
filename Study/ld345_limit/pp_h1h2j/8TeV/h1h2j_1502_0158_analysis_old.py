import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.interpolate
import sys
import matplotlib.patches as mpatches
from scipy.interpolate import interp1d


#Read the data file and save it in the variables
Mh1a, ld345a, cs1 = np.genfromtxt ("cs_h1h2j_8TeV_DeltaM=1_old.dat",dtype=float,unpack=True,skip_header=True) 
Mh1b, ld345b, cs2 = np.genfromtxt ("cs_h1h2j_8TeV_DeltaM=100_old.dat",dtype=float,unpack=True,skip_header=True) 

Mh1,ld345,cs,best_SR,MC_Events,N_events,r,Acc,Lum,error_S,S_obs,S_exp,cs_lim  = np.genfromtxt ("CM_atlas_1502.01518_h1h2j_old.txt",dtype=float,unpack=True,skip_header=True) 

SIG_LIM = interp1d(Mh1, cs_lim, kind='linear')

SIG=SIG_LIM(Mh1a)

fig = plt.subplots()
plt.tick_params(axis='both',labelsize=18)
#Name of axes 
plt.xlabel("Mh$_1$ (GeV)", fontsize=25)
plt.ylabel("$\\sigma(pp\\rightarrow h_1h_2j)$ (fb) with $P_T^{jet} > 100$ GeV", fontsize=20)
plt.title('$\\sigma(pp\\rightarrow h_1h_2j)$ (fb) at 8 TeV', fontsize=25,y=1.02)
plt.xlim(10,200)
plt.ylim(0.1,10000)
plt.yscale('log')

plt.plot(Mh1a, cs1, linestyle='--',color='b',linewidth=2, label="$\\Delta M=1$ GeV")
plt.plot(Mh1b, cs2, linestyle='--',color='y',linewidth=2, label="$\\Delta M=100$ GeV")
plt.plot(Mh1a, SIG, linestyle='-',color='r',linewidth=2, label="95% CL $ ( 20.3 fb^{-1} )$")

plt.legend(loc="lower left", handlelength=2,borderaxespad=0.1,fancybox=True, shadow=True,fontsize = 17,labelspacing=0.2,handletextpad=0.1)

plt.grid()
plt.tight_layout()
plt.savefig('CM_limit_h1h2_8TeV_old.pdf')
plt.clf()



