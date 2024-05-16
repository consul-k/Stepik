data_type = input().strip()

if data_type == "int":
    num1 = int(input().strip())
    num2 = int(input().strip())
    if num1 == 0 and num2 == 0:
        print("Empty Ints")
    else:
        print(num1 + num2)

elif data_type == "str":
    text = input().strip()
    if not text:
        print("Empty String")
    else:
        print(text)

elif data_type == "list":
    items = input().strip().split()
    if not items:
        print("Empty List")
    else:
        print(items[-1])

else:
    print("Unknown type")
