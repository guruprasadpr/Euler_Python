#!/usr/bin/python 

def primFac(x):
   l=[]
   i=2
   y=x
   while True:
           if (x==1 or i>y/2): break
           if (x%i==0): 
                   l.append(i)
                   x=x/i
           i+=1
   l.append(x)
   return  l

print primFac(600851475143)
