#Iteration exercise - 3

user_num = int(input("Enter an integar that is greater than 1:"))
factor = 0

for i in range (1, user_num+1):
    if user_num%i == 0:
        factor += 1

if factor == 2:
    print("It is a prime number.")
else:
    print("It is not a prime nummber.")