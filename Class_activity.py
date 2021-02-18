numbers = [3, 5, 6, 9, 2]
print(numbers)

numbers.append(10)
print(numbers)

numbers.insert(0, 99)
print(numbers)

numbers[0] += 1
print(numbers)

numbers += [8]
print(numbers)

numbers.remove(3)
print(numbers)

numbers.pop()
print(numbers)

names = ['Alex', 'Fay', 'Rhity']
names2 = ['Emma', 'Bob']
joined = "-".join(names)
print(joined)

joined = "-".join(names2)
print(joined)

hello = "*".join(names)
print(hello)

numbers = (3, 5, 6, 9, 2)
print(numbers)

first_int = 10
second_int = 20
if first_int > second_int:
    print("The first int is bigger!")
else:
    print("The second int is bigger!")

    for i, value in enumerate("hello"):
        print(i, value)

    for i, value in enumerate("hello", start=1):
        print(i, value)


def jagaban(celsius):
    result = (celsius * 1.8) + 32
    return result


x = 2
y = x + 1

temperature = 100
converted_temp = jagaban(temperature)
print(converted_temp)
