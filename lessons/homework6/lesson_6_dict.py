# ЗАДАНИЕ 1

student = {
    "name": "Иван",
    "age": 20,
    "course": 2,
    "city": "Moscow"
}

print(student.keys())
print(student.values())

for entries in student.items():
    print(entries)

for values in student.values():
    print(values)

# ЗАДАНИЕ 2

student1 = {"имя": "Иван", "возраст": 20, "курс": 2}
student2 = {"имя": "Мария", "возраст": 21, "город": "Санкт-Петербург"}

student1.update(student2)

print(student1)
print(student2)

# такой вариант для задания со student3

student_1 = {"имя": "Иван", "возраст": 20, "курс": 2}
student_2 = {"имя": "Мария", "возраст": 21, "город": "Санкт-Петербург"}
student_3 = student_1 | student_2

print(student_1)
print(student_2)
print(student_3)
