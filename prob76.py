#!/usr/bin/python 

d1={}
d1[1]=1
d1[2]=1
d1[3]=2

for num in range(4,10):
    sum=0
    print 'For : ', num
    for i,j in zip(range(1,num), range(num-1,0,-1)):
            if i>j: break
            sum+=d1[i]*d1[j]
            if d1[i]+d1[j]==2: sum+=1
            print i,j
    d1[num]=sum

print d1
