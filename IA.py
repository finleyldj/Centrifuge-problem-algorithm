#!/usr/bin/env python3
import math 
n = int(input('How many slots are there? '))
s=[]
p=[]
f=[]
# A function to print the prime factors of n 
def prime_factors(n):
	i = 2
	while i * i <= n:
		if n % i:
			i += 1
		else:
			n //= i
			s.append(i)
	if n > 1:
		s.append(n)
	return s
prime_factors(n)
for x in range(len(s)):
	print (s[x])       
#Function which prints all of the possible sums of the prime factors of n        
k=int(input('How many test tubes do you have? '))
#lines 23-57 have been adapted from source code by stack overflow user "Jonathan"
def check_sum(s, k):
	g = 1
	c=1
	t=1
	z=1
	l=1
	while c <=len(s):
		while g < k:
			while t < k:
				t=s[c]*g
				f.append(t)
	while c <= len(s):
		while z<(len(s)-1):
			while g < k:
				while t < k:
					t=s[c]*g+s[c+z]
					f.append(t)
	while c<= len(s):
		while z<(len(s)-1):
			while g < k:
				while t < k:
					while l<g:		
						t=s[c]*g+s[c+z]*l
						f.append(t)
	if k in s:
		return True
	else:
		return False				

def check_sum_holes(s,k):
	g = 1
	c=1
	t=1
	z=1
	l=1
	while c<=len(s):
		while g < (n-k):
			while t < (n-k):
				t=s[c]*g
				f.append(t)
	while c <= len(s):
		while z<(len(s)-1):
			while g < (n-k):
				while t < (n-k):
					t=s[c]*g+s[c+z]
					f.append(t)
	while c<= len(s):
		while z<(len(s)-1):
			while g < (n-k):
				while t < (n-k):
					while l<g:		
						t=s[c]*g+s[c+z]*l
						f.append(t)
	if n-k in s:
		return True
	else:
		return False	

check_sum(s,k)
check_sum_holes(s,k)
def check_balance (s,k):
	check_sum(s,k)
	check_sum_holes(s,k)
	if check_sum(s,k) and check_sum_holes(s,k):
		print("This is a balanced configuration")
	else:
		print("You cannot balance this centrifuge with " + str(k) + " test tubes")
check_balance(s,k)		


  