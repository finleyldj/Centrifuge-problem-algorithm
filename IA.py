#!/usr/bin/env python3
import math 
n = int(input('How many slots are there? '))
s=[]
# A function to print the prime factors of n 
def primeFactors(n):
	i=1
	while(i<=n):
	    k=0
	    if(n%i==0):
	        j=1
	        while(j<=i):
	            if(i%j==0):
	                k=k+1
	            j=j+1
	        if(k==2):
	            s.append(i)
	    i=i+1	
primeFactors(n)
for x in range(len(s)):
	print (s[x])       
