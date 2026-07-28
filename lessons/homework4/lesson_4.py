# Task 1
strr = type("Привет")
intt = type(42)
fltt = type(3.14)
listt = type([1, 2, 3])

print(strr)
print(intt)
print(fltt)
print(listt)

# Task 2
text = "python PROGRAMMING"

print(text.lower())
print(text.upper())
print(text.capitalize())
print(text.title())

# Task 3
text_1 = " Hello World "

print(text_1.strip())
print(text_1.lstrip())
print(text_1.rstrip())

# Task 4
fruits = "яблоко,банан,апельсин,груша"
fruits_list = fruits.split(',')

print(fruits_list)
print(" | ".join(fruits_list))

# Task 5
text_2 = "Я изучаю Python. Python - это круто!"

print(text_2.replace("Python", "не Java"))

# Task 6
text_3 = "Python программирование на Python"

print(text_3.find("Python"))
print(text_3.count("Python"))
print(text_3.find("Java"))

# Task 7
print("Hello123".isalnum())
print("12345".isdigit())
print("Hello".isalpha())
print("   ".isspace())

# Task 8
srez = "Pytonh very good"

print(srez[0:3])
print(srez[13:])
print(srez[0::2])
print(srez[::-1])

# Task 9
print("Он сказал: \"Привет\"")
print("Первая строка \nВторая строка")

