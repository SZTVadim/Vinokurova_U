# Task 1
strr = type("Привет")
intt = type(42)
fltt = type(3.14)
listt = type([1, 2, 3])

print(""" 
Задание 1
""",f'{strr}, \n{intt}, \n{fltt}, \n{listt}')

# Task 2
text = "python PROGRAMMING"
low = text.lower()
up = text.upper()
cap = text.capitalize()
title = text.title()

print(""" 
Задание 2
""",f'{low}, \n{up}, \n{cap}, \n{title}')

# Task 3
text_1 = " Hello World "

print("""
Задание 3""")
print(f'{text_1.strip()}\n{text_1.lstrip()}\n{text_1.rstrip()}')

# Task 4
fruits = "яблоко,банан,апельсин,груша"
fruits_list = fruits.split(',')

print(""" 
Задание 4
""",f'{fruits_list},\n{" | ".join(fruits_list)}')

# Task 5
text_2 = "Я изучаю Python. Python - это круто!"

print(""" 
Задание 5
""",text_2.replace("Python","не Java"))

# Task 6
text_3 = "Python программирование на Python"

print(""" 
Задание 6
""",f'{text_3.find("Python")}\n{text_3.count("Python")}\n{text_3.find("Java")}')

# Task 7
print(""" 
Задание 7
""","Hello123".isalnum(), "12345".isdigit(), "Hello".isalpha(), "   ".isspace())

# Task 8
srez = "Pytonh very good"

print(""" 
Задание 8
""",f'{srez[0:3]}\n{srez[13:]}\n{srez[0::2]}\n{srez[::-1]}')

# Task 9
print(""" 
Задание 9""")
print("Он сказал: \"Привет\"")
print("Первая строка \nВторая строка")
