/*====== Modules ===============
   Keys to switch on 
   various modules of micrOMEGAs  
================================*/
      
#define MASSES_INFO    
  /* Display information about mass spectrum  */
#define OMEGA           
  /* Calculate relic density and display contribution of  individual channels */
      
#define CDM_NUCLEON     
  /* Calculate amplitudes and cross-sections for  CDM-nucleon collisions */  

/*===== End of DEFINE  settings ===== */

#include"../../sources/micromegas.h"
#include"../../sources/micromegas_aux.h"
#include"../lib/pmodel.h"
#include <time.h>

/*******START***********************/
int main(int argc,char** argv)
{  int err;
   char cdmName[10];
   int spin2, charge3,cdim;
   
  ForceUG=0;  /* to Force Unitary Gauge assign 1 */

  VZdecay=2; VWdecay=2; 
   
 int i;
 i=0;
  FILE *f1 = fopen("ld345=1.dat","w"); 
 fprintf(f1,"%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s \n"," Mh1   ","   Mh2  ","   Mhc   ","  ld345   ", "    ld    ", "    Omega  ","    protonSI ","   Br(H->h1h1) ","  Br(H->h2h2) "," Br(H->h-h+) ","   Width_H   ", "  HB  ", "  HS  ","   R   ","  v_stab ","   LEP ", "  S    ","   T  ");
 
 double massh1, massh2, massCH, ld345, ldm345, ld, ld45, ld3, ld4, ld5, protonSI, Omega, MDM, limit, lamS, md2, vv, massW, massZ, alfa;
 int vstab,minvac;
 Omega=0;
 protonSI=0;
  
  for(massh2 = 200; massh2 <= 200; massh2 = massh2 + 1)
     {  for(massCH = 200; massCH <= 200; massCH = massCH + 1)  
           {   for(massh1 = 10; massh1 <= 200; massh1 = massh1 + 1)
	         {  for(ld345 = 1; ld345 <= 1; ld345 = ld345 + 0.001)
	               {  for(ld = 3.73 /*0.15*/; ld <= 3.73 /* 0.15*/; ld=ld + 0.01) 
                          {    
                          i=i+1;
                        		
   if(massh1<=massh2 && massh1<=massCH)
   {assignValW("Mh1",massh1);
			assignValW("Mh2",massh2);
			assignValW("Mhc",massCH);
			assignValW("ld345",ld345);
			assignValW("ld",ld);      
			
  			err=sortOddParticles(cdmName); }
   
   else{
     /* printf("Mass Dark Matter bigger than other 2 odd mass\n");*/ continue;
      			}
  
			if(err) { printf("Can't calculate %s\n",cdmName); continue;}
    			
    			findVal("Mh1",&massh1);
			findVal("Mhc",&massCH);
			findVal("Mh2",&massh2);
			findVal("ld345",&ld345);
			findVal("ld",&ld);
			findVal("ld3",&ld3);
			findVal("ld4",&ld4);
			findVal("ld5",&ld5);
			findVal("md2",&md2);
			findVal("vv",&vv);
			findVal("lam",&lamS);
			findVal("MZ",&massZ);
			findVal("MW",&massW);
			MDM = fmin(massh1,massh2);
			ld45 = ld4 + ld5;
			ldm345 = ld3 + ld4 - ld5;
     
  vstab=0;
  minvac=0;
  /**** Minimum of the vacuum ****/ /*With this conditions we are make sure that the potential is bounded from below and is a neutral vacuum*/
   
   if(  ld45 < 0 
     && ld5 < 0 
     && lamS > 0 
     && ld > 0 
     && 2*sqrt(ld*lamS) + ld3 > 0 
     && 2*sqrt(ld*lamS) + ld345 > 0 
     && 2*sqrt(ld*lamS) + ldm345 > 0 ) 
     {minvac=1;}
  
  /***  Stability of the vacuum  ***/ 
  /* Region I and II */
   if( 4*lamS*ld-ld345*ld345>0 )    	 
     {  if (md2 < (1/2)*vv*vv*ld345 && vv*vv*lamS>0) {vstab=1;}
           
        else {vstab=-1;}
                           }
   /* Region III */
   else{
        if (ld345>0 && md2 < vv*vv*sqrt(ld*lamS) && vv*vv*lamS>0)  {vstab=2;}  
          
        else {vstab=-2;}
 			   }

    qNumbers(cdmName, &spin2, &charge3, &cdim); 
  /*  printf("\n========== NEW POINT ==========\n");
    printf("\nDark matter candidate is '%s' with spin=%d/2\n", cdmName,	 spin2); */
        
   if(vstab > 0 && minvac > 0){

 txtList braH;
 double BraH_1,BraH_2,BraH_3,Brat_1,Brat_2,WH;

  /*Mass and width decay of neutral higgs*/
   WH = pWidth("H",&braH);

  /*Branching ratios of Neutral higgs without Standard Model equivalents */
  BraH_1 = findBr(braH,"~h1,~h1");
  BraH_2 = findBr(braH,"~h2,~h2");
  BraH_3 = findBr(braH,"~h+,~h-");
 
/* HiggsBounds and HiggsSignals limits*/ 
 int HS,HB;
 if(BraH_1 < 0.312){HS=1;}
 else {HS=0;}

 if(BraH_1 < 0.6304){HB=1;}
 else {HB=0;}

/* Calculation of the R value corresponding to the diferent zones of the vacuum stability */
  int region; 
  double R; 
  R = ld345/(2*sqrt(ld*lamS));

/* Calculation of the vacuum stability zone */
 if(R>0 && R<1) {region = 1;}
 if(R>-1 && R<0) {region = 2;}
 if(R>1) {region = 3;}
  
/* LEP limits */
  int LEP, LEP_lim;
     LEP_lim = 0;

 if (massh1 + massCH < massW) {LEP_lim = -1;}
 if (massh2 + massCH < massW) {LEP_lim = -2;}
 if (massh1 + massh2 < massZ) {LEP_lim = -4;}
 if (2*massCH < massZ) {LEP_lim = -8;}

 if (LEP_lim < 0){LEP = LEP_lim;}
 else{LEP = 1;}

/* Electroweak Precision Test */
float DS,DT,DF;
float PI = 3.14159265359;
float alfa = 0.00729735;

/* Parameter S */
float S(float Sh1,float Sh2,float Shc){
float S1,S2,S3,resultS,beta,delta;
beta = 0.1666666666667;
delta = 0.138888888889;
  S1 = beta*log((Sh1*Sh1)/(Shc*Shc)); 
  S2 = ((Sh1*Sh1)*(Sh2*Sh2))/(3*(Sh2*Sh2-Sh1*Sh1)*(Sh2*Sh2-Sh1*Sh1));
  S3 = ((Sh2*Sh2*Sh2*Sh2)/6)*((Sh2*Sh2-3*Sh1*Sh1)/((Sh2*Sh2-Sh1*Sh1)*(Sh2*Sh2-Sh1*Sh1)*(Sh2*Sh2-Sh1*Sh1)))*log((Sh2*Sh2)/(Sh1*Sh1));
  resultS = (1/(2*PI))*(S1 - delta + S2 + S3);
return resultS;
}

/* Definimos la funcion F */ 
float F(float x,float y){
float resultF;
	if (x==y) {resultF = 0;}
	else {resultF = (x*x+y*y)/2 - ((x*x*y*y)/(x*x-y*y))*log((x*x)/(y*y));}
return resultF;
}

/* Parameter T */
float T(float Th1,float Th2,float Th3){
float resultT,den;
	den = 32*PI*PI*alfa*vv*vv;
	resultT = (1/den)*(F(Th3,Th2) + F(Th3,Th1) - F(Th2,Th1));
return resultT;
}
  
DF = F(massh1,massh2);
DS = S(massh1,massh2,massCH);
DT = T(massh1,massh2,massCH);

#ifdef MASSES_INFO
{ 
  printf("\n=== MASSES OF HIGG AND ODD PARTICLES: ===\n");
  
  printHiggs(stdout);
  printMasses(stdout,1);
 
}
#endif


#ifdef OMEGA
{ int fast=1;
  double Beps=1.E-4, cut=0.01;
  double Xf;  
  int i,err; 
  double Lmin,Lmax,vS;
 /* printf("\n---- Calculation of relic density ---\n");   */
  

 Omega= darkOmega(&Xf,fast,Beps);


 printChannels(Xf,cut,Beps,1,stdout);
 printf("omega1=%.2E \n", Omega);
 

}

#endif


#ifdef CDM_NUCLEON
{ double pA0[2],pA5[2],nA0[2],nA5[2];
  double Nmass=0.939; /*nucleon mass*/
  double SCcoeff;        

printf("\n==== Calculation of CDM-nucleons amplitudes  =====\n");   

  if(CDM1)
  {  
    nucleonAmplitudes(CDM1,NULL, pA0,pA5,nA0,nA5);
    printf("CDM[antiCDM]-nucleon micrOMEGAs amplitudes for %s \n",CDM1);
    printf("proton:  SI  %.3E [%.3E]  SD  %.3E [%.3E]\n",pA0[0], pA0[1],  pA5[0], pA5[1] );
    printf("neutron: SI  %.3E [%.3E]  SD  %.3E [%.3E]\n",nA0[0], nA0[1],  nA5[0], nA5[1] ); 

  SCcoeff=4/M_PI*3.8937966E8*pow(Nmass*Mcdm/(Nmass+ Mcdm),2.);
    printf("CDM[antiCDM]-nucleon cross sections[pb]:\n");
    printf(" proton  SI %.3E [%.3E] SD %.3E [%.3E]\n",
       SCcoeff*pA0[0]*pA0[0],SCcoeff*pA0[1]*pA0[1],3*SCcoeff*pA5[0]*pA5[0],3*SCcoeff*pA5[1]*pA5[1]);
    printf(" neutron SI %.3E [%.3E] SD %.3E [%.3E]\n",
       SCcoeff*nA0[0]*nA0[0],SCcoeff*nA0[1]*nA0[1],3*SCcoeff*nA5[0]*nA5[0],3*SCcoeff*nA5[1]*nA5[1]);
  }
  if(CDM2)
  {
    nucleonAmplitudes(CDM2,NULL, pA0,pA5,nA0,nA5);
    printf("CDM[antiCDM]-nucleon micrOMEGAs amplitudes for %s \n",CDM2);
    printf("proton:  SI  %.3E [%.3E]  SD  %.3E [%.3E]\n",pA0[0], pA0[1],  pA5[0], pA5[1] );
    printf("neutron: SI  %.3E [%.3E]  SD  %.3E [%.3E]\n",nA0[0], nA0[1],  nA5[0], nA5[1] ); 

  SCcoeff=4/M_PI*3.8937966E8*pow(Nmass*Mcdm/(Nmass+ Mcdm),2.);
    printf("CDM[antiCDM]-nucleon cross sections[pb]:\n");
    printf(" proton  SI %.3E [%.3E] SD %.3E [%.3E]\n",
       SCcoeff*pA0[0]*pA0[0],SCcoeff*pA0[1]*pA0[1],3*SCcoeff*pA5[0]*pA5[0],3*SCcoeff*pA5[1]*pA5[1]);
    printf(" neutron SI %.3E [%.3E] SD %.3E [%.3E]\n",
       SCcoeff*nA0[0]*nA0[0],SCcoeff*nA0[1]*nA0[1],3*SCcoeff*nA5[0]*nA5[0],3*SCcoeff*nA5[1]*nA5[1]);
  }     
    protonSI= SCcoeff*pA0[0]*pA0[0];
    printf("protonSI= %.3E [pb]\n",protonSI);
}
#endif
    
     

 fprintf(f1,"%.2f   %.2f   %.2f   %.3E   %.3E   %.3E    %.3E     %.3E      %.3E     %.3E     %.3E      %i      %i    %.3f      %i        %i    %.3f    %.3f \n", massh1, massh2, massCH, ld345, ld, Omega, protonSI, BraH_1, BraH_2, BraH_3, WH, HB, HS, R, region, LEP, DS, DT);

  }}}}}}

  return 0;
}
