#!/usr/bin/env python3
import time

A = 1103515245
M = 32768
C = 12345

def getBigNumber(x):
    #for i in range(20):
    x = (A*x + C) % M
    return x

def isPrime(a):
    i = 2
    while i < a:
        if (a % i) == 0:
            return False
        i = i + 1
    return True

def MCD(a,b):
    i = 2
    stop = min(a,b)
    while i <= stop:
        if ((a % i) == 0) and ((b % i) == 0):
            return True
        i = i + 1
    return False

def test_e(e,d,p1q1):
    print(e*d, p1q1)
    if ( (e*d) % p1q1) == 1:
        return True
    return False
        
x0 = int(time.time()) #time.time_ns()
#print(x0)
p = getBigNumber(x0)
while not isPrime(p):    
    p = getBigNumber(p)
print("p",p)

q = getBigNumber(p)
while not isPrime(q):    
    q = getBigNumber(q)
print("q",q)

n = p*q
print("n",n)

d = getBigNumber(q)
p1q1 = (p-1)*(q-1)

while not MCD(d,p1q1):
    d = getBigNumber(d)
print("d",d)

e = getBigNumber(d)

while not test_e(e,d,p1q1):
    e = getBigNumber(e)
    print(e)
print("e",e)

#Maximo comun divisor
#d = 31
#phi = (p-1)*(q-1) = 6*10 = 60


