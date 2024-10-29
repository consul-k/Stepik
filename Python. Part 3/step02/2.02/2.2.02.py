for index, (student, score) in enumerate(zip(students, scores), start=1):
    print(f"{index}. {student}: {score}")
