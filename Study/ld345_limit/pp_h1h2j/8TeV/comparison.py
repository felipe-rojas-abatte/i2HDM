import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.interpolate
import sys
import matplotlib.patches as mpatches
from scipy.interpolate import interp1d


#Read the data file and save it in the variables
Mh1a_old, Mh2a_old, cs1_old = np.genfromtxt ("cs_h1h2j_8TeV_DeltaM=1_old.dat",dtype=float,unpack=True,skip_header=True) 
Mh1b_old, Mh2b_old, cs2_old = np.genfromtxt ("cs_h1h2j_8TeV_DeltaM=100_old.dat",dtype=float,unpack=True,skip_header=True) 

Mh1a_new, cs1_new = np.genfromtxt ("cs_h1h2j_8TeV_DeltaM=1_new.dat",dtype=float,unpack=True,skip_header=True) 
Mh1b_new, cs2_new = np.genfromtxt ("cs_h1h2j_8TeV_DeltaM=100_new.dat",dtype=float,unpack=True,skip_header=True) 

Mh1_old, ld345_old, cs_old, best_SR_old, MC_Events_old, N_events_old, r_old, Acc_old, Lum_old, error_S_old, S_obs_old, S_exp_old, cs_lim_old  = np.genfromtxt ("CM_atlas_1502.01518_h1h2j_old.txt",dtype=float,unpack=True,skip_header=True) 

Mh1_new, ld345_new, cs_new, best_SR_new, MC_Events_new, N_events_new, r_new, Acc_new, Lum_new, error_S_new, S_obs_new, S_exp_new, cs_lim_new  = np.genfromtxt ("CM_atlas_1502.01518_h1h2j_new.txt",dtype=float,unpack=True,skip_header=True) 

SIG_LIM_1502_01518_old = interp1d(Mh1_old, cs_lim_old, kind='linear')
SIG_old=SIG_LIM_1502_01518_old(Mh1a_old)

SIG_LIM_1502_01518_new = interp1d(Mh1_new, cs_lim_new, kind='linear')
SIG_new=SIG_LIM_1502_01518_new(Mh1a_new)

fig = plt.subplots()
plt.tick_params(axis='both',labelsize=18)
#Name of axes 
plt.xlabel("Mh$_1$ (GeV)", fontsize=25)
plt.ylabel("$\\sigma(pp\\rightarrow h_1h_2j)$ (fb) with $P_T^{jet} > 100$ GeV", fontsize=20)
plt.title('$\\sigma(pp\\rightarrow h_1h_2j)$ (fb) at 8 TeV', fontsize=25,y=1.02)
plt.xlim(10,200)
plt.ylim(0.1,10000)
plt.yscale('log')

plt.plot(Mh1a_old, cs1_old, linestyle='--',color='b',linewidth=2, label="$\\Delta M=1$ GeV old")
plt.plot(Mh1a_new, cs1_new, linestyle='-.',color='b',linewidth=2, label="$\\Delta M=1$ GeV new")

plt.plot(Mh1b_old, cs2_old, linestyle='--',color='y',linewidth=2, label="$\\Delta M=100$ GeV old")
plt.plot(Mh1b_new, cs2_new, linestyle='-.',color='y',linewidth=2, label="$\\Delta M=100$ GeV new")

plt.plot(Mh1a_old, SIG_old, linestyle='-',color='r',linewidth=2, label="95% CL $ ( 20.3 fb^{-1} )$ old")
plt.plot(Mh1a_new, SIG_new, linestyle='-.',color='r',linewidth=2, label="95% CL $ ( 20.3 fb^{-1} )$ new")


plt.legend(loc="lower left", handlelength=2,borderaxespad=0.1,fancybox=True, shadow=True,fontsize = 13,labelspacing=0.2,handletextpad=0.1)

plt.grid()
plt.tight_layout()
plt.savefig('comparison.pdf')
plt.clf()



