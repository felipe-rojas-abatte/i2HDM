import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.interpolate
import sys
import matplotlib.patches as mpatches
from scipy.interpolate import interp1d


#Read the data file and save it in the variables
#Cross sections files
Mh1a, Mh2a, cs1 = np.genfromtxt ("cs_8TeV_pp_h1h2j_DeltaM=1.dat",dtype=float,unpack=True,skip_header=True) 
Mh1b, Mh2b, cs2 = np.genfromtxt ("cs_8TeV_pp_h1h2j_DeltaM=100.dat",dtype=float,unpack=True,skip_header=True) 

#CheckMATE analysis files
Mh1w,ld345w,csw,best_SRw,MC_Eventsw,N_eventsw,rw,Accw,Lumw,error_Sw,S_obsw,S_expw,cs_limw  = np.genfromtxt ("CH_MATE_atlas_2012_147_h1h2j.txt",dtype=float,unpack=True,skip_header=True)

Mh1x,ld345x,csx,best_SRx,MC_Eventsx,N_eventsx,rx,Accx,Lumx,error_Sx,S_obsx,S_expx,cs_limx  = np.genfromtxt ("CH_MATE_atlas_1407_0608_h1h2j.txt",dtype=float,unpack=True,skip_header=True) 

Mh1y,ld345y,csy,best_SRy,MC_Eventsy,N_eventsy,ry,Accy,Lumy,error_Sy,S_obsy,S_expy,cs_limy  = np.genfromtxt ("CH_MATE_atlas_1502.01518_h1h2j.txt",dtype=float,unpack=True,skip_header=True) 

Mh1z,ld345z,csz,best_SRz,MC_Eventsz,N_eventsz,rz,Accz,Lumz,error_Sz,S_obsz,S_expz,cs_limz  = np.genfromtxt ("CH_MATE_cms_1408_3583_h1h2j.txt",dtype=float,unpack=True,skip_header=True) 

#Interpolation of the CheckMATE analysis
SIG_LIM_2012_147 = interp1d(Mh1w, cs_limw, kind='linear')
SIG1=SIG_LIM_2012_147(Mh1a)

SIG_LIM_1407_0608 = interp1d(Mh1x, cs_limx, kind='linear')
SIG2 = SIG_LIM_1407_0608(Mh1a) 

SIG_LIM_1502_01518 = interp1d(Mh1y, cs_limy, kind='linear')
SIG3 = SIG_LIM_1502_01518(Mh1a) 

SIG_LIM_1408_3583 = interp1d(Mh1z, cs_limz, kind='linear')
SIG4 = SIG_LIM_1408_3583(Mh1a) 

fig = plt.subplots()
#Name of axes 
plt.xlabel("Mh$_1$ (GeV)", fontsize=15)
plt.ylabel("$\\sigma(pp\\rightarrow h_1h_2j)$ (fb) with $P_{Tjet}>100$ (GeV)", fontsize=15)
plt.title('Cross Section Limit at parton level \n for monojet + Missing Energy Analysis', fontsize=15)
plt.xlim(10,200)
plt.yscale('log')

plt.plot(Mh1a, cs1, linestyle='--',color='b',linewidth=2, label="$\\Delta M=1$ GeV")
plt.plot(Mh1b, cs2, linestyle='--',color='y',linewidth=2, label="$\\Delta M=100$ GeV")
plt.plot(Mh1a, SIG1, linestyle='-',color='r',linewidth=2, label="CM ATLAS_2012_147 $\\sigma_{lim}$ at $\\mathscr{L}=10 (fb^{-1})$")
plt.plot(Mh1a, SIG2, linestyle='-',color='b',linewidth=2, label="CM ATLAS_1407_0608 $\\sigma_{lim}$ at $\\mathscr{L}=20 (fb^{-1})$")
plt.plot(Mh1a, SIG3, linestyle='-',color='g',linewidth=2, label="CM ATLAS_1502_01518 $\\sigma_{lim}$ at $\\mathscr{L}=20 (fb^{-1})$")
plt.plot(Mh1a, SIG4, linestyle='-',color='y',linewidth=2, label="CM cms_1408_3583 $\\sigma_{lim}$ at $\\mathscr{L}=19.7 (fb^{-1})$")


plt.legend(loc="lower left", borderaxespad=0.1,fancybox=True, shadow=True,fontsize = 'small')


plt.text(150, 100, '$\\sqrt{s}=8$ TeV',
        verticalalignment='top', horizontalalignment='center', color='black', fontsize=15)

plt.grid()
plt.savefig('h1h2j_lim_different_analysis.pdf')
plt.show()
plt.clf()



