#Iteration exercise - 8 

loop = True
longest = 0 
result = ""

while loop:
    name = str(input("Name:"))
    counter = 0

    if name != "X":
        for i in name:
            counter += 1 
            if counter > longest :
                longest = counter
                result = name
                
    else:
        loop = False

print(f"Longest name: {result}")