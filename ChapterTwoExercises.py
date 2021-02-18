# 2.1 (What does this code do?) Create the variables x = 2 and y = 3, then determine what each of the following
# statements displays: a) print('x =', x) b) print('Value of', x, '+', x, 'is', (x + x)) c) print('x =') d) print((x
# + y), '=', (y + x)) In [1]: min(47, 95, 88, 73, 88, 84) Out[1]: 47 In [2]: max(47, 95, 88, 73, 88, 84) Out[2]: 95
# In [3]: print('Range:', min(47, 95, 88, 73, 88, 84), '-', ...: max(47, 95, 88, 73, 88, 84)) ...: Range: 47 - 95
# Exercises 71 2.2 (What’s wrong with this code?) The following code should read an integer into the variable rating:
# rating = input('Enter an integer rating between 1 and 10') 2.3 (Fill in the missing code) Replace *** in the
# following code with a statement that will print a message like 'Congratulations! Your grade of 91 earns you an A in
# this course'. Your statement should print the value stored in the variable grade: if grade >= 90: *** 2.4 (
# Arithmetic) For each of the arithmetic operators +, -, *, /, // and **, display the value of an expression with
# 27.5 as the left operand and 2 as the right operand. 2.5 (Circle Area, Diameter and Circumference) For a circle of
# radius 2, display the diameter, circumference and area. Use the value 3.14159 for π. Use the following formulas (r
# is the radius): diameter = 2r, circumference = 2πr and area = πr2. [In a later chapter, we’ll introduce Python’s
# math module which contains a higher-precision representation of π.] 2.6 (Odd or Even) Use if statements to
# determine whether an integer is odd or even. [Hint: Use the remainder operator. An even number is a multiple of 2.
# Any multiple of 2 leaves a remainder of 0 when divided by 2.] 2.7 (Multiples) Use if statements to determine
# whether 1024 is a multiple of 4 and whether 2 is a multiple of 10. (Hint: Use the remainder operator.)

x = 2
y = 3
print('x =', x)

print('value of', x, '+', x, 'is', (x + x))

print('x =')

print((x + y), 'x =', (y + x))

rating = int(input('Enter an integer rating between 1 and 10'))
print(rating * 10)

grade = int(input("enter a grade "))
if grade >= 90:
    print(f'Congratulations! Your grade of {grade} earns you an A in this course')

print(27.5 + 2)
print(27.5 - 2)
print(27.5 * 2)
print(27.5 / 2)
print(27.5 // 2)

# diameter = 2r ,  circumference =  2Pir, area = Pirsquared

diameter = 2 * 2
print(f'diameter is {diameter}')

circumference = 2 * 3.14159 * 2
print(f'circumference is {circumference}')

area = 3.14159 * 2 * 2
print(f'area is {area}')

number = int(input('enter a number'))
if number % 2 == 0:
    print(f'{number} is an even number')

number2 = int(input('enter a number'))
if number2 % 2 != 0:
    print(f'{number2} is an odd number')

if 1024 % 4 == 0:
    print('1024 is a multiple of 4')

if 2 % 10 != 0:
    print('10 is not a multiple of 2')
