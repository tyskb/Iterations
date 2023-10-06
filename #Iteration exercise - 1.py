#Iteration exercise - 1

user_num = int(input("Enter a number:"))
total = 1
num = 1

while num <= user_num:
    total = total*num
    num += 1 
print(f"{user_num}! = {total}")