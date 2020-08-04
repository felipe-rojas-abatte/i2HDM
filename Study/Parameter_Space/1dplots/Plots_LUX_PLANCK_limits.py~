import numpy as np
import matplotlib
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
Mh1a, Mh2a, Mhca, ld345a ,lda, Omegaa, prota, Brh1a, Brh2a, Brhca, WHa, HBa, HSa, Ra, vstaba, LEPa, Sa, Ta  = np.genfromtxt("Datos/ld345=1.dat",dtype=float,unpack=True,skip_header=True) 
Mh1b, Mh2b, Mhcb, ld345b ,ldb, Omegab, protb, Brh1b, Brh2b, Brhcb, WHb, HBb, HSb, Rb, vstabb, LEPb, Sb, Tb  = np.genfromtxt("Datos/ld345=0.5.dat",dtype=float,unpack=True,skip_header=True) 
Mh1c, Mh2c, Mhcc, ld345c ,ldc, Omegac, protc, Brh1c, Brh2c, Brhcc, WHc, HBc, HSc, Rc, vstabc, LEPc, Sc, Tc  = np.genfromtxt("Datos/ld345=0.2.dat",dtype=float,unpack=True,skip_header=True) 
Mh1d, Mh2d, Mhcd, ld345d ,ldd, Omegad, protd, Brh1d, Brh2d, Brhcd, WHd, HBd, HSd, Rd, vstabd, LEPd, Sd, Td  = np.genfromtxt("Datos/ld345=0.02.dat",dtype=float,unpack=True,skip_header=True) 
Mh1e, Mh2e, Mhce, ld345e ,lde, Omegae, prote, Brh1e, Brh2e, Brhce, WHe, HBe, HSe, Re, vstabe, LEPe, Se, Te  = np.genfromtxt("Datos/ld345=0.01.dat",dtype=float,unpack=True,skip_header=True) 
Mh1f, Mh2f, Mhcf, ld345f ,ldf, Omegaf, protf, Brh1f, Brh2f, Brhcf, WHf, HBf, HSf, Rf, vstabf, LEPf, Sf, Tf  = np.genfromtxt("Datos/ld345=0.001.dat",dtype=float,unpack=True,skip_header=True) 

#Read data for negatives values of ld345
Mh1g, Mh2g, Mhcg, ld345g ,ldg, Omegag, protg, Brh1g, Brh2g, Brhcg, WHg, HBg, HSg, Rg, vstabg, LEPg, Sg, Tg  = np.genfromtxt("Datos/ld345=-1.dat",dtype=float,unpack=True,skip_header=True) 
Mh1h, Mh2h, Mhch, ld345h ,ldh, Omegah, proth, Brh1h, Brh2h, Brhch, WHh, HBh, HSh, Rh, vstabh, LEPh, Sh, Th  = np.genfromtxt("Datos/ld345=-0.5.dat",dtype=float,unpack=True,skip_header=True) 
Mh1i, Mh2i, Mhci, ld345i ,ldi, Omegai, proti, Brh1i, Brh2i, Brhci, WHi, HBi, HSi, Ri, vstabi, LEPi, Si, Ti  = np.genfromtxt("Datos/ld345=-0.2.dat",dtype=float,unpack=True,skip_header=True) 
Mh1j, Mh2j, Mhcj, ld345j ,ldj, Omegaj, protj, Brh1j, Brh2j, Brhcj, WHj, HBj, HSj, Rj, vstabj, LEPj, Sj, Tj  = np.genfromtxt("Datos/ld345=-0.02.dat",dtype=float,unpack=True,skip_header=True) 
Mh1k, Mh2k, Mhck, ld345k ,ldk, Omegak, protk, Brh1k, Brh2k, Brhck, WHk, HBk, HSk, Rk, vstabk, LEPk, Sk, Tk  = np.genfromtxt("Datos/ld345=-0.01.dat",dtype=float,unpack=True,skip_header=True) 
Mh1l, Mh2l, Mhcl, ld345l ,ldl, Omegal, protl, Brh1l, Brh2l, Brhcl, WHl, HBl, HSl, Rl, vstabl, LEPl, Sl, Tl  = np.genfromtxt("Datos/ld345=-0.001.dat",dtype=float,unpack=True,skip_header=True) 

LUX=LUX_SIG(Mh1a)

## Re-scale the Direct Detection cross section Sigma_SI

re_sca = 0.00000001

prot_a = ((Omegaa/0.112)*prota)/re_sca
prot_b = ((Omegab/0.112)*protb)/re_sca
prot_c = ((Omegac/0.112)*protc)/re_sca
prot_d = ((Omegad/0.112)*protd)/re_sca
prot_e = ((Omegae/0.112)*prote)/re_sca
prot_f = ((Omegaf/0.112)*protf)/re_sca

prot_g = ((Omegag/0.112)*protg)/re_sca
prot_h = ((Omegah/0.112)*proth)/re_sca
prot_i = ((Omegai/0.112)*proti)/re_sca
prot_j = ((Omegaj/0.112)*protj)/re_sca
prot_k = ((Omegak/0.112)*protk)/re_sca
prot_l = ((Omegal/0.112)*protl)/re_sca

N_LUX = LUX/re_sca


## LUX limits on rescaled Direct Detection cross section Sigma_SI vs Mh1 for lambda_345>0 
fig, ax1 = plt.subplots()
ax1.fill_between(Mh1a, N_LUX, 1000 ,facecolor='palegreen', interpolate=True)
ax1.text(0.5, 0.85, 'LUX 85.3 live-days', verticalalignment='top', horizontalalignment='center',
        transform=ax1.transAxes, color='green', fontsize=18)

#Name of axes
plt.xlabel("Mh$_1$ (GeV)",fontsize=15)
plt.ylabel("$\\hat{\\sigma}_{SI}$",fontsize=20)
plt.title("LUX limit on rescaled Direct Detection Cross Section $\\hat{\\sigma}_{SI}$ for $\\lambda_{345}>0$" )
plt.xlim(10,1000)
plt.yscale('log') 

plt.plot(Mh1a, prot_a, label='$\lambda_{345}=1.0$',color='b')
plt.plot(Mh1b, prot_b, label='$\lambda_{345}=0.5$',color='g')
plt.plot(Mh1c, prot_c, label='$\lambda_{345}=0.2$',color='r')
plt.plot(Mh1d, prot_d, label='$\lambda_{345}=0.02$',color='m')
plt.plot(Mh1e, prot_e, label='$\lambda_{345}=0.01$',color='y')
plt.plot(Mh1f, prot_f, label='$\lambda_{345}=0.001$',color='k')

plt.plot(Mh1a, N_LUX, label='LUX',color='green',linewidth=2)

plt.legend(loc="lower left", borderaxespad=0.1,prop={'size':11})
plt.savefig('Omega_LUX_limit_pos.pdf')

#----------------------------------------------------------------------------------------------

 ## LUX limits on rescaled Direct Detection cross section Sigma_SI vs Mh1 for lambda_345<0 
fig, ax2 = plt.subplots()
ax2.fill_between(Mh1g, N_LUX, 1000 ,facecolor='palegreen', interpolate=True)
ax2.text(0.5, 0.85, 'LUX 85.3 live-days', verticalalignment='top', horizontalalignment='center',
       transform=ax2.transAxes, color='green', fontsize=18)

#Name of axes
plt.xlabel("Mh$_1$ (GeV)",fontsize=15)
plt.ylabel("$\\hat{\\sigma}_{SI}$",fontsize=20)
plt.title("LUX limit on rescaled Direct Detection Cross Section $\\hat{\\sigma}_{SI}$ for $\\lambda_{345}<0$" )
plt.xlim(10,1000)
plt.yscale('log') 

plt.plot(Mh1g, prot_g, label='$\lambda_{345}=-1.0$',color='b')
plt.plot(Mh1h, prot_h, label='$\lambda_{345}=-0.5$',color='g')
plt.plot(Mh1i, prot_i, label='$\lambda_{345}=-0.2$',color='r')
plt.plot(Mh1j, prot_j, label='$\lambda_{345}=-0.02$',color='m')
plt.plot(Mh1k, prot_k, label='$\lambda_{345}=-0.01$',color='y')
plt.plot(Mh1l, prot_l, label='$\lambda_{345}=-0.001$',color='k')

plt.plot(Mh1g, N_LUX, label='LUX',color='green',linewidth=2)

plt.legend(loc="lower left", borderaxespad=0.1,prop={'size':11})
plt.savefig('Omega_LUX_limit_neg.pdf')

#----------------------------------------------------------------------------------------------

## Planck limits for Relic Density vs Mh1 for ld_345>0
fig1 = plt.subplots()
#Name of axes
plt.xlabel("Mh$_1$ (GeV)",fontsize=15)
plt.ylabel("Relic Density $\\Omega h^2$",fontsize=15)
plt.title('Mh$_1$ vs. Relic Density $\\Omega h^2$ for $\\lambda_{345}>0$')
plt.yscale('log')  #Escala logaritmica para el eje y

plt.plot(Mh1a, Omegaa, label='$\lambda_{345}=1.0$',color='b')
plt.plot(Mh1b, Omegab, label='$\lambda_{345}=0.5$',color='g')
plt.plot(Mh1c, Omegac, label='$\lambda_{345}=0.2$',color='r')
plt.plot(Mh1d, Omegad, label='$\lambda_{345}=0.02$',color='m')
plt.plot(Mh1e, Omegae, label='$\lambda_{345}=0.01$',color='y')
plt.plot(Mh1f, Omegaf, label='$\lambda_{345}=0.001$',color='k')

plt.plot(Mh, lim_inf,linestyle='--',color='red')
plt.plot(Mh, omega,color='red')
plt.plot(Mh, lim_sup,linestyle='--',color='red')

plt.legend(loc="upper right", borderaxespad=0.1)
plt.savefig('Omega_Mh1_pos.pdf')
#plt.show()

#----------------------------------------------------------------------------------------------

## Planck limits for Relic Density vs Mh1 for ld_345<0
fig2 = plt.subplots()
#Name of axes
plt.xlabel("Mh$_1$ (GeV)",fontsize=15)
plt.ylabel("Relic Density $\Omega h^2$",fontsize=15)
plt.title('Mh$_1$ vs. Relic Density $\\Omega h^2$ for $\\lambda_{345}<0$')
plt.yscale('log')  #Escala logaritmica para el eje y

plt.plot(Mh1g, Omegag, label='$\lambda_{345}=-1.0$',color='b')
plt.plot(Mh1h, Omegah, label='$\lambda_{345}=-0.5$',color='g')
plt.plot(Mh1i, Omegai, label='$\lambda_{345}=-0.2$',color='r')
plt.plot(Mh1j, Omegaj, label='$\lambda_{345}=-0.02$',color='m')
plt.plot(Mh1k, Omegak, label='$\lambda_{345}=-0.01$',color='y')
plt.plot(Mh1l, Omegal, label='$\lambda_{345}=-0.001$',color='k')

plt.plot(Mh, lim_inf,linestyle='--',color='red')
plt.plot(Mh, omega,color='red')
plt.plot(Mh, lim_sup,linestyle='--',color='red')

plt.legend(loc="upper right", borderaxespad=0.1)
plt.savefig('Omega_Mh1_neg.pdf')

#----------------------------------------------------------------------------------------------

## LUX limits on Direct Detection cross section Sigma_SI vs Mh1 for lambda_345   
fig3, ax = plt.subplots()
ax.fill_between(Mh1a, LUX, 0.001 ,facecolor='palegreen', interpolate=True)
ax.text(0.45, 0.95, 'LUX 85.3 live-days',
        verticalalignment='top', horizontalalignment='center',
        transform=ax.transAxes,
        color='green', fontsize=15)

#nombre de los ejes y del grafico
plt.xlabel("Dark Matter mass Mh$_1$ (GeV)",fontsize=15)
plt.ylabel("Direct Detection $\\sigma_{SI}$ (pb)",fontsize=15)
plt.title("LUX limit for Direct Detection $\\sigma_{SI}$ vs Mh$_1$")
plt.xlim(10,1000)
plt.ylim(0.000000000000001,0.001)
plt.yscale('log')  #Escala logaritmica para el eje y

plt.plot(Mh1a, prota,label='$|\lambda_{345}|=1.0$',linestyle='--',color='b')
plt.plot(Mh1b, protb,label='$|\lambda_{345}|=0.5$',linestyle='--',color='g')
plt.plot(Mh1c, protc,label='$|\lambda_{345}|=0.2$',linestyle='--',color='r')
plt.plot(Mh1d, protd, label='$|\lambda_{345}|=0.02$',linestyle='--',color='m')
plt.plot(Mh1e, prote, label='$|\lambda_{345}|=0.01$',linestyle='--',color='y')
plt.plot(Mh1f, protf, label='$|\lambda_{345}|=0.001$',linestyle='--',color='k')

plt.plot(Mh1a, LUX, label='LUX',color='green',linewidth=2)

plt.legend(loc="upper right", borderaxespad=0.1,prop={'size':11},bbox_to_anchor=(1.05, 1.05))
plt.savefig('DD_Mh1_ld345.pdf')

plt.clf()
