#Iteration exercise - 7

loop = True
total_sum = 0
counter = 0

while loop:
    user_num = int(input("Enter a number from 0-100 or type -1 to exit:"))
    if user_num >= 0 and user_num <= 100:
        total_sum += user_num
        counter += 1
    elif user_num == -1:
        loop = False

avg = total_sum/counter
print(f"The average is {avg}.")