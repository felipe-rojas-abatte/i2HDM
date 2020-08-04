#include <stdio.h>

/*******START***********************/
int main()
{  

  FILE *f1 = fopen("scan_rand_LUX.dat","r"); 
  FILE *f2 = fopen("scan_rand_LUX_HAT_HS_LEP_EWPT_PLANCK.dat","w");
 
fprintf(f2,"%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s\n"," Mh1  ","  Mh2  ","  Mhc   ","  ld345   ", "   ld    ", "    Omega    ","   protonSI ","  Br(H->h1h1) ","  Br(H->h2h2) "," Br(H->h-h+) ","  Width_H   ", "   HB  ", "  HS  ","   R ","  vstab ","   LEP ", "  S    ","   T    ","   LUX  ");
 
  float mh1,mh2,mch,ld345,ld,omega,prot,Brh1,Brh2,Brch,WH,R,massZ,massW,S,T,LUX;
  int K, HB, HS, LEP, vstab;
  
   if ( f1!= NULL )     
   {  fscanf(f1, "%*s %*s %*s %*s %*s %*s %*s %*s %*s %*s %*s %*s %*s %*s %*s %*s %*s %*s %*s");
      for(K = 1; K <= 395548; K++)  
       {fscanf(f1, "%f %f %f %f %f %f %f %f %f %f %f %i %i %f %i %i %f %f %f",&mh1, &mh2, &mch, &ld345, &ld, &omega, &prot, &Brh1, &Brh2, &Brch, &WH, &HB, &HS, &R, &vstab, &LEP, &S, &T, &LUX);
      
/*printf("K=%i  mh1=%.2f  mh2=%.2f  mch=%.2f  ld345=%.3E  ld=%.3E \n",K,mh1,mh2,mch,ld345,ld);*/

   float R_ome,Psi_hat;

R_ome = omega/0.112;
Psi_hat = R_ome*prot;
 
if (omega<0.1226 && omega>0.1172 ){     
	 if(Psi_hat < LUX ){	
		if (HS > 0 && LEP > 0){ 
		 	if(S < 0.14 && S > -0.04 && T < 0.15 && T > 0.01){
  			 
	   
fprintf(f2,"%.2f   %.2f   %.2f   %.3E   %.3E   %.3E    %.3E     %.3E      %.3E     %.3E     %.3E      %i      %i    %.3f    %i     %i    %.3f    %.3f    %.3E \n", mh1, mh2, mch, ld345, ld, omega, prot, Brh1, Brh2, Brch, WH, HB, HS, R, vstab, LEP, S, T, LUX); 


  }}}}}}

  return 0;
}
