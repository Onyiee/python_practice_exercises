# def centimeter_to_meter_conversion(centimeter):
#     """ documentation"""
#     meter = centimeter / 100
#     print(meter)
#
#
# centimeter_to_meter_conversion(200000)
test = 7
print(id(test))


def multiply(num):
    print(num)
    print("num id is ", id(num))
    print("num is test", num is test)
    num = 34
    print("after assignment num id is ", id(num))
    print("num is test", num is test)


multiply(test)
print(test)
print(id(test))
