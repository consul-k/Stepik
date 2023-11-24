'''

Напишите программу, которая отсортирует список subject_marks по возрастанию оценок. 
Затем распечатайте предметы и оценки, каждую пару на новой строке через пробел

Sample Input:

Sample Output:

History 82
English 88
Science 90
Physics 93
Maths 97

'''

subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Physics', 93),('History', 82)]
for i in sorted(subject_marks, key = lambda x: x[1]):
    print(*i)
