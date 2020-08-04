import numpy as np
import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['text.latex.unicode'] = True
import matplotlib.pyplot as plt
from matplotlib.legend import Legend
#Legend.update_default_handler_map({AnyObject: AnyObjectHandler()})
from array import array

import scipy.interpolate
from scipy.interpolate import interp1d
import sys
import matplotlib.patches as mpatches
import matplotlib.ticker as ticker
from matplotlib.ticker import ScalarFormatter
###################################################

####################################################
			
M,x1,sigma,x2,x3,x4,x5=np.genfromtxt("sigma_h+-mh1.out",dtype=float,unpack=True, comments='#',skip_header=2)
M02,om02=np.genfromtxt("coann_0.2.dat",dtype=float,unpack=True, comments='#',skip_header=1)
M14,om14=np.genfromtxt("coann_0.14.dat",dtype=float,unpack=True, comments='#',skip_header=1)

#M,x1,sigma,x2,x3,x4,x5=np.genfromtxt("test.out",dtype=float,unpack=True, comments='#',skip_header=2)

sigma=sigma*1000.

#----------------------------------------------------------------------------------------------
#params = {'legend.fontsize': 8, 'legend.linewidth': 2,'lines.linewidth':2, 'legend.fontsize': 6}
params = {'legend.fontsize': 8,'lines.linewidth':2, 'legend.fontsize': 6}
plt.rcParams.update(params)
	
fig, ax = plt.subplots(figsize=(4.,3.))
plt.subplots_adjust(bottom=0.18,right=0.8,left=0.18,top=0.8)



plt.xlabel("$M_{h^+}$ (GeV)",fontsize=16)
plt.ylabel("$\\sigma$ (fb)",fontsize=16, color=(0.5,0.1,0.1))

#plt.title( )
plt.xlim(400,600)
plt.ylim(0.1,1.5)
plt.yscale('linear') 
plt.xscale('linear') 

ln1=plt.plot(M, sigma,    alpha=0.7, color=(0.5,0.1,0.1),label='$pp\ \\to h^+h^- + h^\\pm h_{1,2}$  @ 8 TeV')
#plt.plot(M, sigmaM, label='$1/M_T$',    alpha=0.7, color=(0.1,0.1,0.1))

ax2 = ax.twinx()
plt.ylim(0.06,0.15)
ln2=ax2.plot(M02,om02, 'r',	alpha=0.7, color=(0.1,0.1,0.7), label='$\\Omega h^2$' )
plt.ylabel("$\\Omega h^2$ ",fontsize=16, color=(0.1,0.1,0.7))

lns = ln1+ln2
labs = [l.get_label() for l in lns]
ax.legend(lns, labs, loc=1,bbox_to_anchor=[1.1, 1.35],handlelength=3.,fontsize=11)

plt.plot([400,600],[0.118,0.118], color=(0.1,0.1,0.7), linewidth=0.6, ls='-')
plt.plot([400,600],[0.118*0.8,0.118*0.8], color=(0.1,0.1,0.7), linewidth=0.6, ls='--')
plt.plot([400,600],[0.118*1.2,0.118*1.2], color=(0.1,0.1,0.7), linewidth=0.6, ls='--')

plt.savefig('sigma_h+.pdf')








