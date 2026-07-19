num1 = (int(input("enter a number1:")))
num2 = (int(input("enter a number2:")))

print("enter symbol: + - * / %")
sign = input("enter a sign ")

if sign == "+":
    print(num1 + num2)
elif sign == "-":
    print(num1 - num2)
elif sign == "*":
    print(num1 * num2)
elif sign == "/":
    print(num1 / num2) 
elif sign == "%":
    print(num1 % num2)
else:
    print("Invalid operator")
