#Iteration exercise - 6

user_num = int(input("Enter an integer greater than -1:"))
num0 = 0
num1 = 1

for i in range (1, user_num):
    sum = num0 + num1
    num0 = num1
    num1 = sum
print(sum)