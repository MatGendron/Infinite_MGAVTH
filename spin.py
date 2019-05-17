#!/usr/bin/python3

##Coding the representation of a and b in each entity
def binaryArray(x):
    if x==0:
        return [0,0,0,0]
    else:
        res=[]
        while i!=0:
            res.append(i%2)
            i//2
        return res.reverse()

list_theta=[]
for i in range(16):
    list_theta.append(binaryArray(i))

print(list_theta)