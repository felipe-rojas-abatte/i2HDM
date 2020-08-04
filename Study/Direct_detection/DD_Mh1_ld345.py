import numpy as np
#import matplotlib
import matplotlib.pyplot as plt
import scipy.interpolate
import sys


#Crea los arreglos
DMmass1 = []
DMmass2 = []
DMmass3 = [] 
DMmass4 = [] 
DMmass5 = []
DMmass6 = []
DM_LUX = []

DD1 = [] 
DD2 = []
DD3 = []
DD4 = []
DD5 = []
DD6 = []
DD_LUX = []

#Lee los datos del archivo y los guarda en las variables MDM, Mh1, Mh2, Mhc, ld345, ld, ld45, ld5, omega, prot, Br, WH, vstab, HS
MDMa, Mh1a, Mh2a, Mhca, ld345a, lda, omegaa, prota, Brh1a, Brh2a, Brh3a, WHa, HBa, HSa, Ra ,vstaba, LEPa, Sa, Ta = np.genfromtxt("DD_ld345=1.dat",dtype=float,unpack=True,skip_header=True) 
MDMb, Mh1b, Mh2b, Mhcb, ld345b, ldb, omegab, protb, Brh1b, Brh2b, Brh3b, WHb, HBb, HSb, Rb ,vstabb, LEPb, Sb, Tb = np.genfromtxt("DD_ld345=0.5.dat",dtype=float,unpack=True,skip_header=True) 
MDMc, Mh1c, Mh2c, Mhcc, ld345c, ldc, omegac, protc, Brh1c, Brh2c, Brh3c, WHc, HBc, HSc, Rc ,vstabc, LEPc, Sc, Tc = np.genfromtxt("DD_ld345=0.2.dat",dtype=float,unpack=True,skip_header=True) 
MDMd, Mh1d, Mh2d, Mhcd, ld345d, ldd, omegad, protd, Brh1d, Brh2d, Brh3d, WHd, HBd, HSd, Rd ,vstabd, LEPd, Sd, Td = np.genfromtxt("DD_ld345=0.02.dat",dtype=float,unpack=True,skip_header=True) 
MDMe, Mh1e, Mh2e, Mhce, ld345e, lde, omegae, prote, Brh1e, Brh2e, Brh3e, WHe, HBe, HSe, Re ,vstabe, LEPe, Se, Te = np.genfromtxt("DD_ld345=0.01.dat",dtype=float,unpack=True,skip_header=True) 
MDMf, Mh1f, Mh2f, Mhcf, ld345f, ldf, omegaf, protf, Brh1f, Brh2f, Brh3f, WHf, HBf, HSf, Rf ,vstabf, LEPf, Sf, Tf = np.genfromtxt("DD_ld345=0.001.dat",dtype=float,unpack=True,skip_header=True) 
DMLUX, DDLUX = np.genfromtxt("LUX_data.dat",dtype=float,unpack=True,skip_header=True) 



#Llena los arreglos con las 3 variables x=Mh1, y=ld345, z=omega (z en escala logaritmica)
DMmass1 = np.array(Mh1a)
DD1 = np.array(prota)
DMmass2 = np.array(Mh1b)
DD2 = np.array(protb)
DMmass3 = np.array(Mh1c)
DD3 = np.array(protc)
DMmass4 = np.array(Mh1d)
DD4 = np.array(protd)
DMmass5 = np.array(Mh1e)
DD5 = np.array(prote)
DMmass6 = np.array(Mh1f)
DD6 = np.array(protf)
DM_LUX = np.array(DMLUX)
DD_LUX = np.array(DDLUX)

fig, ax = plt.subplots()
ax.fill_between(DM_LUX, DD_LUX, 0.001 ,facecolor='palegreen', interpolate=True)
ax.text(0.45, 0.95, 'LUX 85.3 live-days',
        verticalalignment='top', horizontalalignment='center',
        transform=ax.transAxes,
        color='green', fontsize=15)

#nombre de los ejes y del grafico
plt.xlabel("Dark Matter mass Mh$_1$ (GeV)",fontsize=15)
plt.ylabel("Direct Detection $\\sigma_{SI}$ (pb)",fontsize=15)
plt.title("LUX limit in \n plane Mh$_1$ vs. Direct Detection $\\sigma_{SI}$")
plt.xlim(10,200)
plt.ylim(0.00000000000001,0.001)
plt.yscale('log')  #Escala logaritmica para el eje y

plt.plot(DMmass1, DD1,label='$|\lambda_{345}|=1.0$',linestyle='--',color='b')
plt.plot(DMmass2, DD2,label='$|\lambda_{345}|=0.5$',linestyle='--',color='g')
plt.plot(DMmass3, DD3,label='$|\lambda_{345}|=0.2$',linestyle='--',color='r')
plt.plot(DMmass4, DD4, label='$|\lambda_{345}|=0.02$',linestyle='--',color='m')
plt.plot(DMmass5, DD5, label='$|\lambda_{345}|=0.01$',linestyle='--',color='y')
plt.plot(DMmass6, DD6, label='$|\lambda_{345}|=0.001$',linestyle='--',color='k')
plt.plot(DM_LUX,DD_LUX, label='LUX',color='green',linewidth=2)

plt.legend(loc="upper right", borderaxespad=0.1,prop={'size':11},bbox_to_anchor=(1.05, 1.05))
plt.savefig('DD_Mh1_ld345.pdf')
plt.show()
plt.clf()

