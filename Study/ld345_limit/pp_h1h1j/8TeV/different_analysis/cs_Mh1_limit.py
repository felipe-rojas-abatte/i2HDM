import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.interpolate
import sys
import matplotlib.patches as mpatches
from scipy.interpolate import interp1d


#Read the data file and save it in the variables
Mh1a, ld345a, cs1 = np.genfromtxt ("cs_8TeV_ld345=0.1.dat",dtype=float,unpack=True,skip_header=True) 
Mh1b, ld345b, cs2 = np.genfromtxt ("cs_8TeV_ld345=-0.01.dat",dtype=float,unpack=True,skip_header=True) 
Mh1c, ld345c, cs3 = np.genfromtxt ("cs_8TeV_ld345_limit.dat",dtype=float,unpack=True,skip_header=True) 
#Mh1d, CMcs = np.genfromtxt ("CMcs_8TeV_pp_h1h1j.dat",dtype=float,unpack=True,skip_header=True) 

Mh1,ld345,cs,best_SR,MC_Events,N_events,r,Acc,Lum,error_S,S_exp,cs_lim  = np.genfromtxt ("CH_MATE_8TeV_pp_h1h1j.dat",dtype=float,unpack=True,skip_header=True) 

SIG_LIM = interp1d(Mh1, cs_lim, kind='linear')

SIG=SIG_LIM(Mh1a)

fig = plt.subplots()
#Name of axes 
plt.xlabel("Mh$_1$ (GeV)", fontsize=15)
plt.ylabel("$\\sigma(pp\\rightarrow h_1h_1j)$ (fb)", fontsize=20)
plt.xlim(10,200)
plt.yscale('log')

plt.plot(Mh1a, cs1, linestyle='--',color='b',linewidth=2, label="$\\lambda_{345}=0.1$")
plt.plot(Mh1b, cs2, linestyle='--',color='y',linewidth=2, label="$\\lambda_{345}=-0.01$")
plt.plot(Mh1c, cs3, linestyle='--',color='g',linewidth=2, label="$\\lambda_{345}=$limit")
plt.plot(Mh1a, SIG, linestyle='-',color='r',linewidth=2, label="CheckMATE $\\sigma$ limit")
plt.legend(loc="lower left", borderaxespad=0.1,fancybox=True, shadow=True)

plt.text(150, 100, '$M_{h1}=M_{h2}$, $\\sqrt{s}=8$ TeV, \n $\\mathscr{L}=10 (fb^{-1})$',
        verticalalignment='top', horizontalalignment='center', color='black', fontsize=15)

plt.grid()
plt.savefig('Mh1_ld345_limit.pdf')
plt.show()
plt.clf()



