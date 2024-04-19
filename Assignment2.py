
num1 = int(input("Enter a four digit number: "))

a =num1%10
b =int(num1/10)%10
c =int(num1/100)%10
d =int(num1/1000)%10

print(f"Face value={d} {c} {b} {a}")

print(f"place value= {d*1000} + {c*100} + {b*10} + {a*1}")

print(f"reversed value = {a}{b}{c}{d}")


