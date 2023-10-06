#Iteration exercise - 5

user_num = int(input("Enter a number greater than one:"))

temp_num = 0
result = 0

for num in range (1, user_num+1):
    num_factor = 0
    for i in range (1, num+1):
        if num%i == 0:  
            num_factor += 1
    if num_factor > temp_num:
        temp_num = num_factor
        result = num

print(result)
            
    