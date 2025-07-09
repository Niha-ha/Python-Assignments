#took input as float number so that we can perform operation on both integer and floating point number

number1 = float(input("Enter 1st number:"))
number2 = float(input("Enter 2nd number:"))
operator = input("Enter an operator(+, -, *, /)")

if operator == '+':
    print('sum is:', number1+number2)
elif operator == '-':
    print('Difference of two numbers:', abs(number1-number2))
elif operator == '*':
    print('product is:', number1*number2)
elif operator == '/' and number2 == 0:
    print("can't divide by 0")
elif operator == '/' and number2 != 0:
    print('quotient is:', round(number1/number2, 2))
else:
    print("Invalid operator. Please enter +, -, *, or /")

    


