#!/usr/bin/python3

import numpy as np

##Function that prints a matrix
def print_matrix(M):
    for l in M:
        print("[", end="")
        for i in l:
            if i != 0:
                print("%.3f" % i, end=" | ")
            else:
                print("     ", end = " | ")
        print("]")

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
##theta is the array where the permutation occurs
##permutation is the given index whose values are going to be permuted
def permute(theta,permutation):
    new_theta = theta.copy()
    a,b = permutation
    tmp=new_theta[a-1]
    new_theta[a-1]=new_theta[b-1]
    new_theta[b-1]=tmp
    return new_theta

#Function that returns all the possible permutation in an array of size n
def transpo_of_size(n):
    tab=[]
    for i in range (1,n):
        for j in range (n,i,-1):
            tab.append([i,j])
    return tab

##Function that takes an array of binaries and gives the corresponding decimal
def bin_to_dec(b):
    res=0
    temp=8
    for i in b:
        res+=(i*temp)
        temp=temp//2
    return res

##Function that builds a 16x16 array of 0s
def zero_matrix():
    res=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(16):
        res[i]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    return res

list_theta=[]
for i in range(16):
    list_theta.append(Dec_to_Bin(i))

Ssquare_matrix=zero_matrix()

transpo_base=transpo_of_size(4)

for theta_in in list_theta:
    for transpo in transpo_base:
        theta_out = permute(theta_in,transpo)
        Ssquare_matrix[bin_to_dec(theta_in)][bin_to_dec(theta_out)]+=1

S = np.array(Ssquare_matrix)

D,P = np.linalg.eig(S)

##print(D)

temp = np.diag(D)

print_matrix(temp)
