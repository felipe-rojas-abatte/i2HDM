import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.interpolate
import sys
import matplotlib.patches as mpatches
from scipy.interpolate import interp1d


#Read the data file and save it in the variables
Mh1a, ld345a, cs8_new = np.genfromtxt ("cs_8TeV_ld345_limit_new.dat",dtype=float,unpack=True,skip_header=True) 
Mh1b, ld345b, cs8_old = np.genfromtxt ("cs_8TeV_ld345_limit_old.dat",dtype=float,unpack=True,skip_header=True) 
Mh1c, ld345c, cs13_new = np.genfromtxt ("cs_13TeV_ld345_limit_new.dat",dtype=float,unpack=True,skip_header=True) 
Mh1d, ld345d, cs13_old = np.genfromtxt ("cs_13TeV_ld345_limit_old.dat",dtype=float,unpack=True,skip_header=True) 

fig = plt.subplots()
#Name of axes 
plt.xlabel("Mh$_1$ (GeV)", fontsize=15)
plt.ylabel("$\\sigma(pp\\rightarrow h_1h_1j)$ (fb)", fontsize=20)
plt.xlim(10,200)
plt.ylim(0.1,10000)
plt.yscale('log')

plt.plot(Mh1a, cs8_new, linestyle='--',color='b',linewidth=2, label="$\\lambda_{345}^{max}$ new - 8 TeV")
plt.plot(Mh1b, cs8_old, linestyle='-',color='b',linewidth=2, label="$\\lambda_{345}^{max}$ old - 8 TeV")
plt.plot(Mh1c, cs13_new, linestyle='--',color='r',linewidth=2, label="$\\lambda_{345}^{max}$ new - 13 TeV")
plt.plot(Mh1d, cs13_old, linestyle='-',color='r',linewidth=2, label="$\\lambda_{345}^{max}$ old - 13 TeV")
plt.legend(loc="upper right", borderaxespad=0.1,fancybox=True, shadow=True)

#plt.text(150, 100, '$M_{h1}=M_{h2}$, $\\sqrt{s}=8$ TeV, \n $\\mathscr{L}=10 (fb^{-1})$',
 #       verticalalignment='top', horizontalalignment='center', color='black', fontsize=15)

plt.grid()
plt.savefig('Mh1_ld345_limit.pdf')
plt.show()
plt.clf()



