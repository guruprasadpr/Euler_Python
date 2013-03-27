#!/usr/bin/python 

def Pal(x):
   val=str(x)
   rval=val[::-1]
   return True if val==rval else False


x=range(101,1000)
y=range(101,1000)

f=[i*j for i in x for j in y if(Pal(i*j))]
print max(f)
