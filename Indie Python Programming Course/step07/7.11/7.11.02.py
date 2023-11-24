'''

Напишите программу, которая отсортирует список subject_marks по убыванию оценок.

Затем распечатайте предметы и оценки, каждую пару на новой строке через пробел

Sample Input:

Sample Output:

Maths 97
Physics 93
Programming 91
Science 90
English 88
History 82
French 78
Chemistry 76
Art 58

'''

subject_marks = [('English', 88), ('Science', 90), ('Maths', 97),
                 ('Physics', 93), ('History', 82), ('French', 78),
                 ('Art', 58), ('Chemistry', 76), ('Programming', 91)]
for i in sorted(subject_marks, key = lambda x: -x[1]):
    print(*i)
