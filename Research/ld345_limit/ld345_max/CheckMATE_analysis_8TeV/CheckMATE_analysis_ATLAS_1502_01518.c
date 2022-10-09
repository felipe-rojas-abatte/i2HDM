#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define PYTHIA "/home/felipe/Documents/Programas/pythia8205/examples/pp_h1h1j"

int main()
{   

 FILE *fCMR = fopen("CM_atlas_1502.01518_new_ld345_8TeV.txt","w");

 system("mkdir /home/felipe/Documents/Programas/pythia8205/examples/pp_h1h1j");
 system("mkdir /home/felipe/Documents/Programas/CheckMATE-1.2.2/bin/pp_h1h1j");

/* Open file with numerical ld345_max */
FILE *num_ld345_max = fopen("l345_limit.dat","r");

fprintf(fCMR,"%s %s %s %s %s %s %s %s %s %s %s %s %s \n",
 "    Mh1  ", " ld345 ", "   cross_section  ","  best_SR  "," MC_Events ", " N_events  ",
 "   r_value  ","   Acceptance ","  Lumin ", "    error_S  ", "   S_obs    ","     S_exp","   cross_sec_limit  ");
 

int energy,n_events,Mh1,K;
float ld345_max,lum,ld345;
char analysis[20];

energy = 4000; /*Energy of 1 proton GeV*/
n_events = 20000;  /*N° of events*/
lum = 20;  /* Luminosity in fb-1*/  
strcpy(analysis, "atlas_1502_01518" ); 

/* atlas_conf_2012_147 Monojet + missing energy analisis at 10 fb^(-1) */
/* atlas_1407_0608 Monojet + missing energy analisis at 20 fb^(-1) */
/* atlas_1502_01518 Monojet energy analisis at 20 fb^(-1) */
/* cms_1408_3583 Monojet + missing energy analysis at 19.5 fb^(-1) */


/*float ld345_fhi(float mh1){
float MH,MW,MZ,ee,CW,SW,GSM,vev,PI,l1,l2,result;
MH=125;
MW=80.401;
MZ=91.187;
ee=0.31343;
CW=MW/MZ;
SW=sqrt(1-CW*CW);
GSM=4.255E-03;
vev=(2*MW*SW)/ee;
PI = 3.14159265359;
l1 = (MH*MH)/(2*vev*vev);
l2 = 4*PI/3;
  result = 2*((mh1/vev)*(mh1/vev) + sqrt(l1*l2));
return result;
}*/

float ld345_flow(float mh1){
float MH,MW,MZ,ee,CW,SW,GSM,vev,PI,result,num,den,Br;
MH=125;
MW=80.401;
MZ=91.187;
ee=0.31343;
CW=MW/MZ;
SW=sqrt(1-CW*CW);
Br=0.28;
GSM=4.255E-03;
vev=(2*MW*SW)/ee;
PI = 3.14159265359;
num= 4*PI*ee*ee*MH*Br*GSM;
den= (1-Br)*SW*SW*MW*MW*sqrt(1-4*(mh1/MH)*(mh1/MH));
result = sqrt(num/den);
return result;
}

     for(K = 10; K <= 200; K=K+50)  {

/* Genero el archivo BATCH con la información del proceso*/
 FILE *f10 = fopen("pp_h1h1j_cc","w"); 

if(K<=62.5){ 
  	ld345_max = ld345_flow(K);
	printf("\n For Mh1 = %i, lambda_345 max = %.6f \n ", K, ld345_max);}

else{   do{fscanf(num_ld345_max,"%i  %f ",&Mh1, &ld345);} while(Mh1<K);
	   ld345_max = ld345;
	   printf("\n Mh1 = %i, K = %i \n",Mh1,K);
	   printf("\n For Mh1 = %i, lambda_345 max = %.6f \n ", K, ld345_max);}

fprintf(f10,"Model: SM+2IHDM \n");
fprintf(f10,"Model changed: False\n");
fprintf(f10,"Gauge: Feynman\n");
fprintf(f10,"Process: p,p->~h1,~h1,jet\n");
fprintf(f10,"Composite: p=u,U,d,D,s,S,c,C,b,B,G\n");
fprintf(f10,"Composite: jet=u,U,d,D,s,S,c,C,b,B,G\n");
fprintf(f10,"pdf1: cteq6l (proton)\n");
fprintf(f10,"pdf2: cteq6l (proton)\n");
fprintf(f10,"p1: %i \n", energy);
fprintf(f10,"p2: %i \n", energy);
fprintf(f10,"Parameter: Mh1=%i \n", K);
fprintf(f10,"Parameter: Mh2=%i \n", K);
fprintf(f10,"Parameter: Mhc=200\n");
fprintf(f10,"Parameter: ld=1\n");
fprintf(f10,"Parameter: ld345=%.6f \n",ld345_max);
fprintf(f10,"alpha Q : T5\n"); 
fprintf(f10,"Cut parameter: T(jet)\n");
fprintf(f10,"Cut invert: False\n");
fprintf(f10,"Cut min: 100\n");
fprintf(f10,"Kinematics : 12 -> 34, 5\n");
fprintf(f10,"Kinematics : 34 -> 3 , 4\n");
fprintf(f10,"Regularization momentum:1: 34\n");
fprintf(f10,"Regularization mass:1: MH\n");
fprintf(f10,"Regularization width:1: wH\n");
fprintf(f10,"Regularization power:1: 2\n");
fprintf(f10,"Number of events (per run step): %i \n",n_events);
fprintf(f10,"Filename: pp_h1h1j\n");
fprintf(f10,"NTuple: False\n");
fprintf(f10,"Cleanup: False\n");
fprintf(f10,"Parallelization method: local\n");
fprintf(f10,"Max number of nodes: 8\n");
fprintf(f10,"Max number of processes per node: 1\n");
fprintf(f10,"sleep time: 3\n");
fprintf(f10,"nice level: 19\n");
fprintf(f10,"nSess_1: 5\n");
fprintf(f10,"nCalls_1: 100000\n");
fprintf(f10,"nSess_2: 5\n");
fprintf(f10,"nCalls_2: 100000\n");
fclose(f10);

/****** Ejecuto el archivo BATCH *******/

printf("\n ================================ \n Ejecutando archivo batch n=%i \n ================================ \n\n",K);

printf("  Parameters \n  Mh1 = %i(GeV)  ld345 = %.6f   N° events= %i  \n",K,ld345_max,n_events);

system("./calchep_batch pp_h1h1j_cc");


/******* Elimino la parte que no me gusta del archivo numerical.txt ********/

FILE *oldFile = fopen("/home/felipe/Documents/Programas/micromegas_4.1.8/2IHDM_fixed/work/html/numerical.txt", "r");
FILE *newFile = fopen("/home/felipe/Documents/Programas/micromegas_4.1.8/2IHDM_fixed/work/new_numerical.txt", "w");

int lineNumber;
int len;
char line[4096],line1[4096];
int todoNumber;
lineNumber=0;

/**** Debemos seleccionar la cantidad de líneas que deseamos eliminar del archivo numerical ****/
todoNumber=6;

if (oldFile != NULL) {
    while (fgets(line, sizeof line, oldFile)) {
        len = strlen(line);
        if (len && (line[len - 1] != '\n')) {} else {
            lineNumber++;
            if (lineNumber < todoNumber) {
                // Do nothing   
            } else {
                fputs(line, newFile);
            }
        }
    }
} else {
    printf("ERROR");
}
fclose(oldFile);
fclose(newFile);

/**** Extrae la sección eficaz del archivo numerical *****/
 
  FILE *f2 = fopen("/home/felipe/Documents/Programas/micromegas_4.1.8/2IHDM_fixed/work/new_numerical.txt","r");

    float sig;
      fscanf(f2,"%*s  %f  %*s  %*s  %*f  %*f",&sig);
      
fclose(f2);

remove("/home/felipe/Documents/Programas/micromegas_4.1.8/2IHDM_fixed/work/new_numerical.txt");


/***** Descomprime archivo .lhe *****/
system("gunzip /home/felipe/Documents/Programas/micromegas_4.1.8/2IHDM_fixed/work/Events/pp_h1h1j-single.lhe.gz");
/****** Mueve el archivo .lhe a la carpeta examples en pythia ******/
system("cp /home/felipe/Documents/Programas/micromegas_4.1.8/2IHDM_fixed/work/Events/pp_h1h1j-single.lhe /home/felipe/Documents/Programas/pythia8205/examples/pp_h1h1j/pp_h1h1j.lhe");

/******* Genero el archivo .cmnd para pythia ********/

 FILE *fcmnd = fopen("/home/felipe/Documents/Programas/pythia8205/examples/pp_h1h1j/pp_h1h1j.cmnd","w");
fprintf(fcmnd,"! File: main42.cmnd \n");
fprintf(fcmnd,"! This file contains commands to be read in for a Pythia8 run.\n");
fprintf(fcmnd,"! Lines not beginning with a letter or digit are comments.\n");
fprintf(fcmnd,"! Names are case-insensitive  -  but spellings-sensitive!\n");
fprintf(fcmnd,"! The changes here are illustrative, not always physics-motivated.\n\n");

fprintf(fcmnd,"! 1) Settings that will be used in a main program.\n");
fprintf(fcmnd,"Main:numberOfEvents = %i        ! number of events to generate\n",n_events);
fprintf(fcmnd,"Main:timesAllowErrors = 3          ! abort run after this many flawed events\n\n");

fprintf(fcmnd,"! 2) Settings related to output in init(), next() and stat().\n");
fprintf(fcmnd,"Init:showChangedSettings = on      ! list changed settings\n");
fprintf(fcmnd,"Init:showAllSettings = off         ! list all settings\n");
fprintf(fcmnd,"Init:showChangedParticleData = on  ! list changed particle data\n");
fprintf(fcmnd,"Init:showAllParticleData = off     ! list all particle data\n");
fprintf(fcmnd,"Next:numberCount = 1000            ! print message every n events\n");
fprintf(fcmnd,"Next:numberShowLHA = 1             ! print LHA information n times\n");
fprintf(fcmnd,"Next:numberShowInfo = 1            ! print event information n times\n");
fprintf(fcmnd,"Next:numberShowProcess = 1         ! print process record n times\n");
fprintf(fcmnd,"Next:numberShowEvent = 1           ! print event record n times\n");
fprintf(fcmnd,"Stat:showPartonLevel = on          ! additional statistics on MPI\n\n");

fprintf(fcmnd,"! 3) Beam parameter settings. Values below agree with default ones.\n");
fprintf(fcmnd,"Beams:idA = 2212                   ! first beam, p = 2212, pbar = -2212\n");
fprintf(fcmnd,"Beams:idB = 2212                   ! second beam, p = 2212, pbar = -2212\n");
fprintf(fcmnd,"Beams:eCM = %i.                 ! CM energy of collision\n\n",2*energy);

fprintf(fcmnd,"! 4a) Pick processes and kinematics cuts.\n");
fprintf(fcmnd,"! Colour singlet charmonium production of J/psi and chi_c.\n");
fprintf(fcmnd,"! Charmonium:gg2ccbar(3S1)[3S1(1)]g    = on,off\n");
fprintf(fcmnd,"! Charmonium:gg2ccbar(3PJ)[3PJ(1)]g    = on,on,on\n");
fprintf(fcmnd,"! Charmonium:qg2ccbar(3PJ)[3PJ(1)]q    = on,on,on\n");
fprintf(fcmnd,"! Charmonium:qqbar2ccbar(3PJ)[3PJ(1)]g = on,on,on\n");
fprintf(fcmnd,"! PhaseSpace:pTHatMin = 20.          ! minimum pT of hard process\n\n");

fprintf(fcmnd,"! 4b) Alternative beam and process selection from a Les Houches Event File.\n");
fprintf(fcmnd,"! NOTE: to use this option, comment out the lines in section 4a above\n");
fprintf(fcmnd,"! and uncomment the ones below. Section 3 is ignored for frameType = 4.\n");
fprintf(fcmnd,"Beams:frameType = 4                ! read info from a LHEF\n");
fprintf(fcmnd,"Beams:LHEF = /home/felipe/Documents/Programas/pythia8205/examples/pp_h1h1j/pp_h1h1j.lhe             ! the LHEF to read from\n\n");

fprintf(fcmnd,"! 5) Other settings. Can be expanded as desired.\n");
fprintf(fcmnd,"! Note: may overwrite some of the values above, so watch out.\n");
fprintf(fcmnd,"#Tune:pp = 6                        ! use Tune 4Cx\n");
fprintf(fcmnd,"#ParticleDecays:limitTau0 = on      ! set long-lived particle stable ...\n");
fprintf(fcmnd,"#ParticleDecays:tau0Max = 10        ! ... if c*tau0 > 10 mm\n");
fclose(fcmnd);

/******* Ejecuto el archivo .lhe en Pythia *******/

printf("\n ================================ \n Ejecutando archivo pythia n=%i \n ================================ \n\n",K);

printf(" Cross Section = %.4f(fb) \n ",sig);

system("/home/felipe/Documents/Programas/pythia8205/examples/main42 /home/felipe/Documents/Programas/pythia8205/examples/pp_h1h1j/pp_h1h1j.cmnd /home/felipe/Documents/Programas/pythia8205/examples/pp_h1h1j/pp_h1h1j.hepmc > /home/felipe/Documents/Programas/pythia8205/examples/pp_h1h1j/pp_h1h1j_out");

/******* Genero el archivo .dat para CheckMATE *******/

FILE *fdat = fopen("/home/felipe/Documents/Programas/CheckMATE-1.2.2/bin/pp_h1h1j/pp_h1h1j.dat","w");

fprintf(fdat,"## General Options \n");
fprintf(fdat,"[Mandatory Parameters] \n");
fprintf(fdat,"Name: pp_h1h1j \n");
fprintf(fdat,"Analyses: %s \n\n",analysis); 
fprintf(fdat,"[Optional Parameters] \n\n");
fprintf(fdat,"SkipParamCheck: yes \n\n");
fprintf(fdat,"## Process Information (Each new process 'X' must start with [X]) \n");
fprintf(fdat,"[pp_h1h1j_1_8TEV_20k] \n");
fprintf(fdat,"XSect: %.4E *FB \n",sig);
fprintf(fdat,"XSectErr: 0*FB \n");
fprintf(fdat,"Events: /home/felipe/Documents/Programas/pythia8205/examples/pp_h1h1j/pp_h1h1j.hepmc");
fclose(fdat);

/******* Ejecuto el archivo .hepmc en CheckMATE *******/

printf("\n ======================================= \n Ejecutando archivo CheckMATE n=%i \n ======================================= \n\n",K);

system("/home/felipe/Documents/Programas/CheckMATE-1.2.2/bin/CheckMATE /home/felipe/Documents/Programas/CheckMATE-1.2.2/bin/pp_h1h1j/pp_h1h1j.dat"); 

/******* Extraigo la información del archivo best signal region *******/

FILE *fbsr = fopen("/home/felipe/Documents/Programas/CheckMATE-1.2.2/results/pp_h1h1j/evaluation/best_signal_regions.txt","r");

 float r_obs, r_exp, S, dS_stat, dS_sys, dS_tot, S95_obs, S95_exp; 
    char bestSR[3]=""; 
    char atlas[200]="";
   
   fscanf(fbsr,"%*s  %*s  %*s  %*s  %*s  %*s  %*s  %*s  %*s  %*s");
   fscanf(fbsr,"%s  %s  %f  %f  %f  %f  %f  %f  %f  %f",atlas, bestSR, &r_obs, &r_exp, &S, &dS_stat, &dS_sys, &dS_tot, &S95_obs, &S95_exp); 

printf("\n \n bestSR=%s  r_obs=%.3f  r_exp=%.3f  S=%.3f  dS_stat=%.3f  dS_sys=%.3f  dS_tot=%.3f  S95_obs=%.3f  S95_exp=%.3f \n \n",bestSR, r_obs, r_exp, S, dS_stat, dS_sys, dS_tot, S95_obs, S95_exp);

/******** Genera el archivo con la información de analysis*************/

FILE *oldAnalysis = fopen("/home/felipe/Documents/Programas/CheckMATE-1.2.2/results/pp_h1h1j/analysis/000_atlas_1502_01518_signal.dat", "r");

FILE *newAnalysis = fopen("/home/felipe/Documents/Programas/micromegas_4.1.8/2IHDM_fixed/work/analysis.txt", "w");

int BSR = bestSR[2] - '0';

char line2[4096];
int todoN,lineN,len2;
lineN=0;

if(BSR==1){todoN=17;}
if(BSR==2){todoN=18;}
if(BSR==3){todoN=19;}
if(BSR==4){todoN=20;}
if(BSR==5){todoN=21;}
if(BSR==6){todoN=22;}
if(BSR==7){todoN=23;}
if(BSR==8){todoN=24;}
if(BSR==9){todoN=25;}

if (oldAnalysis != NULL) {
    while (fgets(line2, sizeof line2, oldAnalysis)) {
        len2 = strlen(line2);
        if (len2 && (line2[len2 - 1] != '\n')) {} else {
            lineN++;
            if (lineN < todoN) {
                // Do nothing   
            } else {
                fputs(line2, newAnalysis);
            }
        }
    }
} else {
    printf("ERROR");
}
fclose(oldAnalysis);
fclose(newAnalysis);

float Sum_W,Sum_W2,Acc,N_Norm,r,cc_lim;
char SR[10]="";

FILE *analysis = fopen("/home/felipe/Documents/Programas/micromegas_4.1.8/2IHDM_fixed/work/analysis.txt","r");
fscanf(analysis,"%s  %f  %f  %f  %f",SR, &Sum_W, &Sum_W2, &Acc, &N_Norm); 

printf("SR=%s  Sum_W=%.f  Sum_W2=%.f  Acc=%f  N_Norm=%.4E \n \n",SR,Sum_W,Sum_W2,Acc,N_Norm); 

fclose(fbsr);
fclose(analysis);

/******* Calculamos seccion eficaz limite *******/

cc_lim = (S95_obs + 1.96*dS_tot)/(lum*Acc);
r = (lum*Acc*sig-1.96*dS_tot)/(S95_obs);

printf("Acc = %.4E  cc_lim = %.3E  cc = %.3E  S = %.4E S95_obs = %.2E  S95_exp = %.2E  r = %.3E  \n\n",Acc,cc_lim,sig,S,S95_obs,S95_exp,r);

fprintf(fCMR,"    %i   %.6f      %.3E          %s        %i      %.3f       %.5f        %.3f        %.f       %.2E      %.2E      %.2E      %.2f   \n",K,ld345_max,sig,SR,n_events,N_Norm,r,Acc,lum,dS_tot,S95_obs,S95_exp,cc_lim); 

/*Elimino la carpeta results de CheckMATE*/
system("rm -R /home/felipe/Documents/Programas/CheckMATE-1.2.2/results/pp_h1h1j");


}
return 0; 
}

 
