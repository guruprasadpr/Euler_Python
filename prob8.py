#!/usr/bin/python 
from operator import mul

def getMaxProd(x):
   i,j=0,5
   l1=[]
   while True:
           if j==len(x)+1: break
           num=x[i:j]
           i,j=i+1,j+1
           if (num.find('0')!=-1): continue
           l1.append(reduce(mul,map(int,list(num)),1))

   return max(l1)

  
with open('file.txt','r') as f:
    x=f.read().replace('\n','');
    print getMaxProd(x)
