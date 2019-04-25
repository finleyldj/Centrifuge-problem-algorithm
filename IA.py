#!/usr/bin/env python3
import math 
n = int(input('How many slots are there? '))
s=[]
s.append(n)
# A function to print the prime factors of n 
def primeFactors(s):  
    # reducing n to an odd number 
    while n % 2 == 0: 
       return (int(2)), 
       s = n / 2
           
    for i in range(3,int(math.sqrt(n))+1,2): 
          
        # adding values of n to set s
        while n % i== 0: 
             c=int(n/i)
             s.append(c)        
    # Where n is a prime 
    # > 2
    if n > 2: 
        pass	
primeFactors(n)
print (s)
        
