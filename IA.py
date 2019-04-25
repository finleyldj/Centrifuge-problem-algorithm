#!/usr/bin/env python3
import math 
n = int(input('How many slots are there? '))
s=n
# A function to print all prime factors of  
# a given number n 
def primeFactors(n):  
    # print the number of two's that divide n 
    while n % 2 == 0: 
       yield (int(2)), 
       n = n / 2
          
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(math.sqrt(n))+1,2): 
          
        # while i divides n , print i ad divide n 
        while n % i== 0: 
            yield(int(i)), 
            n = n / i 
              
    # Condition if n is a prime 
    # number greater than 2 
    if n > 2: 
        yied (int(n))
	
for n in primeFactors(n):
	print(n)
try:
	pf_gen=primeFactors(n)
	next (pf_gen)
except TypeError:
	pass
#Function which prints all of the possible sums of the prime factors of n        
#def sumofprimes(n):
	#while n<=s:
		
#k= int(input('How many test tubes do you have?'))
#if k==n:
	#print ('This is balanced!')
        
