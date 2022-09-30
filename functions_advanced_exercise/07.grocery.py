def grocery_store(**kwargs):
    sorted_elements = [f"{name_product}: {value_product}" for name_product, value_product in sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))]
    return "\n".join(sorted_elements)

print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))

