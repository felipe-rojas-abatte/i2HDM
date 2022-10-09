/*====== Modules ===============
/*====== Modules ===============
   Keys to switch on 
   various modules of micrOMEGAs  
================================*/
      
/*#define MASSES_INFO      
  /* Display information about mass spectrum  */

#define HIGGSBOUNDS "../../HiggsBounds-4.2.0"
  
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
   
   

/**** Create files ****/   
 FILE *f1 = fopen("2IHDM_new_MH_GammaTot.dat","w");
 FILE *f2 = fopen("2IHDM_new_effC.dat","w");
 FILE *f3 = fopen("2IHDM_new_BR_H_NP.dat","w");
 
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
    FILE *f4 = fopen("Benchmarks.txt", "r");
    
    float massh1,massh2,massCH;  
    float ld345,ld;    
    for(K = 1; K <= 13; K++)  
       {fscanf(f4, "%f %f %f %f %f", &massh1, &massh2, &massCH, &ld345, &ld);
       printf("K = %i  massh1 = %.1f  massh2 = %.1f  massCH = %.1f  ld345 = %.3f  ld = %.2f \n ",K,massh1,massh2,massCH,ld345,ld);
    
  ///////////////////////////////////////////////////  
  
    
     assignValW("Mh1",massh1); 
     assignValW("Mh2",massh2); 
     assignValW("Mhc",massCH);
     assignValW("ld345",ld345);
     assignValW("ld",ld);

     err=sortOddParticles(cdmName);

     if(err) { printf("Can't calculate %s\n",cdmName); return 0; }
     
////////////////////////////////////////////////////////////////////
#ifdef MASSES_INFO
{
  printf("\n=== MASSES OF HIGG AND ODD PARTICLES: ===\n");
  printHiggs(stdout);
  printMasses(stdout,1);
      
}
#endif


/*Generating files for effC Higgs Bounds*/

  double WH,Wtop;
  txtList braH,brat;
 
  double ee,sinW,cosW,massH,massZ,massW,massS,massC,massB,massT,massmu,massta,gHZZ2,gHWW2,ghHZ2,gsHcc2,gsHtt2,gsHss2, gsHbb2,gsHmumu2,gsHtata2,gsHff,gpHff,ldA,ldG,HWW2,HZZ2,HAA2,HGG2,HAZ2,HGGZ2,gHAA2,gHGG2,gHGGZ2,gHAZ2,ghihjZ2;  
   
  /*Parameters of the model*/
   findVal("EE",&ee);
   findVal("MH",&massH);
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
  
  /*Mass and width decay of neutral higgs*/
   WH = pWidth("H",&braH);
  
  /*1-Generating the file 2IHDM_MH_GammaTot.dat)*/
  fprintf(f1,"%i   %.6E   %.6E \n",K,massH,WH);
  
  /*Effective scalar coupling (squered) Higgs-fermions in the 2IHDM */ 
   gsHss2 = ((ee*massS)/(2*sinW*massW))*((ee*massS)/(2*sinW*massW));
   gsHcc2 = ((ee*massC)/(2*sinW*massW))*((ee*massC)/(2*sinW*massW));
   gsHtt2 = ((ee*massT)/(2*sinW*massW))*((ee*massT)/(2*sinW*massW));
   gsHbb2 = ((ee*massB)/(2*sinW*massW))*((ee*massB)/(2*sinW*massW));
   gsHmumu2 = ((ee*massmu)/(2*sinW*massW))*((ee*massmu)/(2*sinW*massW));
   gsHtata2 = ((ee*massta)/(2*sinW*massW))*((ee*massta)/(2*sinW*massW));
     
     
 /*There is not effective pseudo-scalar couplings Higgs-fermions in the 2IHDM*/  
   gpHff = 0; 
   
 /*Efective coupling (squered) Higgs-Gauge Bosons in the 2IHDM*/ 
   gHZZ2 = ((ee*massZ*massZ)/(sinW*massW))*((ee*massZ*massZ)/(sinW*massW));/*findBr(bra3,"Z,Z")*/
   gHWW2 = (ee*massW/sinW)*(ee*massW/sinW);/*findBr(bra3,"W+,W-")*/
   gHAA2 = findBr(braH,"A,A");/*((8*ldA*massW*sinW)/(ee*vv))*((8*ldA*massW*sinW)/(ee*vv));*/
   gHGG2 = findBr(braH,"G,G");/*((8*ldG*massW*sinW)/(ee*vv))*((8*ldG*massW*sinW)/(ee*vv));*/
   gHAZ2 = findBr(braH,"A,Z");
   gHGGZ2 = 0;
   ghihjZ2 = 0;
      
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

  /*2-Generating the file effC.dat*/
  fprintf(f2,"%i        %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  %.6E  \n",K, gsHss2/gsHss2, gpHff, gsHcc2/gsHcc2, gpHff, gsHbb2/gsHbb2, gpHff, gsHtt2/gsHtt2, gpHff, gsHmumu2/gsHmumu2, gpHff, gsHtata2/gsHtata2, gpHff, gHWW2/HWW2, gHZZ2/HZZ2, gHAZ2/HAZ2, gHAA2/HAA2, gHGG2/HGG2, gHGGZ2, ghihjZ2/ghHZ2 );
	  
  
   double BraH_1,BraH_2,BraH_3,BraH_T,Brat_1,Brat_2;
    
  /*Branching ratios of Neutral higgs without Standard Model equivalents */
  BraH_1 = findBr(braH,"~h1,~h1");
  BraH_2 = findBr(braH,"~h2,~h2");
  BraH_3 = findBr(braH,"~h+,~h-");
  BraH_T = BraH_1 + BraH_2 + BraH_3;
  
  /*Branching ratios of higgs boson of SM decaying into invisible particles BraH_7,BraH_8,BraH_10*/
 
  /*3-Generating the file 2IHDM_BR_H_NP.dat*/
  fprintf(f3,"%i        %.6E \n",K, BraH_T);

  }
  
  fclose(f1);
  fclose(f2);
  fclose(f3); 
    
  
#ifdef HIGGSBOUNDS
   if(access(HIGGSBOUNDS "./HiggsBounds",X_OK )) 
   {system(HIGGSBOUNDS "/HiggsBounds LandH effC 1 0 /home/felipe/Tesis/micromegas_3.6.9.2/SM_2IHDM_param/2IHDM_new_");}
#endif
    

/////////////////////////////////////////////////////////////////////////////////
   
#ifdef CLEAN

#endif

  killPlots();
  
 return 0;
}
 
