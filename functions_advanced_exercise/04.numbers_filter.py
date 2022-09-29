def even_odd_filter(**kwargs):
    result_dict= {}

    for key, value in kwargs.items():
        parity = 0 if key == "even" else 1
        filtered = [int(i) for i in value if i % 2 == parity]
        result_dict[key] = filtered

    return result_dict


print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
