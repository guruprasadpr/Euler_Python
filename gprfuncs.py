#!/usr/bin/python 

from math import sqrt

def chkPrime(num):
        flag=0
        if ((num-1)%6!=0 and (num+1)%6!=0): return False
        for j in range(2,int(sqrt(num))+1):
                if num%j==0:
                        flag=1
                        break
        return False if flag else True
  
def genPrime(x):
    count=2
    lprm=[2,3]
    i=5
    if x<=count: return lprm
    while True:
            if count==x: return lprm
            if chkPrime(i): 
                    lprm.append(i)
                    count+=1
            i+=1

def getPrimeBel(x):
    num=0
    lprm=[2,3]
    i=5
    while True:
            if chkPrime(i): 
                    if i>x: return lprm
                    lprm.append(i)
            i+=1

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

def primeFacPow(x):
   l=[]
   i=2
   y=x
   while True:
           if (x==1 or i>int(sqrt(x))+1): break
           if (x%i==0):
                   l.append(i)
                   x=x/i
                   i-=1
           i+=1
   if x!=1: l.append(x)
   return  l

def getDivisors(x):
    l1=[]
    for i in range(1,x/2+1):
            if x%i==0: l1.append(i)
    l1.append(x)
    return l1


def sumofdigits(x):
   return sum(map(int,list(str(x))))

