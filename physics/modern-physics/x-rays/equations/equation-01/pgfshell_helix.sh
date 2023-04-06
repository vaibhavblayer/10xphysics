 awk 'BEGIN{ pi=3.14159; N=12*pi; for(i=0;i<=N;i+=0.1) print sin(i),cos(i), i; }' 
