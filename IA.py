#!/usr/bin/env python3
import math 
n = int(input('How many slots are there? '))
s=[]
p=[]
f=False
l=False
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
def check_sum(s, n):
	sums1, sums2 = [], []
	s1 = s[:len(s) // 2]
	s2 = s[len(s) // 2:]

	for sums, s_ in ((sums1, s1), (sums2, s2)):
		for number in s_:
			for sum_ in sums[:]:
				sums.append(sum_ + number)

			sums.append(number)

	for sum_ in sums1:
		if n - sum_ in sums2:
			return True  

def check_sum_holes(s,n):
	sumzs1, sumzs2 = [], []
	s3 = s[:len(s) // 2]
	s4 = s[len(s) // 2:]

	for sumzs, sz_ in ((sumzs1, s3), (sumzs2, s4)):
		for number in sz_:
			for sumz_ in sumzs[:]:
				sumzs.append(sumz_ + number)

			sumzs.append(number)

	for sumz_ in sumzs1:
		if n==n-k:
			return True
		if n - sumz_ in sumzs2:
			return True	  
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


  