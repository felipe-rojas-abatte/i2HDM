import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.interpolate
import sys
import matplotlib.patches as mpatches
from scipy.interpolate import interp1d

Bkg8TeV=0.01722   # Background CS at 8 TeV after cuts 
Bkg13TeV=0.06285  # Background CS at 13 TeV after cuts

#Read the data file and save it in the variables
Mh1_8, ld345_8, cs8 = np.genfromtxt ("cs_8TeV_ld345_limit_old.dat",dtype=float,unpack=True,skip_header=True) # Signal 8 TeV CS without cuts with ld345=maximum allowed
Mh1_13, ld345_13, cs13 = np.genfromtxt ("cs_13TeV_ld345_limit_old.dat",dtype=float,unpack=True,skip_header=True) # Signal 13 TeV CS without cuts with ld345=maximum allowed
Mh1a, ld345a, csa = np.genfromtxt ("cs_13TeV_ld345=0.1_old.dat",dtype=float,unpack=True,skip_header=True) # Signal 13 TeV CS without cuts with ld345=0.1
Mh1b, ld345b, csb = np.genfromtxt ("cs_13TeV_ld345=-0.01_old.dat",dtype=float,unpack=True,skip_header=True) # Signal 13 TeV CS without cuts with ld345=0.01

#atlas_1502_01518 Monojet analisis at 20 fb^(-1)    (BEST)

Mh1y,ld345y,csy,best_SRy,MC_Eventsy,N_eventsy,ry,Accy,Lumy,error_Sy,S_obs,S_expy,cs_limy  = np.genfromtxt ("CM_atlas_1502.01518_old.txt",dtype=float,unpack=True,skip_header=True) # limits on signal from CM at 8 TeV

mh1_8_cut,ld_8_cut,cs8TeV_cut=np.genfromtxt ("cs_8TeV_pp_h1h1j_new_cut.dat",dtype=float,unpack=True,skip_header=True) # Signal 8 TeV CS after cuts with ld345=maximum allowed
mh1_13_cut,ld_13_cut,cs13TeV_cut=np.genfromtxt ("cs_13TeV_pp_h1h1j_new_cut.dat",dtype=float,unpack=True,skip_header=True) # Signal 13 TeV CS after cuts with ld345=maximum allowed

SIG_LIM = interp1d(Mh1y, cs_limy, kind='linear') # limits from CM at 8 TeV
CS_8TEV_CUT_int = interp1d(mh1_8_cut, cs8TeV_cut, kind='linear') # Signal 8 TeV CS after cuts with ld345=maximum allowed
CS_13TEV_CUT_int = interp1d(mh1_13_cut, cs13TeV_cut, kind='linear') # Signal 13 TeV CS after cuts with ld345=maximum allowed

SIG = SIG_LIM(Mh1a) # limits from CM at 8 TeV
cs8_cut = CS_8TEV_CUT_int(Mh1a) # Signal 8 TeV CS after cuts with ld345=maximum allowed
cs13_cut = CS_13TEV_CUT_int(Mh1a) # Signal 13 TeV CS after cuts with ld345=maximum allowed

## Re-scale CheckMATE limits
lum_in = 20.3    # Initial luminosity

non_lum_scale=(Bkg13TeV/Bkg8TeV)**(0.5)*(cs8_cut/cs13_cut)*(cs13/cs8) # re-scaling due to change of signal and background. All signal cross sections are for ld345=maximum allowed

cs_R_20 = SIG*(lum_in/20)**(0.5)*non_lum_scale  # CheckMATE limits re-scaled as described in /Dropbox/DM-scalar/paper/Marc/extending_limits.pdf, Equation 5
cs_R_100 = SIG*(lum_in/100.0)**(0.5)*non_lum_scale  # CheckMATE limits re-scaled as described in /Dropbox/DM-scalar/paper/Marc/extending_limits.pdf, Equation 5
cs_R_3000 = SIG*(lum_in/3000.0)**(0.5)*non_lum_scale  # CheckMATE limits re-scaled as described in /Dropbox/DM-scalar/paper/Marc/extending_limits.pdf, Equation 5

## Plot of cross section vs Mh1 for 3 values of ld345 (0.1,-0.01,limit) with the Re-scaled CheckMATE limits at 13 TeV

fig = plt.subplots()
plt.tick_params(axis='both',labelsize=18)
#fig = plt.subplots(figsize=(6,4))
plt.xlabel("Mh$_1$ (GeV)", fontsize=25)
plt.ylabel("$\\sigma(pp\\rightarrow h_1h_1j)$ (fb) with $P_T^{jet} > 100$ GeV", fontsize=20)
plt.title('$\\sigma(pp\\rightarrow h_1h_1j)$ (fb) at 13 TeV', fontsize=25,y=1.02)
plt.xlim(10,200)
plt.ylim(0.0000001,4000)
plt.yscale('log')

plt.plot(Mh1a, csa, linestyle='--',color='b',linewidth=2, label="$\\lambda_{345}=0.1$")
plt.plot(Mh1b, csb, linestyle='--',color='y',linewidth=2, label="$\\lambda_{345}=-0.01$")
plt.plot(Mh1_13, cs13, linestyle='--',color='g',linewidth=2, label="$\\lambda_{345}=$maximum")
plt.plot(Mh1_13, cs_R_20, linestyle='-',color='r',linewidth=2, label="95% CL $ ( 20 fb^{-1} )$")
plt.plot(Mh1_13, cs_R_100, linestyle='-',color='m',linewidth=2, label="95% CL $ ( 100 fb^{-1} )$")
plt.plot(Mh1_13, cs_R_3000, linestyle='-',color='black',linewidth=2, label="95% CL $ ( 3000 fb^{-1} )$")
plt.legend(loc="lower left", handlelength=2,borderaxespad=0.1,fancybox=True, shadow=True,fontsize = 16,labelspacing=0.1,handletextpad=0.1)

plt.grid()
plt.tight_layout()
plt.savefig('Mh1_h1h1_limit_13TeV.pdf')

plt.clf()



