def concatenate(*args, **kwargs):
    result = ''

    for element in args:
        if element in args:
            result += element
    for key, value in kwargs.items():
        result = result.replace(key, value)


    return result


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))