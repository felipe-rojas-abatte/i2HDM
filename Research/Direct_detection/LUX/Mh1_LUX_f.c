#include <stdio.h>

/*******START***********************/
int main()
{  
  FILE *f1 = fopen("../scan_rand_1.5TeV.dat","r"); 
  FILE *f2 = fopen("fLUX_scan_rand_1.5TeV.dat","r");
  FILE *f3 = fopen("../scan_rand_1.5TeV_LUX.dat","w");
 
fprintf(f3,"%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s \n", 
 " Mh1  ","  Mh2  ","  Mhc   ","  ld345    ", "   ld    ", "   Omega  ","    protonSI ","   Br(H->h1h1) ","  Br(H->h2h2) "," Br(H->h-h+) ","  Width_H    ", "  HB  ", "  HS  ","   R  "," v_stab ","  LEP ", "  S    ","   T  ","   LUX  ");
 
  float mdm,mh1,mh2,mhc,ld345,ld,omega,protSI,brh1,brh2,brhc,WH,R,S,T,fLUX;

  int K,HB,HS,v_stab,LEP;
  
   if ( f1!= NULL )     
   {  fscanf(f1, "%*s %*s %*s %*s %*s %*s %*s %*s %*s %*s %*s %*s %*s %*s %*s %*s %*s %*s");
      fscanf(f2, "%*s");
       for(K = 1; K <= 585803; K++)  
       {fscanf(f1, "%f %f %f %f %f %f %f %f %f %f %f %i %i %f %i %i %f %f", &mh1, &mh2, &mhc, &ld345, &ld, &omega, &protSI, &brh1, &brh2, &brhc, &WH, &HB, &HS, &R, &v_stab, &LEP, &S, &T);
        fscanf(f2, "%f ", &fLUX);

      
 fprintf(f3,"%.2f   %.2f   %.2f   %.3E   %.3E   %.3E    %.3E     %.3E      %.3E     %.3E     %.3E      %i      %i    %.3f    %i     %i    %.3f    %.3f    %.3E \n", mh1, mh2, mhc, ld345, ld, omega, protSI, brh1, brh2, brhc, WH, HB, HS, R, v_stab, LEP, S, T, fLUX);

}}

  return 0;
}
