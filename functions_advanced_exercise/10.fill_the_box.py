def fill_the_box(height, length, width,  *args):
    volume = height * length * width

    left_cubes = 0
    for element in args:
        if element == "Finish":
            break

        if volume > element:
            volume -= element
        else:
            element -= volume
            left_cubes += element
            volume = 0



    if volume:
        return f"There is free space in the box. You could put {volume} more cubes."
    else:
        return f"No more free space! You have {left_cubes} more cubes."



print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))