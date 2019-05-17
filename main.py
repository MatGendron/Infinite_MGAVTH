#!/usr/bin/python3

##Function that builds an array reprensenting the binary corresponding to a given decimal.
def Dec_to_Bin(n):
    tab_bin=[0,0,0,0]
    k=0
    i=n
    while (i>=1):

        tab_bin[k]=i%2
        i=i//2
        k+=1
    tab_bin.reverse()
    return tab_bin

##Function that permutes two given values in an array
def permute(theta,permutation):
    a,b = permutation
    TMP=theta[a-1]
    theta[a-1]=theta[b-1]
    theta[b-1]=TMP
    return theta
    
def transpo_of_size(n):
    tab=[]
    for i in range (1,n):
        for j in range (n,i,-1):
            tab.append([i,j])
    return tab

##Function that takes an array of binaries and gives the corresponding decimal

##Function that builds a 16x16 array of 0s 

list_theta=[]
for i in range(16):
    list_theta.append(Dec_to_Bin(i))

print(list_theta)

