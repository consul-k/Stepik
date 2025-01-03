student_name = input()

if student_name in class_7A:
    print(class_7A[student_name])
elif student_name in class_7B:
    print(class_7B[student_name])
elif student_name in class_3A:
    print(class_3A[student_name])
else:
    print("Такого ученика нет")
