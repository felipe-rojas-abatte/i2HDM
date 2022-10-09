import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import scipy.interpolate
import sys
import matplotlib.patches as mpatches
from scipy.interpolate import interp1d


#Read the data file and save it in the variables
#Cross sections files
Mh1a, cs1 = np.genfromtxt ("cs_8TeV_ld345=0.1_new.dat",dtype=float,unpack=True,skip_header=True) 
Mh1b, cs2 = np.genfromtxt ("cs_8TeV_ld345=-0.01_new.dat",dtype=float,unpack=True,skip_header=True) 
Mh1c, ld345c, cs3 = np.genfromtxt ("cs_8TeV_ld345_limit_new.dat",dtype=float,unpack=True,skip_header=True) 
#Mh1d, CMcs = np.genfromtxt ("CMcs_8TeV_pp_h1h1j.dat",dtype=float,unpack=True,skip_header=True) 


#CheckMATE analysis files
Mh1y,ld345y,csy,best_SRy,MC_Eventsy,N_eventsy,ry,Accy,Lumy,error_Sy,S_obs,S_expy,cs_limy  = np.genfromtxt ("CM_atlas_1502.01518_new.txt",dtype=float,unpack=True,skip_header=True)


#Interpolation of the CheckMATE analysis
SIG_LIM_1502_01518 = interp1d(Mh1y, cs_limy, kind='linear')
SIG3 = SIG_LIM_1502_01518(Mh1a) 

fig = plt.subplots()
plt.tick_params(axis='both',labelsize=18)
#Name of axes 
plt.xlabel("Mh$_1$ (GeV)", fontsize=25)
plt.ylabel("$\\sigma(pp\\rightarrow h_1h_1j)$ (fb) with $P_T^{jet} > 100$ GeV", fontsize=20)
plt.title('$\\sigma(pp\\rightarrow h_1h_1j)$ (fb) at 8 TeV', fontsize=25,y=1.02)
plt.xlim(10,200)
plt.ylim(0.0000001,4000)
plt.yscale('log')

plt.plot(Mh1a, cs1, linestyle='--',color='b',linewidth=2, label="$\\lambda_{345}=0.1$")
plt.plot(Mh1b, cs2, linestyle='--',color='y',linewidth=2, label="$\\lambda_{345}=-0.01$")
plt.plot(Mh1c, cs3, linestyle='--',color='g',linewidth=2, label="$\\lambda_{345}=$maximum")
plt.plot(Mh1a, SIG3, linestyle='-',color='r',linewidth=2, label="95% CL $ ( 20.3 fb^{-1} )$")

plt.text(60, 0.0000015, '',
         verticalalignment='top', horizontalalignment='center', color='black', fontsize=12,zorder=9)

plt.legend(loc="lower left", handlelength=2,borderaxespad=0.1,fancybox=True, shadow=True,fontsize = 17,labelspacing=0.1,handletextpad=0.1)

plt.grid()
plt.tight_layout()
plt.savefig('CM_limit_h1h1j_8TeV_new.pdf')
#plt.show()
plt.clf()



