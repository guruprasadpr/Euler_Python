#!/usr/bin/python 


with open('prob13.txt','r') as f:
  l1=[]
  for line in f:
          l1.append(line.strip())

s=0
l2=[]
for i in range(49,-1,-1):
  s=s/10
  for num in l1: s+=int(num[i])
  l2.insert(0,s%10)

l2.insert(0,s/10)
print ''.join(map(str,l2[0:9]))
#print sum(map(int,l1))
