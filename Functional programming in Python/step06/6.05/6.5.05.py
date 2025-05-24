def get_info_marks(students, *marks):
    info = {
        student: {"best": -1, "worst": 101}
        for student in students
    }

    for mark_list in marks:
        for i, mark in enumerate(mark_list):
            student = students[i]
            if mark > info[student]["best"]:
                info[student]["best"] = mark
            if mark < info[student]["worst"]:
                info[student]["worst"] = mark

    return info
