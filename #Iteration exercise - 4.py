#Iteration exercise - 4

sum = 0

for i in range (1, 10000+1):
    for x in range (1,i):
        if i%x ==0:
            sum += x
    if sum == i:
        print(f"{i} is a perfect number.")
    sum = 0
