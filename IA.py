#!/usr/bin/env python3
import math 
n = int(input('How many slots are there? '))
s=[]
k=[]
# A function to print the prime factors of n 
def primeFactors(n):
	i=1
	while(i<=n):
	    k=0
	    if(n%i==0):
	        j=1
	        while(j<=i):
	            if(i%j==0):
	                q=q+1
	            j=j+1
	        ifqk==2):
	            s.append(i)
	    i=i+1	
primeFactors(n)
for x in range(len(s)):
	print (s[x])       
#Function which prints all of the possible sums of the prime factors of n        
def primeSum(n):
	g=1
	while g<=len(s):
		d=s[(len(s))-(len(s)-g)]
		k.append(d)
