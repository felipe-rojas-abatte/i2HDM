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
import math
###################################################

####################################################
			
pi=np.pi
DMMEV=np.array([140+i for i in range(101)])
DM=DMMEV/1000.

fpi=0.130
v=242.17
mpi=0.13957

GAM=fpi**2/(4*v**4)*DM**2*(DM**2-mpi**2)**(0.5)/pi


#----------------------------------------------------------------------------------------------
#params = {'legend.fontsize': 8, 'legend.linewidth': 2,'lines.linewidth':2, 'legend.fontsize': 6}
params = {'legend.fontsize': 8,'lines.linewidth':2, 'legend.fontsize': 6}
plt.rcParams.update(params)
	
fig, ax = plt.subplots(figsize=(5,3.8))
plt.subplots_adjust(bottom=0.20,right=0.85,left=0.15)

plt.text (150,3E-15, '$h^+ \\to  h_1\\pi^+ $', fontsize=14)


plt.xlabel("$\\Delta M= M_{h^+}-M_{h_1}$ (MeV)",fontsize=14)
plt.ylabel("$\\Gamma$ (GeV)",fontsize=16)
#plt.title('$pp\ \\to$ DM DM jet  @ 8 TeV' )
plt.xlim(130,200)
plt.ylim(5E-017,5E-15)
plt.yscale('log') 
plt.xscale('linear') 

####################################################
plt.plot(DMMEV ,  GAM, label='$h^+ \\to  h_1\\pi^+ $',    alpha=0.7, color=(0.5,0.1,0.1))
#plt.legend(loc=1,bbox_to_anchor=[1.00, 1.0],handlelength=3.,fontsize=11)
plt.savefig('gamma.pdf')


#----------------------------------------------------------------------------------------------
#params = {'legend.fontsize': 8, 'legend.linewidth': 2,'lines.linewidth':2, 'legend.fontsize': 6}
params = {'legend.fontsize': 8,'lines.linewidth':2, 'legend.fontsize': 6}
plt.rcParams.update(params)
	
fig, ax = plt.subplots(figsize=(5,3.8))
plt.subplots_adjust(bottom=0.20,right=0.85,left=0.15)

tau=(6.582*10**(-16))/GAM

#plt.title('$pp\ \\to$ DM DM jet  @ 8 TeV' )
plt.xlim(130,200)
plt.yscale('log') 
plt.xlabel("$\\Delta M= M_{h^+}-M_{h_1}$ (MeV)",fontsize=14)
plt.xscale('linear') 
plt.text (150,10, '$h^+ \\to  h_1\\pi^+ $', fontsize=14)


###################################################
plt.ylabel("$\\tau$ (ns)",fontsize=16, color=(0.7,0.1,0.1))
plt.ylim(0.1,30)
ln1=plt.plot(DMMEV,  tau, label='$\\tau$',    alpha=0.7, color=(0.7,0.1,0.1))



ax2 = ax.twinx()
ctau=(1.9746*10**(-14))/GAM
plt.ylim(1,300)
plt.yscale('log') 
ln2=ax2.plot(DMMEV,  ctau, 'r',	alpha=0.7, color=(0.1,0.1,0.7), label='$c\\tau$' )
plt.ylabel("$c\\tau$ (cm)",fontsize=16, color=(0.1,0.1,0.7))


lns = ln1+ln2
labs = [l.get_label() for l in lns]
ax.legend(lns, labs, loc=1,handlelength=3.,fontsize=11)


plt.savefig('lifetime.pdf')



quit()

