number_of_student = int(input())

student_dict = {}
for student in range(number_of_student):
    student_name, grade = input().split()
    if student_name not in student_dict:
        student_dict[student_name] = []
    student_dict[student_name].append(float(grade))

for student, grades in student_dict.items():
    average_grade = sum(grades) / len(grades)
    grade_formatted = " ".join(f'{grade:.2f}' for grade in grades)
    print(f"{student} -> {grade_formatted} (avg: {average_grade:.2f})")

