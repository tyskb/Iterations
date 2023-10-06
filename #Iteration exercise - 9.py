#Iteration exercise - 9 

A = int(input("Enter the first positive integer: "))
B = int(input("Enter the second positive integer: "))
larger_num = max(A, B)
print(f"{A} and {B} shares: ")

for i in range (1, larger_num):
    if A % i == 0 and B % i == 0:
        print(i)
