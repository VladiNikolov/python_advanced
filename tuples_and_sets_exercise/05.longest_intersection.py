number = int(input())
best_intersection = set()

for _ in range(number):
    first_range, second_range = input().split("-")

    first_start, first_end = [int(i) for i in first_range.split(",")]
    second_start, second_end = [int(i) for i in second_range.split(",")]

    first = set(range(first_start, first_end + 1))
    second = set(range(second_start, second_end + 1))

    union_set = first.intersection(second)
    if len(union_set) > len(best_intersection):
        best_intersection = union_set
print(f"Longest intersection is [{', '.join(map(str, best_intersection))}] with length {len(best_intersection)}")
