def read_file(file_name):
    with open(file_name, 'r') as file:
        data = file.read()
        print(data)

a = input()
read_file(a)
