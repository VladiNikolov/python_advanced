def forecast(*args):
    weather_dict = {"Sunny": [], "Cloudy": [], "Rainy": []}
    result = []

    for element in args:
        l0, l1 = element
        location = l0
        weather = l1

        if weather not in weather_dict:
            weather_dict[weather] = []
        weather_dict[weather].append(location)

    for keys, values in weather_dict.items():
        for value in sorted(values):
            result.append(f"{value} - {keys}")

    return '\n'.join(result)

# print(forecast(
#     ("Beijing", "Sunny"),
#     ("Hong Kong", "Rainy"),
#     ("Tokyo", "Sunny"),
#     ("Sofia", "Cloudy"),
#     ("Peru", "Sunny"),
#     ("Florence", "Cloudy"),
#     ("Bourgas", "Sunny")))

# print(forecast(
#     ("Sofia", "Sunny"),
#     ("London", "Cloudy"),
#     ("New York", "Sunny")))

print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))
