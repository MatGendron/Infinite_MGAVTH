#!/usr/bin/python3

##Coding the representation of a and b in each entity
def binaryArray(x):
    b=bin(x)
    res=[]
    i=4
    while i!=0:
        res.append(b%2)
        b=b//2
        i-=1


list_theta=[]
for i in range(16):
    list_theta.append(binaryArray(i))

print(list_theta)