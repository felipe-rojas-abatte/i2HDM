import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import scipy.interpolate
from scipy.interpolate import interp1d
import sys
import matplotlib.patches as mpatches
import matplotlib.ticker as ticker
from matplotlib.ticker import ScalarFormatter


#Read the data file and save it in the variables

(MDM,SIG)=np.genfromtxt("LUX.dat",dtype=float,unpack=True,skip_header=False) 
LUX_SIG=interp1d(MDM, SIG, kind='linear')

Mh, lim_inf, omega, lim_sup = np.genfromtxt("limit.dat", dtype=float, unpack=True, skip_header=True)

#Read data for positives values of ld345
Mh1a, Mh2a, Mhca, ld345a ,lda, Omegaa, prota, Brh1a, Brh2a, Brhca, WHa, HBa, HSa, Ra, vstaba, LEPa, Sa, Ta  = np.genfromtxt("data/ld345=1.mh1=mhall+100.dat",dtype=float,unpack=True,skip_header=True) 
Mh1d, Mh2d, Mhcd, ld345d ,ldd, Omegad, protd, Brh1d, Brh2d, Brhcd, WHd, HBd, HSd, Rd, vstabd, LEPd, Sd, Td  = np.genfromtxt("data/ld345=0.1.mh1=mhall+100.dat",dtype=float,unpack=True,skip_header=True) 
Mh1e, Mh2e, Mhce, ld345e ,lde, Omegae, prote, Brh1e, Brh2e, Brhce, WHe, HBe, HSe, Re, vstabe, LEPe, Se, Te  = np.genfromtxt("data/ld345=0.01.mh1=mhall+100.dat",dtype=float,unpack=True,skip_header=True) 
Mh1f, Mh2f, Mhcf, ld345f ,ldf, Omegaf, protf, Brh1f, Brh2f, Brhcf, WHf, HBf, HSf, Rf, vstabf, LEPf, Sf, Tf  = np.genfromtxt("data/ld345=0.001.mh1=mhall+100.dat",dtype=float,unpack=True,skip_header=True) 

#Read data for negatives values of ld345
Mh1g, Mh2g, Mhcg, ld345g ,ldg, Omegag, protg, Brh1g, Brh2g, Brhcg, WHg, HBg, HSg, Rg, vstabg, LEPg, Sg, Tg  = np.genfromtxt("data/ld345=-1.mh1=mhall+100.dat",dtype=float,unpack=True,skip_header=True) 
Mh1j, Mh2j, Mhcj, ld345j ,ldj, Omegaj, protj, Brh1j, Brh2j, Brhcj, WHj, HBj, HSj, Rj, vstabj, LEPj, Sj, Tj  = np.genfromtxt("data/ld345=-0.1.mh1=mhall+100.dat",dtype=float,unpack=True,skip_header=True) 
Mh1k, Mh2k, Mhck, ld345k ,ldk, Omegak, protk, Brh1k, Brh2k, Brhck, WHk, HBk, HSk, Rk, vstabk, LEPk, Sk, Tk  = np.genfromtxt("data/ld345=-0.01.mh1=mhall+100.dat",dtype=float,unpack=True,skip_header=True) 
Mh1l, Mh2l, Mhcl, ld345l ,ldl, Omegal, protl, Brh1l, Brh2l, Brhcl, WHl, HBl, HSl, Rl, vstabl, LEPl, Sl, Tl  = np.genfromtxt("data/ld345=-0.001.mh1=mhall+100.dat",dtype=float,unpack=True,skip_header=True) 

LUX=LUX_SIG(Mh1a)

## Re-scale the Direct Detection cross section Sigma_SI

re_sca = 1

prot_a = ((Omegaa/0.112)*prota)/re_sca
prot_d = ((Omegad/0.112)*protd)/re_sca
prot_e = ((Omegae/0.112)*prote)/re_sca
prot_f = ((Omegaf/0.112)*protf)/re_sca

prot_g = ((Omegag/0.112)*protg)/re_sca
prot_j = ((Omegaj/0.112)*protj)/re_sca
prot_k = ((Omegak/0.112)*protk)/re_sca
prot_l = ((Omegal/0.112)*protl)/re_sca

N_LUX = LUX/re_sca


#----------------------------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(6.3,5.3))
plt.subplots_adjust(bottom=0.15,right=0.95)
ax.fill_between(Mh1a, N_LUX, 1000 ,facecolor='palegreen', interpolate=True, alpha=0.5)

ax.text(0.33, 0.85, 'Excluded by LUX 100 with 85.3 live-days', verticalalignment='top', horizontalalignment='left',
        transform=ax.transAxes, color='green', fontsize=12)

#ax.fill_between([10,45], [1E-5,1E-5], 1E-15 ,facecolor=[(1,0.6,0.6)], alpha=0.5)
#ax.text(0.05, 0.5, 'Excluded by LEP', verticalalignment='top', horizontalalignment='left',
#        transform=ax.transAxes, color='red', fontsize=12)

plt.xlabel("$M_{h1}$ (GeV)",fontsize=15)
plt.ylabel("$\\hat{\\sigma}_{SI}$ (pb)",fontsize=15)
plt.title('$M_{h2}=M_{h^\pm}=M_{h1}$+100 GeV' )
plt.xlim(10,1000)
plt.ylim(1E-15,1E-5)
plt.yscale('log') 
plt.xscale('log') 

plt.plot(Mh1a, prot_a, label='$\lambda_{345}=1.0$',color='b')
plt.plot(Mh1d, prot_d, label='$\lambda_{345}=0.1$',color='m')
plt.plot(Mh1e, prot_e, label='$\lambda_{345}=0.01$',color='y')
plt.plot(Mh1f, prot_f, label='$\lambda_{345}=0.001$',color='k')
plt.plot(Mh1g, prot_g, label='$\lambda_{345}=-1.0$',color='b',linestyle='--')
plt.plot(Mh1j, prot_j, label='$\lambda_{345}=-0.1$',color='m',linestyle='--')
plt.plot(Mh1k, prot_k, label='$\lambda_{345}=-0.01$',color='y',linestyle='--')
plt.plot(Mh1l, prot_l, label='$\lambda_{345}=-0.001$',color='k',linestyle='--')

plt.plot(Mh1a, N_LUX, label='LUX',color='green',linewidth=2)

plt.legend(loc="lower left", borderaxespad=0.1,prop={'size':11})
plt.savefig('DD_LUX_limit_mh+100_new.pdf')

#----------------------------------------------------------------------------------------------
## Planck limits for Relic Density vs Mh1 for ld_345>0
plt.subplots(figsize=(6,4.5))
plt.subplots_adjust(bottom=0.15,right=0.95)
#Name of axes
plt.xlabel("Mh$_1$ (GeV)",fontsize=15)
plt.ylabel("Relic Density $\\Omega h^2$",fontsize=15)
plt.title('$M_{h2}=M_{h^\pm}=M_{h1}$+100 GeV')
plt.yscale('log')  #Escala logaritmica para el eje y
plt.xscale('log')  #Escala logaritmica para el eje x
plt.xlim(10,1000)
plt.ylim(1E-06,100)


plt.plot(Mh1a, Omegaa, label='$\lambda_{345}=1.0$',color='b')
plt.plot(Mh1d, Omegad, label='$\lambda_{345}=0.1$',color='m')
plt.plot(Mh1e, Omegae, label='$\lambda_{345}=0.01$',color='y')
plt.plot(Mh1f, Omegaf, label='$\lambda_{345}=0.001$',color='k')
plt.plot(Mh1g, Omegag, label='$\lambda_{345}=-1.0$',color='b',linestyle='--')
plt.plot(Mh1j, Omegaj, label='$\lambda_{345}=-0.1$',color='m',linestyle='--')
plt.plot(Mh1k, Omegak, label='$\lambda_{345}=-0.01$',color='y',linestyle='--')
plt.plot(Mh1l, Omegal, label='$\lambda_{345}=-0.001$',color='k',linestyle='--')

plt.plot(Mh, lim_inf,linestyle='--',color='red')
plt.plot(Mh, omega,color='red')
plt.plot(Mh, lim_sup,linestyle='--',color='red')

#plt.legend(loc="lower right", borderaxespad=0.1)
plt.legend(loc="upper right", ncol=2, borderaxespad=0.1,prop={'size':11},bbox_to_anchor=(1.05, 1.0))
plt.savefig('Omega_Mh1_mh+100_new.pdf')

#----------------------------------------------------------------------------------------------
## LUX limits on Direct Detection cross section Sigma_SI vs Mh1 for lambda_345   
fig3, ax = plt.subplots()
ax.fill_between(Mh1a, LUX, 0.001 ,facecolor='palegreen', interpolate=True)
ax.text(0.45, 0.95, 'LUX 85.3 live-days',
        verticalalignment='top', horizontalalignment='center',
        transform=ax.transAxes,
        color='green', fontsize=15)

#nombre de los ejes y del grafico
plt.xlabel("Dark Matter mass $M_{h1}$ (GeV)",fontsize=15)
plt.ylabel("Direct Detection $\\sigma_{SI}$ (pb)",fontsize=15)
plt.title("LUX limit for Direct Detection $\\sigma_{SI}$ vs $M_{h1}$")
plt.xlim(10,1000)
plt.ylim(0.000000000000001,0.001)
plt.yscale('log')  #Escala logaritmica para el eje y

plt.plot(Mh1a, prota,label='$|\lambda_{345}|=1.0$',linestyle='--',color='b')
plt.plot(Mh1d, protd, label='$|\lambda_{345}|=0.1$',linestyle='--',color='m')
plt.plot(Mh1e, prote, label='$|\lambda_{345}|=0.01$',linestyle='--',color='y')
plt.plot(Mh1f, protf, label='$|\lambda_{345}|=0.001$',linestyle='--',color='k')

plt.plot(Mh1a, LUX, label='LUX',color='green',linewidth=2)

plt.legend(loc="upper right", borderaxespad=0.1,prop={'size':11},bbox_to_anchor=(1.05, 1.05))
plt.savefig('DD_Mh1_ld345_mh+100_new.pdf')

plt.clf()
