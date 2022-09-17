number_of_students = int(input())

students_dict = {}
for i in range(number_of_students):
    students, grade = input().split()
    if students not in students_dict:
        students_dict[students] = []
    students_dict[students].append(float(grade))

for students, grades in students_dict.items():
    average_grades = sum(grades) / len(grades)
    grades_list = " ".join(str(f"{grade:.2f}") for grade in grades)
    print(f"{students} -> {grades_list} (avg: {average_grades:.2f})")
