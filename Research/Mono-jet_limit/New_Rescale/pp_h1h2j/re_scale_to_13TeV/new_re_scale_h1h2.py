import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.interpolate
import sys
import matplotlib.patches as mpatches
from scipy.interpolate import interp1d

#Read the data file and save it in the variables
Mh1_13_1, cs13_1 = np.genfromtxt ("cs_13TeV_pp_h1h2j_DeltaM=1_new.dat",dtype=float,unpack=True,skip_header=True) 
Mh1_13_100, cs13_100 = np.genfromtxt ("cs_13TeV_pp_h1h2j_DeltaM=100_new.dat",dtype=float,unpack=True,skip_header=True) 

#Mh1_13TeV_lum20_1, lim_13TeV_lum20_1 = np.genfromtxt ("brief_limit_new_results_20_h1h2_gap1.txt",dtype=float,unpack=True,skip_header=True) 
#Mh1_13TeV_lum100_1, lim_13TeV_lum100_1 = np.genfromtxt ("brief_limit_new_results_100_h1h2_gap1.txt",dtype=float,unpack=True,skip_header=True) 
#Mh1_13TeV_lum3000_1, lim_13TeV_lum3000_1 = np.genfromtxt ("brief_limit_new_results_3000_h1h2_gap1.txt",dtype=float,unpack=True,skip_header=True) 

Mh1_13TeV_lum20_1, lim_13TeV_lum20_1 = np.genfromtxt ("brief_limit_calculated_20.txt",dtype=float,unpack=True,skip_header=True) 
Mh1_13TeV_lum100_1, lim_13TeV_lum100_1 = np.genfromtxt ("brief_limit_calculated_100.txt",dtype=float,unpack=True,skip_header=True) 
Mh1_13TeV_lum3000_1, lim_13TeV_lum3000_1 = np.genfromtxt ("brief_limit_calculated_3000.txt",dtype=float,unpack=True,skip_header=True) 
lim_13TeV_lum20_1 = 1000*lim_13TeV_lum20_1 
lim_13TeV_lum100_1 = 1000*lim_13TeV_lum100_1 
lim_13TeV_lum3000_1 = 1000*lim_13TeV_lum3000_1 
#brief_limit_calculated_3_2.txt

Mh1_13TeV_lum20_100, lim_13TeV_lum20_100 = np.genfromtxt ("brief_limit_new_results_20_h1h2_gap100.txt",dtype=float,unpack=True,skip_header=True) 
Mh1_13TeV_lum100_100, lim_13TeV_lum100_100 = np.genfromtxt ("brief_limit_new_results_100_h1h2_gap100.txt",dtype=float,unpack=True,skip_header=True) 
Mh1_13TeV_lum3000_100, lim_13TeV_lum3000_100 = np.genfromtxt ("brief_limit_new_results_3000_h1h2_gap100.txt",dtype=float,unpack=True,skip_header=True) 

cs_13TeV_lum20_1_int = interp1d(Mh1_13TeV_lum20_1, lim_13TeV_lum20_1, kind='linear')
cs_13TeV_lum100_1_int = interp1d(Mh1_13TeV_lum100_1, lim_13TeV_lum100_1, kind='linear')
cs_13TeV_lum3000_1_int = interp1d(Mh1_13TeV_lum3000_1, lim_13TeV_lum3000_1, kind='linear')

cs_13TeV_lum20_100_int = interp1d(Mh1_13TeV_lum20_100, lim_13TeV_lum20_100, kind='linear')
cs_13TeV_lum100_100_int = interp1d(Mh1_13TeV_lum100_100, lim_13TeV_lum100_100, kind='linear')
cs_13TeV_lum3000_100_int = interp1d(Mh1_13TeV_lum3000_100, lim_13TeV_lum3000_100, kind='linear')

cs_13TeV_lum20_1=(Mh1_13_1)

fig = plt.subplots()
plt.tick_params(axis='both',labelsize=18)
plt.xlabel("Mh$_1$ (GeV)", fontsize=25)
plt.ylabel("$\\sigma(pp\\rightarrow h_1h_2j)$ (fb) with $P_T^{jet} > 100$ GeV", fontsize=20)
plt.title('$\\sigma(pp\\rightarrow h_1h_2j)$ (fb) at 13 TeV', fontsize=25,y=1.02)
plt.xlim(10,200)
plt.ylim(0.1,10000)
plt.yscale('log')

plt.plot(Mh1_13_1, cs13_1, linestyle='--',color='b',linewidth=2, label="$\\Delta M=1$ GeV")
plt.plot(Mh1_13_100, cs13_100, linestyle='--',color='y',linewidth=2, label="$\\Delta M=100$ GeV")

plt.plot(Mh1_13_1, cs_13TeV_lum20_1_int(Mh1_13_1), linestyle='-',color='r',linewidth=2, label="95% CL $ ( 20 fb^{-1} )$")
plt.plot(Mh1_13_1, cs_13TeV_lum100_1_int(Mh1_13_1), linestyle='--',color='r',linewidth=2, label="95% CL $ ( 100 fb^{-1} )$")
plt.plot(Mh1_13_1, cs_13TeV_lum3000_1_int(Mh1_13_1), linestyle=':',color='r',linewidth=2, label="95% CL $ ( 3000 fb^{-1} )$")

# plt.plot(Mh1_13_1, cs_13TeV_lum20_100_int(Mh1_13_1), linestyle='-',color='g',linewidth=2, label="95% CL $ ( 20 fb^{-1} )$")
# plt.plot(Mh1_13_1, cs_13TeV_lum100_100_int(Mh1_13_1), linestyle='--',color='g',linewidth=2, label="95% CL $ ( 100 fb^{-1} )$")
# plt.plot(Mh1_13_1, cs_13TeV_lum3000_100_int(Mh1_13_1), linestyle=':',color='g',linewidth=2, label="95% CL $ ( 3000 fb^{-1} )$")


plt.legend(loc="lower left", handlelength=2,borderaxespad=0.1,fancybox=True, shadow=True,fontsize = 17,labelspacing=0.2,handletextpad=0.1)

plt.grid()
plt.tight_layout()
plt.savefig('new_Mh1_Mh2_h1h2_13TeV_new.pdf')
plt.clf()



