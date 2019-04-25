#!/usr/bin/env python3
import math 
n = int(input('How many slots are there?'))
s=n
# A function to return all prime factors of  
# a given number n 
def primeFactors(n): 
      
    # return the number of two's that divide n 
    while n % 2 == 0: 
        return (int(2)), 
        n = n / 2
          
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(math.sqrt(n))+1,2): 
          
        # while i divides n , return i ad divide n 
        while n % i== 0: 
            return(int(i)), 
            n = n / i 
              
    # Condition if n is a prime 
    # number greater than 2 
    if n > 2: 
        return (int(n))
def sumofprimes(n):
	while n<=s:
		
k= int(input('How many test tubes do you have?'))
if k==n:
	print ('This is balanced!')
        
