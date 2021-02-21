# 3.12 (Palindromes) A palindrome is a number, word or text phrase that reads the same
# backwards or forwards. For example, each of the following five-digit integers is a
# palindrome: 12321, 55555, 45554 and 11611. Write a script that reads in a five-digit integer
# and determines whether it’s a palindrome. [Hint: Use the // and % operators to separate
# the number into its digits.]

number = int(input("Enter a five-digit number: "))

fifth_number = number % 10
number = number // 10

fourth_number = number % 10
number = number // 10

third_number = number % 10
number = number // 10

second_number = number % 10
number = number // 10

first_number = number % 10
number = number // 10

if first_number == fifth_number and fourth_number == second_number:
    print("Number is a palindrome")
else:
    print("Number is not a palindrome")
