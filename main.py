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

##Function that builds an array reprensenting the binary corresponding to a given decimal
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

transpo_base=transpo_of_size(4)

##First developped function that does the calculus using the average of all Pij, wrong function (?)
def spin_avg_error(base):
    ##Builds the matrix sum of Pij according to given base of transpositions
    Ssquare_matrix=zero_matrix()
    for theta_in in list_theta:
        for transpo in base:
            theta_out = permute(theta_in,transpo)
            Ssquare_matrix[bin_to_dec(theta_in)][bin_to_dec(theta_out)]+=1
    S = np.array(Ssquare_matrix)
    ##Getting the eigenvectors of the sum matrix
    D,P = np.linalg.eig(S)
    ##Building the necessary matrix and calculating the average spins
    psi=P[:,0]
    psi_alt = np.reshape(psi,(16,1))
    Pavg = np.true_divide(S,len(base))
    res = np.dot(psi,np.dot(Pavg,psi_alt))
    return res[0]

print("Values for average Pij [wrong function it just shows a first attempt at solving the problem]:")
print("For S²:")
print(spin_avg_error(transpo_base))
print("\nFor H with linear molecule:")
print(spin_avg_error([[1,2],[2,3],[3,4]]))
print("\nFor H with squared molecule:")
print(spin_avg_error([[1,2],[2,3],[3,4],[1,4]]))

##Function that gives the Pij matrix for a given transposition
def pij_matrix(transpo):
    pij=zero_matrix()
    for theta_in in list_theta:
        theta_out=permute(theta_in,transpo)
        pij[bin_to_dec(theta_in)][bin_to_dec(theta_out)]+=1
    return np.array(pij)

##Function that calculates the spin for each transpotion in the given base
def spin(base):
    ##Builds the matrix sum of Pij according to given base of transpositions
    Ssquare_matrix=zero_matrix()
    for theta_in in list_theta:
        for transpo in base:
            theta_out = permute(theta_in,transpo)
            Ssquare_matrix[bin_to_dec(theta_in)][bin_to_dec(theta_out)]+=1
    S = np.array(Ssquare_matrix)
    ##Getting the eigenvectors of the sum matrix
    D,P = np.linalg.eig(S)
    ##Building the necessary matrix and calculating the spin for each Pij
    min = D[0]
    x=0
    for i in range(len(D)):
        if D[i]<min:
            min=D[i]
            x=i
    psi=P[:,x]
    psi_alt = np.reshape(psi,(16,1))
    for transpo in base:
        pij = pij_matrix(transpo)
        res = np.dot(psi,np.dot(pij,psi_alt))
        print("\nTransposition: " + str(transpo))
        print("Result: "+str(res[0]))
    return

print("---------------\nValues with separated Pij:")
print("For S²:")
spin(transpo_base)
print("\nFor H with linear molecule:")
spin([[1,2],[2,3],[3,4]])
print("\nFor H with squared molecule:")
spin([[1,2],[2,3],[3,4],[1,4]])

new_theta=[]
for theta in list_theta:
    x=0
    for i in theta:
        x+=i
    if x==2:
        new_theta+=[theta,]

def zero_matrix_6():
    res=[0,0,0,0,0,0]
    for i in range(6):
        res[i]=[0,0,0,0,0,0]
    return res

def theta_indice(theta_in):
    for i in range(len(new_theta)):
        if new_theta[i]==theta_in:
            return i
    return (-1)

##Function that gives the Pij matrix for a given transposition
def pij_matrix_6(transpo):
    pij=zero_matrix_6()
    for theta_in in list_theta:
        theta_out=permute(theta_in,transpo)
        pij[theta_indice(theta_in)][theta_indice(theta_out)]+=1
    return np.array(pij)

##Function that calculates the spin for each transpotion in the given base
def spin_2(base):
    ##Builds the matrix sum of Pij according to given base of transpositions
    Ssquare_matrix=zero_matrix_6()
    for theta_in in new_theta:
        for transpo in base:
            theta_out = permute(theta_in,transpo)
            Ssquare_matrix[theta_indice(theta_in)][theta_indice(theta_out)]+=1
    S = np.array(Ssquare_matrix)
    print(S)
    ##Getting the eigenvectors of the sum matrix
    D,P = np.linalg.eig(S)
    ##Building the necessary matrix and calculating the spin for each Pij
    min = D[0]
    x=0
    for i in range(len(D)):
        if D[i]<min:
            min=D[i]
            x=i
    psi=P[:,x]
    psi_alt = np.reshape(psi,(6,1))
    for transpo in base:
        pij = pij_matrix_6(transpo)
        res = np.dot(psi,np.dot(pij,psi_alt))
        print("\nTransposition: " + str(transpo))
        print("Result: "+str(res[0]))
    return

print("---------------\nValues with separated Pij:")
print("For S²:")
spin_2(transpo_base)
print("\nFor H with linear molecule:")
spin_2([[1,2],[2,3],[3,4]])
print("\nFor H with squared molecule:")
spin_2([[1,2],[2,3],[3,4],[1,4]])