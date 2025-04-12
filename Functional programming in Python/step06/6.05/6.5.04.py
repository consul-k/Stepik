def get_info_marks(students, *marks):
    best_marks = {student: -1 for student in students}
    
    for mark_list in marks:
        for i, mark in enumerate(mark_list):
            student = students[i]
            if mark > best_marks[student]:
                best_marks[student] = mark
    
    return best_marks
