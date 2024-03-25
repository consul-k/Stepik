number = input()

first_half = number[:3]
second_half = number[3:]

fhs = 0
shs = 0

for i in first_half:
    fhs += int(i)
for j in second_half:
    shs += int(j)
    
if fhs == shs:
    print("Счастливый")
else:
    print("Несчастливый")
