numbers1 = input()
numbers2 = input()

list1 = list(map(int, numbers1.split()))
list2 = list(map(int, numbers2.split()))

combined_list = list1 + list2

sorted_list = sorted(combined_list, reverse=True)

result = ' '.join(map(str, sorted_list))
print(result)
