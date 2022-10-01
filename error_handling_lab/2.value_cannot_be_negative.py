class ValueCannotBeNegative(Exception):
    """"Number is below zero"""
    pass

for i in range(5):
    number = int(input())
    if number < 5:
        raise ValueCannotBeNegative