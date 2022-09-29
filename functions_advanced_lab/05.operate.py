def operate(operator, *args):
    def add(*args):
        return sum(args)

    def subtract(x, *args):
        return x + sum(-y for y in args)

    def multiply(*args):
        result = 1
        for x in args:
            result *= x
        return result


    def devide(x, *args):
        result = x
        for value in args:
            result /= value
        return result

    if operator == "+":
        return add(*args)
    elif operator == "-":
        return subtract(*args)
    elif operator == "*":
        return multiply(*args)
    elif operator == "/":
        return devide(*args)

print(operate("*", 3, 4))