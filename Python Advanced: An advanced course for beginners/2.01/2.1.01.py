def check_overlap(start1, end1, start2, end2):
    if start1 < end2 and start2 < end1:
        print("Да")
        h1, m1 = divmod(start2, 60)
        h2, m2 = divmod(end2, 60)
        print(f"{h1:02d}:{m1:02d} - {h2:02d}:{m2:02d}")
    else:
        print("Нет")

check_overlap(int(input()), int(input()), int(input()), int(input()))
