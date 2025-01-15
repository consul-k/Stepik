def calculate_rating():
    
    line1 = input()
    line2 = input()
    line3 = input()
    line4 = input()

    set1 = set(line1.split())
    set2 = set(line2.split())
    set3 = set(line3.split())
    set4 = set(line4.split())

    matches_1_and_4 = len(set1.intersection(set4))
    matches_2_and_3 = len(set2.intersection(set3))

    rating = matches_1_and_4 + matches_2_and_3

    print(rating)

calculate_rating()
