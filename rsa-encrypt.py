#!/usr/bin/env python3
import math 

p = 47
q = 59

n = p*q

d = 157
e = 17

#e = int(input("Public Key: "))
#n = int(input("Module n: "))

public_key = input("To: ")

with open(".rsa/"+public_key+".key", "r", encoding="utf-8") as f:
    lineas = f.readlines() # lista de líneas

estr, nstr = lineas[0].split('\t')

e = int(estr)
n = int(nstr)

print(d,n)

M = input("Enter some text: ")

#M = "ITS ALL GREEK TO ME"

print(M)
encode = {' ': '00'}

encode.update({chr(65 + i): str(i + 1).zfill(2) for i in range(26)})

N = len(M)

Menc = []
for i in range(int(N/2)):    
    c = encode[M[2*i]] + encode[M[2*i+1]]
    #print(c)
    Menc.append(c)
if (N % 2 == 1):
    c = encode[M[N-1]] + "00"
    Menc.append(c)
    #print(c)

#print(Menc)
C=[]
for i in range(len(Menc)):
    m = int(Menc[i])
    c = pow(m,e,n)
    #print(str(m)+"^"+str(e)+"%"+str(n)+"="+str(c))
    #c = multi % n 
    C.append(str(c).zfill(4))
    #print(encode[M[i]], pow(encode[M[i]],e))
    
print(*C)

