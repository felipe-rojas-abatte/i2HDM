#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int main()
{   
/* Create file with information to be stored (Mh1, ld345_max, cs) */ 
 FILE *fdata = fopen("cs_13TeV_pp_h1h1j_maxld345.dat","w");
 fprintf(fdata,"%s %s %s \n"," Mh1 ","  ld345   ","   cs_(fb)  ");

/* Open file with numerical ld345_max */
FILE *num_ld345_max = fopen("ld345_max_interpolation.dat","r");

char name[100];
char batch[100];

strcpy(name, "pp_h1h1j_cc" );
strcpy(batch, "./calchep_batch pp_h1h1j_cc" );
 
int energy,Mh1;
float ld345_max,K,ld345;

energy = 6500;  /* Energy of each beam in GeV*/



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
PI = 3.14159265359;
num= 4*PI*ee*ee*MH*Br*GSM;
den= (1-Br)*SW*SW*MW*MW*sqrt(1-4*(mh1/MH)*(mh1/MH));
result = sqrt(num/den);
return result;
}

     for(K = 62; K <= 200; K=K+1)  {

/* Genero el archivo BATCH con la información del proceso*/
 FILE *f10 = fopen(name,"w"); 

if(K<=62.5){ 
  	ld345_max = ld345_flow(K);
	printf("\n For Mh1 = %.1f, lambda_345 max = %.6f \n ", K, ld345_max);}

else{   do{fscanf(num_ld345_max,"%i  %f ",&Mh1, &ld345);} while(Mh1<K);
	   ld345_max = ld345;
	   printf("\n Mh1 = %i, K = %.1f \n",Mh1,K);
	   printf("\n For Mh1 = %.1f, lambda_345 max = %.6f \n ", K, ld345_max);}
	

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
fprintf(f10,"Parameter: Mh1=%.1f \n", K);
fprintf(f10,"Parameter: Mh2=%.1f \n", K);
fprintf(f10,"Parameter: Mhc=200\n");
fprintf(f10,"Parameter: ld=1\n");
fprintf(f10,"Parameter: ld345=%.6f \n",ld345_max);
fprintf(f10,"alpha Q : M34\n");
fprintf(f10,"Cut parameter: T(jet)\n");
fprintf(f10,"Cut invert: False\n");
fprintf(f10,"Cut min: 100\n");
fprintf(f10,"Kinematics : 12 -> 34, 5\n");
fprintf(f10,"Kinematics : 34 -> 3 , 4\n");
fprintf(f10,"Regularization momentum:1: 34\n");
fprintf(f10,"Regularization mass:1: MH\n");
fprintf(f10,"Regularization width:1: wH\n");
fprintf(f10,"Regularization power:1: 2\n");
fprintf(f10,"Number of events (per run step): 1\n");
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

/* Ejecuto el archivo BATCH */

printf("\n ================================ \n Ejecutando archivo batch n=%.1f \n ================================ \n\n",K);
printf("  Mh1 = %.1f  ld345 = %.6f \n",K,ld345_max);

system(batch);


/*** Elimino la parte que no me gusta del archivo numerical.txt ****/

FILE *oldFile = fopen("/home/felipe/Documents/Programas/micromegas_4.1.8/2IHDM_fixed/work/html/numerical.txt", "r");
FILE *newFile = fopen("/home/felipe/Documents/Programas/micromegas_4.1.8/2IHDM_fixed/work/new_numerical.txt", "w");

int lineNumber;
int len;
char line[4096],line1[4096];
int todoNumber;
lineNumber=0;

/*Debemos seleccionar la cantidad de líneas que deseamos eliminar del archivo numerical */
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
      fprintf(fdata," %.1f    %.6f    %.4E \n",K,ld345_max,sig);        

fclose(f2);

remove("/home/felipe/Documents/Programas/micromegas_4.1.8/2IHDM_fixed/work/new_numerical.txt");

}

return 0; 
}

 
