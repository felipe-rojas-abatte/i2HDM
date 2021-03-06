import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.interpolate
import sys
import matplotlib.patches as mpatches
from scipy.interpolate import interp1d


#Read the data file and save it in the variables
#Cross sections files
Mh1a, ld345a, cs1 = np.genfromtxt ("cs_8TeV_ld345_limit_old.dat",dtype=float,unpack=True,skip_header=True) 
Mh1b, ld345b, cs2 = np.genfromtxt ("cs_8TeV_ld345_limit_new.dat",dtype=float,unpack=True,skip_header=True) 

#CheckMATE analysis files
Mh1x,ld345x,csx,best_SRx,MC_Eventsx,N_eventsx,rx,Accx,Lumx,error_Sx,S_obsx,S_expx,cs_limx  = np.genfromtxt ("CH_MATE_atlas_1502.01518_old.txt",dtype=float,unpack=True,skip_header=True) 

Mh1y,ld345y,csy,best_SRy,MC_Eventsy,N_eventsy,ry,Accy,Lumy,error_Sy,S_obsy,S_expy,cs_limy  = np.genfromtxt ("CH_MATE_atlas_1502.01518_new.txt",dtype=float,unpack=True,skip_header=True) 

#Interpolation of the CheckMATE analysis
SIG_LIM_1502_01518 = interp1d(Mh1x, cs_limx, kind='linear')
SIG_OLD = SIG_LIM_1502_01518(Mh1a) 


fig,ax = plt.subplots()
plt.tick_params(axis='both',labelsize=18)
#Name of axes 
plt.xlabel("Mh$_1$ (GeV)", fontsize=25)
plt.ylabel("$\\sigma(pp\\rightarrow h_1h_1j)$ (fb) with $P_T^{jet} > 100$ GeV", fontsize=20)
plt.title('$\\sigma(pp\\rightarrow h_1h_1j)$ (fb) at 8 TeV', fontsize=25,y=1.02)
plt.xlim(10,200)
plt.ylim(0.01,10000)
plt.yscale('log')

plt.plot(Mh1a, cs1, linestyle='-',color='r',linewidth=2, label="$\\lambda_{345}=$max old")
plt.plot(Mh1b, cs2, linestyle='--',color='b',linewidth=2, label="$\\lambda_{345}=$max new")
plt.plot(Mh1a, SIG_OLD, linestyle='-',color='r',linewidth=2, label="95% CL $ ( 20.3 fb^{-1})$ old")
cax = ax.scatter(Mh1y,cs_limy, c='b', s=30, edgecolor='', rasterized=True, label="95% CL $ (20.3 fb^{-1})$ new")

plt.text(60, 0.0000015, '', verticalalignment='top', horizontalalignment='center', color='black', fontsize=12,zorder=9)

plt.legend(loc="lower left", handlelength=2,borderaxespad=0.1,fancybox=True, shadow=True,fontsize = 17,labelspacing=0.1,handletextpad=0.1)

plt.grid()
plt.tight_layout()
plt.savefig('Mh1_h1h1_ld345max_8TeV.pdf')
plt.show()
plt.clf()



