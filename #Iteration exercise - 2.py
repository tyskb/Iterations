#Iteration exercise - 2

user_num = int(input("Enter an integar that is greater than 0:"))
print(f"Factors or {user_num}")

for i in range (1, user_num+1):
    if user_num%i == 0:
        print(i)