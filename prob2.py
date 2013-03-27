#!/usr/bin/python 

def evenV(x):
 return True if (x%2==0) else False

fib=[1,2]
[fib.append(fib[-2]+fib[-1]) for i in range(1,50) if (fib[-2]+fib[-1])<4000000]

print sum(filter(evenV,fib))
