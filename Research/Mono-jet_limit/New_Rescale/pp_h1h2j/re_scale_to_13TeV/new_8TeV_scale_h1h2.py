import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.interpolate
import sys
import matplotlib.patches as mpatches
from scipy.interpolate import interp1d

#Read the data file and save it in the variables
Mh1_8_1, cs8_1 = np.genfromtxt ("cs_8TeV_pp_h1h2j_DeltaM=1_new.dat",dtype=float,unpack=True,skip_header=True) 
Mh1_8_100, cs8_100 = np.genfromtxt ("cs_8TeV_pp_h1h2j_DeltaM=100_new.dat",dtype=float,unpack=True,skip_header=True) 

Mh1_8TeV, lim_8TeV = np.genfromtxt ("brief_limit_calculated_8tev.txt",dtype=float,unpack=True,skip_header=True) 

lim_8TeV = 1000*lim_8TeV

cs_8TeV_int = interp1d(Mh1_8TeV, lim_8TeV, kind='linear')
cs_8TeV=cs_8TeV_int(Mh1_8_1)

fig = plt.subplots()
plt.tick_params(axis='both',labelsize=18)
plt.xlabel("Mh$_1$ (GeV)", fontsize=25)
plt.ylabel("$\\sigma(pp\\rightarrow h_1h_2j)$ (fb) with $P_T^{jet} > 100$ GeV", fontsize=20)
plt.title('$\\sigma(pp\\rightarrow h_1h_2j)$ (fb) at 8 TeV', fontsize=25,y=1.02)
plt.xlim(10,200)
plt.ylim(0.1,10000)
plt.yscale('log')

plt.plot(Mh1_8_1, cs8_1, linestyle='--',color='b',linewidth=2, label="$\\Delta M=1$ GeV")
plt.plot(Mh1_8_100, cs8_100, linestyle='--',color='y',linewidth=2, label="$\\Delta M=100$ GeV")
print Mh1_8_1
print cs_8TeV
plt.plot(Mh1_8_1, cs_8TeV, linestyle='-',color='r',linewidth=2, label="95% CL $ ( 20.3 fb^{-1} )$")

plt.legend(loc="lower left", handlelength=2,borderaxespad=0.1,fancybox=True, shadow=True,fontsize = 17,labelspacing=0.2,handletextpad=0.1)

plt.grid()
plt.tight_layout()
plt.savefig('new_Mh1_Mh2_h1h2_8TeV_new.pdf')
plt.clf()


