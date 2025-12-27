import ast

try:
    input_str = input()
    files_dict = ast.literal_eval(input_str)
except EOFError:
    files_dict = {}

dangerous_extensions = [".exe", ".dll", ".bat", ".scr"]
fake_files = []

for filename, ext in files_dict.items():
    if filename.endswith('.'):
        fake_files.append(filename)
    elif ext.lower() in dangerous_extensions:
        fake_files.append(filename)

if not fake_files:
    print("Поддельные файлы не найдены.")
else:
    result_str = ", ".join(fake_files)
    print(f"Поддельные файлы: {result_str}")
