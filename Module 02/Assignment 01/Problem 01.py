'''Write a function that takes two numbers as input and returns their average.
 Call the function with different values'''


def average(number1, number2):
    return (number1+number2)/2

# calling the function with different values
print(round(average(2.5,5.6),2))
print(round(average(2.5,-5.6),2))
print(round(average(-2.5,-5.6),2))
print(round(average(100,34),2))
