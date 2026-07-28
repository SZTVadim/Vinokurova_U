# ЗАДАНИЕ 1
fruits = ["яблоко"]

print(fruits)

fruits.append("банан")
fruits.extend(["апельсин", "груша"])
fruits.insert(1, "виноград")

print(fruits)

# ЗАДАНИЕ 2
fruits_2 = ["яблоко", "банан", "апельсин", "банан"]
fruits_2.remove("банан")
fruits_new = fruits_2.pop()

print(fruits_2)
print(fruits_new)

# ЗАДАНИЕ 3
fruits_3 = ["яблоко", "банан", "апельсин", "банан"]

print(fruits_3.index("банан"))
print(fruits_3.count("банан"))

# ЗАДАНИЕ 4
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()

print(numbers)

numbers.sort(reverse=True)

print(numbers)
