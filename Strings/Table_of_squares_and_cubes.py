# 2.8 (Table of Squares and Cubes) Write a script that calculates the squares and cubes
# of the numbers from 0 to 5. Print the resulting values in table format, as shown below. Use
# the tab escape sequence to achieve the three-column output.
# number square cube
# 0 0 0
# 1 1 1
# 2 4 8
# 3 9 27
# 4 16 64
# 5 25 125

number = 0
print("number\tsquare\tcube")
while number <= 5:
    square = number * number
    cube = number * number * number
    print("{}\t\t{}\t\t{}".format(number, square, cube))
    number += 1


# number = 0
# while number != -1:
#     number = int(input("enter a number, enter -1 to exit:"))
#     if number != -1:
#         square = number * number
#         cube = number * number * number
#         print(number, square, cube)
# print("number\tsquare\tcube")

# for number in range(5):
#     square = number * number
#     cube = number * number * number
#     print(f"\t{number}\t\t{square}\t\t{cube}")
