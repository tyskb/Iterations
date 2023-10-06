#Iteration exercise - 10


#Prime Factor Finder
#The prime factors of 13195 are 5, 7, 13, 29. Write a program that can find the prime factors of a number. 
#Determine the largest prime factor for the number 600851475143. 

num = 600851475143
largest = 0

while num % 2 == 0:
    num //= 2
    largest = max(largest, 2)


if num % 2 != 0:
    num 