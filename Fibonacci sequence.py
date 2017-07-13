# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 11:32:30 2017

@author: yangjinyue
"""

def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))
        
nterms = int(input("N="))

if nterms <= 0:
    print("wrong number")
else:
    print("fibo:")
    for i in range(nterms):
        print(recur_fibo(i))
        