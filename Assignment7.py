print("The factorial from 1 to 10 is ")

a = 1
b = a
li = [1,2,3,4,5,6,7,8,9,10]
for value in li:
    while a <= value:
        b = b * a
        a = a + 1 
    else:
        print(f"Factorial of {value} is {b}")