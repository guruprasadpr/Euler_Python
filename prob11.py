#!/usr/bin/python 

def maxgridProd(l1):
   res=[]
   res=[l1[row][i]*l1[row][i+1]*l1[row][i+2]*l1[row][i+3] for row in range(20) for i in range(17) ]
   res.extend([l1[row][col]*l1[row+1][col]*l1[row+2][col]*l1[row+3][col] for row in range(17) for col in range(20) ])
   res.extend([l1[row][col]*l1[row+1][col+1]*l1[row+2][col+2]*l1[row+3][col+3] for row in range(17) for col in range(17) ])
   res.extend([(l1[row][col]*l1[row+1][col-1]*l1[row+2][col-2]*l1[row+3][col-3]) for row in range(17) for col in range(19,2,-1) ])
   return max(res)



with open('prob11.txt' ,'r') as f:
   l1=[]
   for line in f:
           l1.append(map(int,line.strip().split(' ')))
   print maxgridProd(l1)

