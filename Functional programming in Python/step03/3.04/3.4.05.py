def create_student(name, age, marks=None):
    if marks is None:
        marks = []
    return {
        'name': name,
        'age': age,
        'marks': marks  # оценки
    }


def add_mark(student, mark):
    student['marks'].append(mark)
