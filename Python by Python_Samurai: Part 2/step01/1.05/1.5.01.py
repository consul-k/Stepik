lst = ["мыть  или не  мыть вот   в чем вопрос", "наташа   ростова приключения во вьетнаме",
      "лучший курс   на степике", "утка   кря кря кря   папа хрю хрю хрю"]

# продолжите решение здесь
print(["-".join(line.split()) for line in lst])
