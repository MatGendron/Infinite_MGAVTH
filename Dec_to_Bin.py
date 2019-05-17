def Dec_to_Bin(n):
    tab_bin=[]
    i=n
    while (i>1):
        i=i//2
        tab_bin.append(i%2)
    tab_bin.reverse()
    return tab_bin
