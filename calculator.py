"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


def main():
    # This is where the user can input the calculation.
    
    # This will be a series of if statements for determining which function to call.
    cond = True
    while cond:
        input = raw_input("> ")
        numbers = input.split(' ')
        if numbers[0] == "+":
            addition = add(int(numbers[1]), int(numbers[2]))
            print addition
        elif numbers[0] == "-":
            subtraction = subtract(int(numbers[1]), int(numbers[2]))
            print subtraction
        elif numbers[0] == "*":
            multiplication = multiply(int(numbers[1]), int(numbers[2])) 
            print multiplication
        elif numbers[0] == "/":
            division = divide(float(numbers[1]), float(numbers[2]))
            print division
        elif numbers[0] == "square":
            squaring = square(int(numbers[1]))
            print squaring
        elif numbers[0] == "cube":
            cubed = cube(int(numbers[1]))
            print cubed
        elif numbers[0] == "pow":
            powered = power(int(numbers[1]), int(numbers[2]))
            print powered
        elif numbers[0] == "mod":
            module = mod(int(numbers[1]), int(numbers[2]))
            print module
        elif numbers[0] == "q":
            break

if __name__ == '__main__':
    main()