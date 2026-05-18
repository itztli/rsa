#!/usr/bin/env python3
import math 

p = 47
q = 59

n = p*q

d = 157  # PRIVATE KEY
e = 17   # PUBLIC KEY

M = input("Enter crypted text: ")

with open(".rsa/private.key", "r", encoding="utf-8") as f:
    lineas = f.readlines() # lista de líneas

dstr, nstr = lineas[0].split('\t')

d = int(dstr)
n = int(nstr)

print(d,n)
#d = int(input("Private Key: "))
#n = int(input("Module n: "))

#M = "ITS ALL GREEK TO ME"

#print(M)
encode = {' ': '00'}

encode.update({chr(65 + i): str(i + 1).zfill(2) for i in range(26)})

#N = len(M)

#Menc = []
#for i in range(int(N/2)):    
#    c = encode[M[2*i]] + encode[M[2*i+1]]
#    #print(c)
#    Menc.append(c)
#if (N % 2 == 1):
#    c = encode[M[N-1]] + "00"
#    Menc.append(c)
#    #print(c)
#
#print(Menc)
#C=[]
#for i in range(len(Menc)):
#    m = int(Menc[i])
#    c = pow(m,e,n)
#    #print(str(m)+"^"+str(e)+"%"+str(n)+"="+str(c))
#    #c = multi % n 
#    C.append(str(c).zfill(4))
#    #print(encode[M[i]], pow(encode[M[i]],e))
#    
C = M.split(" ")
print(C)

decode = {v: k for k, v in encode.items()}
#for c in C:
#    M1 = c[0:2]
#    M2 = c[2:4]
#    print(decode[M1]+decode[M2])

for i in range(len(C)):
    Mdec = str(pow(int(C[i]), d, n)).zfill(4)
    M1 = Mdec[0:2]
    M2 = Mdec[2:4]
    print(decode[M1]+decode[M2],end="")
print("")
