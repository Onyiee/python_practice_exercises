# (Odd or Even) Use if statements to determine whether an integer is odd or even.
# [Hint: Use the remainder operator. An even number is a multiple of 2. Any multiple of 2
# leaves a remainder of 0 when divided by 2.]


number = int(input("enter a number: "))
if number % 2 == 0:
    print("number is even")
else:
    print("number is odd")
