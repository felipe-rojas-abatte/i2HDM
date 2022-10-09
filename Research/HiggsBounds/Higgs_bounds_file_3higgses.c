/*====== Modules ===============
/*====== Modules ===============
   Keys to switch on 
   various modules of micrOMEGAs  
================================*/
      
#define MASSES_INFO      
  /* Display information about mass spectrum  */

#define HIGGSBOUNDS "../../HiggsBounds-4.2.0"


#define CROSS_SECTIONS

  
/*===== end of Modules  ======*/

/*===== Options ========*/
/*#define SHOWPLOTS*/
     /* Display  graphical plots on the screen */ 


#define CLEAN  to clean intermediate files

/*===== End of DEFINE  settings ===== */


#include"../sources/micromegas.h"
#include"../sources/micromegas_aux.h"
#include"lib/pmodel.h"
#include"lib/lesHouches.c"
#include <stdio.h>
#include <stdlib.h>


int main(int argc,char** argv)
{  int err,step,i,K;
   char cdmName[10];
   int spin2, charge3,cdim;
   double massH;          
  
     
   
/**** Create files ****/   
 FILE *f1 = fopen("2IHDM_MH_GammaTot.dat","w");
 FILE *f2 = fopen("2IHDM_MHplus_GammaTot.dat","w");
 FILE *f3 = fopen("2IHDM_effC.dat","w");
 FILE *f4 = fopen("2IHDM_BR_H_NP.dat","w");
 FILE *f5 = fopen("2IHDM_BR_t.dat","w");
 FILE *f6 = fopen("2IHDM_BR_Hplus.dat","w");
 FILE *f7 = fopen("2IHDM_LEP_HpHm_CS_ratios.dat","w"); 
 
 
 ForceUG=0;  /* to Force Unitary Gauge assign 1 */
  
  if(argc==1)
  { 
      printf(" Correct usage:  ./main  <file with parameters> \n");
      printf("Example: ./main data1.par\n");
      exit(1);
  }
                               
  err=readVar(argv[1]);
  
  if(err==-1)     {printf("Can not open the file\n"); exit(1);}
  else if(err>0)  { printf("Wrong file contents at line %d\n",err);exit(1);}
           
  
  err=sortOddParticles(cdmName);
 ////////////////////////////////////////
  /*Read the information stored in Benchmarks file*/
   FILE *f8 = fopen("Benchmarks.txt", "r");
    
    float massh1,massh2,massCH;  
    float ld345,ld;    
    for(K = 1; K <= 13; K++)  
       {fscanf(f8, "%f %f %f %f %f", &massh1, &massh2, &massCH, &ld345, &ld);
       printf("K = %i  massh1 = %.1f  massh2 = %.1f  massCH = %.1f  ld345 = %.3f  ld = %.2f \n ",K,massh1,massh2,massCH,ld345,ld);
  
  ///////////////////////////////////////////////////  
     assignValW("Mh1",massh1);
     assignValW("Mh2",massh2);
     assignValW("Mhc",massCH);
     assignValW("ld345",ld345);
     assignValW("ld",ld);  
    
    
      err=sortOddParticles(cdmName);

     if(err) { printf("Can't calculate %s\n",cdmName); return 0; }
    
     findVal("MH",&massH);
////////////////////////////////////////////////////////////////////
#ifdef MASSES_INFO
{
  printf("\n=== MASSES OF HIGG AND ODD PARTICLES: ===\n");
  printHiggs(stdout);
  printMasses(stdout,1);
      
}
#endif


////////////////////////////////////////////////////////////////////


/*Normalized cross section ratios for the leptonic higgs production */
#ifdef CROSS_SECTIONS
{  printf("Cross section from Leptons\n");
   char * pname1,*pname2; 
   char process[30];
   double Pcm=150.,cosmin=-0.99, cosmax=0.99;
   
   pname1= pdg2name(11);
   pname2= pdg2name(-11);
   if(pname1 && pname2)
   { numout*cc;
     sprintf(process,"%s,%s->2*x",pname1,pname2);
     cc=newProcess(process); 
     if(cc)
     {  int ntot,l;
        char * name[4];
        procInfo1(cc,&ntot,NULL,NULL); /*proporciona informacion sobre el n° de subprocesos y guarda el n° en                                                                         				ntot*/
        for(l=1;l<=ntot; l++)
        { int err;
          double cs;
          char txt[100];
          procInfo2(cc,l,name,NULL); /*crea un arreglo para cada subproceso con los nombres de particulas (name) y las masas de las particulas (NULL)*/
          sprintf(txt,"%3s,%3s -> %3s %3s  ",name[0],name[1],name[2],name[3]); /*Imprime el subproceso*/
          cs= cs22(cc,l,Pcm,cosmin,cosmax,&err);  /*calcula la seccion eficaz del subproceso*/
	  if(err) printf("%-20.20s    Error\n",txt);
          else if(cs<=0){printf("%-20.20s  %.2E [pb] l=%i\n",txt,0.0,l);
	                   switch(l){
		           case 1 :fprintf(f7,"%i  %.2E  \n",K,cs);}
	                   }
	    
	       else {printf("%-20.20s  %.2E [pb] l=%i\n",txt,cs,l);
	               switch(l){
		       case 1 :fprintf(f7,"%i  %.2E  \n",K,cs/cs);
		               
			       break;}
		       }
        }
     }
}
}
#endif 

/*Generating files for effC Higgs Bounds*/

  double Wh1,Wh2,Whc,WH,Wtop;
  txtList brah1,brah2,braH,brahc,brat;
  
  /*Mass and width decay of neutral higgs*/
  Wh1 = pWidth("~h1",&brah1);
  Wh2 = pWidth("~h2",&brah2);
  WH = pWidth("H",&braH);
  
  /*1-Generating the file 2IHDM_MH_GammaTot.dat)*/
  fprintf(f1,"%i  %.6E   %.6E   %.6E   %.6E  %.6E   %.6E \n",K,massh1,massh2,massH,Wh1,Wh2,WH);
  
  /*Mass and width decay of charged higgs*/ 
  Whc = pWidth("~h+",&brahc);
  
  /*2-Generating the file 2IHDM_MHplus_GammaTot.dat*/
  fprintf(f2,"%i  %.6E   %.6E \n",K,massCH,Whc);
  
  double ee,sinW,cosW,massZ,massW,massS,massC,massB,massT,massmu,massta,gHZZ2,gHWW2,ghHZ2,gsHcc2,gsHtt2,gsHss2, gsHbb2,gsHmumu2,gsHtata2,gsh1ff,gph1ff,gsh2ff,gph2ff,gsHff,gpHff,ldA,ldG,ghihjZ,gh1h2Z2,HWW2,HZZ2,HAA2,HGG2,HAZ2,HGGZ2,h1GBGB,h2GBGB,ghihjZ2,gHAA2,gHGG2,gHGGZ2,gHAZ2;  
   
 /*Parameters of the model*/
   findVal("EE",&ee);
   findVal("MZ",&massZ);
   findVal("MW",&massW);
   findVal("SW",&sinW);
   findVal("CW",&cosW);
   findVal("Ms",&massS);
   findVal("Mc",&massC);
   findVal("Mt",&massT);
   findVal("Mb",&massB);
   findVal("Mm",&massmu);
   findVal("Mtau",&massta);
   findVal("LmbdAA",&ldA);
   findVal("LmbdGG",&ldG);
 
 /*Effective scalar coupling (squered) Higgs-fermions in the 2IHDM */ 
   gsh1ff = 0;
   gsh2ff = 0;  
   gsHss2 = ((ee*massS)/(2*sinW*massW))*((ee*massS)/(2*sinW*massW));
   gsHcc2 = ((ee*massC)/(2*sinW*massW))*((ee*massC)/(2*sinW*massW));
   gsHtt2 = ((ee*massT)/(2*sinW*massW))*((ee*massT)/(2*sinW*massW));
   gsHbb2 = ((ee*massB)/(2*sinW*massW))*((ee*massB)/(2*sinW*massW));
   gsHmumu2 = ((ee*massmu)/(2*sinW*massW))*((ee*massmu)/(2*sinW*massW));
   gsHtata2 = ((ee*massta)/(2*sinW*massW))*((ee*massta)/(2*sinW*massW));
     
     
 /*There is not effective pseudo-scalar couplings Higgs-fermions in the 2IHDM*/  
   gph1ff = 0;
   gph2ff = 0;
   gpHff = 0; 
   
   
 /*Efective coupling (squered) Higgs-Gauge Bosons in the 2IHDM*/ 
   h1GBGB = 0;  
   h2GBGB = 0;  
   gHZZ2 = ((ee*massZ*massZ)/(sinW*massW))*((ee*massZ*massZ)/(sinW*massW));/*findBr(bra3,"Z,Z")*/
   gHWW2 = (ee*massW/sinW)*(ee*massW/sinW);/*findBr(bra3,"W+,W-")*/
   gHAA2 = findBr(braH,"A,A");/*((8*ldA*massW*sinW)/(ee*vv))*((8*ldA*massW*sinW)/(ee*vv));*/
   gHGG2 = findBr(braH,"G,G");/*((8*ldG*massW*sinW)/(ee*vv))*((8*ldG*massW*sinW)/(ee*vv));*/
   gHAZ2 = findBr(braH,"A,Z");
   gHGGZ2 = 0;
      
   ghihjZ2 = 0;
   gh1h2Z2 = (ee/(2*cosW*sinW))*(ee/(2*cosW*sinW));
  
 /*Efective coupling (squered) Higgs-Gauge Bosons in the Standard Model*/  
   HWW2 = ((ee*massW)/(sinW))*((ee*massW)/(sinW));/*2.15E-01;*/
   HZZ2 = ((ee*massW)/(cosW*cosW*sinW))*((ee*massW)/(cosW*cosW*sinW));/*2.64E-02;*/
   HAA2 = 2.28E-03;/*((8*ldA*massW*sinW)/(ee*vv))*((8*ldA*massW*sinW)/(ee*vv));*/
   HGG2 = findBr(braH,"G,G");/*((8*ldG*massW*sinW)/(ee*vv))*((8*ldG*massW*sinW)/(ee*vv));*/
   HAZ2 = 1.54E-03; /*findBr(bra3,"A,Z");*/
   HGGZ2 = 0;
      
  /*Effective coupling reference value*/
   ghHZ2 = (ee*ee)/(4*sinW*sinW*cosW*cosW);
   
  /*The only higgs that couple with fermions is the standard model higgs H and is CP even*/

  /*3-Generating the file effC.dat*/
  fprintf(f3,"%i  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E \n",K,
	  gsh1ff/gsHss2,   gsh2ff/gsHss2,   gsHss2/gsHss2,     gph1ff,        gph2ff,         gpHff, 
	  gsh1ff/gsHcc2,   gsh2ff/gsHcc2,   gsHcc2/gsHcc2,     gph1ff,        gph2ff,         gpHff, 
	  gsh1ff/gsHbb2,   gsh2ff/gsHbb2,   gsHbb2/gsHbb2,     gph1ff,        gph2ff,         gpHff,
	  gsh1ff/gsHtt2,   gsh2ff/gsHtt2,   gsHtt2/gsHtt2,     gph1ff,        gph2ff,  	      gpHff,
	  gsh1ff/gsHmumu2, gsh2ff/gsHmumu2, gsHmumu2/gsHmumu2, gph1ff,        gph2ff,  	      gpHff,  
	  gsh1ff/gsHtata2, gsh2ff/gsHtata2, gsHtata2/gsHtata2, gph1ff,        gph2ff,         gpHff,
	  h1GBGB/HWW2,	   h2GBGB/HWW2,     gHWW2/HWW2,        h1GBGB/HZZ2,   h2GBGB/HZZ2,    gHZZ2/HZZ2,
	  h1GBGB,     	   h2GBGB,          gHAZ2/HAZ2,        h1GBGB/HAA2,   h2GBGB/HAA2,    gHAA2/HAA2,
	  h1GBGB/HGG2,	   h2GBGB/HGG2,     gHGG2/HGG2,        h1GBGB,        h2GBGB,         gHGGZ2,
	  ghihjZ2/ghHZ2,   gh1h2Z2/ghHZ2,   ghihjZ2/ghHZ2,     ghihjZ2/ghHZ2, ghihjZ2/ghHZ2,     ghihjZ2/ghHZ2);


	 /*gsh1ff/gsHss2,   gph1ff,        gsh2ff/gsHss2,   gph2ff,        gsHss2/gsHss2,     gpHff, 
	  gsh1ff/gsHcc2,   gph1ff,        gsh2ff/gsHcc2,   gph2ff,        gsHcc2/gsHcc2,     gpHff,
	  gsh1ff/gsHbb2,   gph1ff,        gsh2ff/gsHbb2,   gph2ff,        gsHbb2/gsHbb2,     gpHff,
	  gsh1ff/gsHtt2,   gph1ff,        gsh2ff/gsHtt2,   gph2ff,        gsHtt2/gsHtt2,     gpHff,
	  gsh1ff/gsHmumu2, gph1ff,        gsh2ff/gsHmumu2, gph2ff,        gsHmumu2/gsHmumu2, gpHff,
	  gsh1ff/gsHtata2, gph1ff,        gsh2ff/gsHtata2, gph2ff,        gsHtata2/gsHtata2, gpHff,
	  h1GBGB/HWW2,	   h2GBGB/HWW2,   gHWW2/HWW2,      h1GBGB/HZZ2,   h2GBGB/HZZ2,       gHZZ2/HZZ2,
	  h1GBGB,     	   h2GBGB,        gHAZ2/HAZ2,      h1GBGB/HAA2,   h2GBGB/HAA2,       gHAA2/HAA2,
	  h1GBGB/HGG2,	   h2GBGB/HGG2,   gHGG2/HGG2,      h1GBGB,        h2GBGB,            gHGGZ2,
	  ghihjZ2/ghHZ2,   gh1h2Z2/ghHZ2, ghihjZ2/ghHZ2,   ghihjZ2/ghHZ2, ghihjZ2/ghHZ2,     ghihjZ2/ghHZ2);*/
	  
  
   double Brah1_1,Brah1_2,Brah1_3,Brah2_4,Brah2_5,Brah2_6,BraH_7,BraH_8,BraH_9,BraH_10,Brah2_10,Brah2_11, Brah2_1,Bra2,Bra1,Wt,Brahc_1,Brahc_2,Brahc_3,Brat_1,Brat_2,Brah1_T,Brah2_T,BraH_T;
  
  
  /*Branching ratios of Neutral higgs without Standard Model equivalents */
  /*Brah1_1 = findBr(brah1,"~h1,~h1"); NO PHYSICAL*/
  Brah1_2 = findBr(brah1,"~h2,~h2");
  Brah1_3 = findBr(brah1,"H,H");
  Brah2_4 = findBr(brah2,"~h1,~h1");
  /*Brah2_5 = findBr(brah2,"~h2,~h2"); NO PHYSICAL*/
  Brah2_6 = findBr(brah2,"H,H");
  BraH_7 = findBr(braH,"~h1,~h1");
  BraH_8 = findBr(braH,"~h2,~h2");
  /*BraH_9 = findBr(braH,"H,H"); NO PHYSICAL*/
  BraH_10 = findBr(braH,"~h+,~h-");
  Brah1_T = Brah1_2 + Brah1_3;
  Brah2_T = Brah2_4 + Brah2_6;
  BraH_T = BraH_7 + BraH_8 + BraH_10;
  
  /*Branching ratios of higgs boson of SM decaying into invisible particles BraH_7,BraH_8,BraH_10*/
 
  /*4-Generating the file 2IHDM_BR_H_NP.dat*/
  fprintf(f4,"%i  %.6E  %0.6E  %0.6E  %0.6E  %0.6E  %0.6E  %0.6E  %0.6E  %0.6E \n",K, Brah1_T,Brah2_T,BraH_T,Brah1_2,Brah1_3,Brah2_4,Brah2_6,BraH_7,BraH_8);
  
  /*Width decay and Branching ration of top quark*/
  Wtop = pWidth("t",&brat);
  
  Brat_1 = findBr(brat,"W+,b");
  Brat_2 = findBr(brat,"~h+,b");
  
  /*5-Generating the file 2IHDM_BR_t.dat*/
  fprintf(f5,"%i  %0.6E  %0.6E \n",K,Brat_1,Brat_2);
 
  /*Branching ratios of charged higgs */
  Brahc_1 = findBr(brahc,"c,S");
  Brahc_2 = findBr(brahc,"c,B");
  Brahc_3 = findBr(brahc,"E3,n3");
  
  /*6-Generating the file 2IHDM_Hplus.dat*/
  fprintf(f6,"%i  %0.6E  %0.6E  %0.6E \n",K,Brahc_1,Brahc_2,Brahc_3);
 
       }	 
  
  fclose(f1);
  fclose(f2);
  fclose(f3); 
  fclose(f4); 
  fclose(f5); 
  fclose(f6); 
  fclose(f7);
  
  
#ifdef HIGGSBOUNDS
   if(access(HIGGSBOUNDS "./HiggsBounds",X_OK )) 
   {system(HIGGSBOUNDS "/HiggsBounds LandH effC 3 1 /home/felipe/Tesis/micromegas_3.6.9.2/SM_2IHDM_param/2IHDM_");}
#endif
      
  
/////////////////////////////////////////////////////////////////////////////////
   
#ifdef CLEAN

#endif

  killPlots();
  
 return 0;
}
 
