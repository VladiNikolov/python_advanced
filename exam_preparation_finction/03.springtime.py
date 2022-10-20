def start_spring(**elements):

    spring_objects = {}
    result = []

    for value, key in elements.items():
        if key not in spring_objects:
            spring_objects[key] = []

        spring_objects[key].append(value)

    spring_objects = sorted(spring_objects.items(), key=lambda x:(-len(x[1]), x[0]))

    for spring_object,values in spring_objects:
        result.append(f"{spring_object}:")

        for value in sorted(values):
            result.append(f"-{value}")

    return "\n".join(result)

example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))




