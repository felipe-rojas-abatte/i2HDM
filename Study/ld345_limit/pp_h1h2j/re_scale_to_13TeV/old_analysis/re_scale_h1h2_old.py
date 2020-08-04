import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.interpolate
import sys
import matplotlib.patches as mpatches
from scipy.interpolate import interp1d

Bkg8TeV_400=0.01722
Bkg13TeV_400=0.06285
Bkg8TeV_300=0.08471
Bkg13TeV_300=0.2642
Bkg8TeV_200=0.5079
Bkg13TeV_200=1.337

#Read the data file and save it in the variables
Mh1_8_1, ld345_8_1, cs8_1 = np.genfromtxt ("cs_8TeV_pp_h1h2j_DeltaM=1_old.dat",dtype=float,unpack=True,skip_header=True) 
Mh1_8_100, ld345_8_100, cs8_100 = np.genfromtxt ("cs_8TeV_pp_h1h2j_DeltaM=100_old.dat",dtype=float,unpack=True,skip_header=True) 
Mh1_13_1, ld345_13_1, cs13_1 = np.genfromtxt ("cs_13TeV_pp_h1h2j_DeltaM=1_old.dat",dtype=float,unpack=True,skip_header=True) 
Mh1_13_100, ld345_13_100, cs13_100 = np.genfromtxt ("cs_13TeV_pp_h1h2j_DeltaM=100_old.dat",dtype=float,unpack=True,skip_header=True) 

Mh1,ld345,cs,best_SR,MC_Events,N_events,r,Acc,Lum,error_S,S_obs,S_exp,cs_lim  = np.genfromtxt ("CM_atlas_1502.01518_h1h2j_old.txt",dtype=float,unpack=True,skip_header=True) 

mh1_8_cut,ld_8_cut,cs8TeV_cut=np.genfromtxt ("cs_8TeV_pp_h1h2j_new_cut.dat",dtype=float,unpack=True,skip_header=True) 
mh1_13_cut,ld_13_cut,cs13TeV_cut=np.genfromtxt ("cs_13TeV_pp_h1h2j_new_cut.dat",dtype=float,unpack=True,skip_header=True) 

SIG_LIM = interp1d(Mh1, cs_lim, kind='linear')
CS_8TEV_CUT_int = interp1d(mh1_8_cut, cs8TeV_cut, kind='linear')
CS_13TEV_CUT_int = interp1d(mh1_13_cut, cs13TeV_cut, kind='linear')

####  The 8 vs 13 TeV background depends on the signal cuts ####
####  The best signal cut depends on Mh1, therefore  we ########
####  interpolate the background cross section rations for #####
####  differenc Mh1  ###########################################
####  This part depends on the SR is CH_MATE_atlas_1502.01518_h1h2j.txt ####
mh1_bkg=[0,29,67,105,124,200]
bkg_8TeV=[Bkg8TeV_200,Bkg8TeV_200,Bkg8TeV_300,Bkg8TeV_300,Bkg8TeV_400,Bkg8TeV_400]
bkg_13TeV=[Bkg13TeV_200,Bkg13TeV_200,Bkg13TeV_300,Bkg13TeV_300,Bkg13TeV_400,Bkg13TeV_400]
BKG_RATIO_F = interp1d(mh1_bkg, (np.asarray(bkg_13TeV)/np.asarray(bkg_8TeV)), kind='linear')
###################################################################

SIG = SIG_LIM(Mh1_8_1) 
cs8_cut = CS_8TEV_CUT_int(Mh1_8_1)
cs13_cut = CS_13TEV_CUT_int(Mh1_8_1)
bkg_ratio = BKG_RATIO_F(Mh1_8_1)

## Re-scale CheckMATE limits
lum_in = 20.3    # Inicial luminosity

############# Ideally needs to be different limit projections between DeltaM=1 and DeltaM=100. #########
############ Check: If close enough (they probably are) then can use just 1 new limit ###############
non_lum_scale=bkg_ratio**(0.5)*(cs8_cut/cs13_cut)*(cs13_1/cs8_1)
print CS_8TEV_CUT_int(48)/CS_13TEV_CUT_int(48)
############# Ideally needs to be different limit projections between DeltaM=1 and DeltaM=100. #########
############ Check: If close enough (they probably are) then can use just 1 new limit ###############

cs_R_20 = SIG*(lum_in/20)**(0.5)*non_lum_scale  # CheckMATE limits re-scaled
cs_R_100 = SIG*(lum_in/100.0)**(0.5)*non_lum_scale  # CheckMATE limits re-scaled
cs_R_3000 = SIG*(lum_in/3000.0)**(0.5)*non_lum_scale  # CheckMATE limits re-scaled

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
plt.plot(Mh1_13_1, cs_R_20, linestyle='-',color='r',linewidth=2, label="95% CL $ ( 20 fb^{-1} )$")
plt.plot(Mh1_13_1, cs_R_100, linestyle='-',color='m',linewidth=2, label="95% CL $ ( 100 fb^{-1} )$")
plt.plot(Mh1_13_1, cs_R_3000, linestyle='-',color='black',linewidth=2, label="95% CL $ ( 3000 fb^{-1} )$")
plt.legend(loc="lower left", handlelength=2,borderaxespad=0.1,fancybox=True, shadow=True,fontsize = 17,labelspacing=0.2,handletextpad=0.1)

plt.grid()
plt.tight_layout()
plt.savefig('Mh1_ld345_h1h2_13TeV.pdf')
plt.clf()



