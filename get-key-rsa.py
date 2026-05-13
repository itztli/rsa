#!/usr/bin/env python3
import time

A = 1103515245
M = 32768
C = 12345

def getBigNumber(x, maximum):
    #for i in range(20):
    x = (A*x + C) % M
    return x % maximum

def isPrime(a):
    i = 2
    while i < a:
        if (a % i) == 0:
            return False
        i = i + 1
    return True

def gcd(a,b):
    #i = 2
    i = min(a,b)
    while i >= 2:
        if ((a % i) == 0) and ((b % i) == 0):
            return i
        i = i - 1
    return 1

def test_e(e,d,p1q1):
    #print(e*d, p1q1)
    if ( (e*d) % p1q1) == 1:
        return True
    return False



x0 = int(round(time.time() * 1000)) #int(time.time()) #time.time_ns()
#print(x0)
small = int(M/2)
d = x0
e = 1
print("Computing...")
while e == 1:
    p = getBigNumber(d, small)
    while not isPrime(p):    
        p = getBigNumber(p, small)
    #print("p",p)

    q = getBigNumber(p, small)
    while not isPrime(q):    
        q = getBigNumber(q, small)
    #print("q",q)

    n = p*q
    #print("n",n)

    maxpq = max([p,q])

    d = getBigNumber(q,M)

    while True:
        while not isPrime(d):    
            d = getBigNumber(d, M)
        if d > maxpq:
            break
        else:
            d = getBigNumber(d, M)
    #print("d",d)

    #d = getBigNumber(q,M)

    phi_n = (p-1)*(q-1)

    #while not MCD(d,p1q1):
    #    d = getBigNumber(d,M)
    
    #print("phi(n)=",phi_n, "d=",d)
    e = gcd(phi_n, d)
    #print("e",e)
    
    #e = getBigNumber(d,M)
    #while not test_e(e,d,p1q1):
    #    e = getBigNumber(e, M)
    #    #print(e)
    #print("e",e)

print(e,d,n)

#Maximo comun divisor
#d = 31
#phi = (p-1)*(q-1) = 6*10 = 60


