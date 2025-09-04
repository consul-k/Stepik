d = []

for i in range(int(input())):

               d.append(input())

print(all(yey[-1] == "7" for yey in d))
