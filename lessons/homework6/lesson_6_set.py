# ЗАДАНИЕ 1

fruits = {"яблоко", "банан"}
fruits.add("апельсин")
fruits.update(["груша", "виноград"])

print(fruits)

fruits.discard("банан")
fruits.discard("киви")
# fruits.remove("киви")

print(fruits)

random_fruit = fruits.pop()

print(random_fruit)

# ЗАДАНИЕ 2

coordinates = (10, 20, 30, 20, 10, 20, 40)

print(coordinates[0])
print(coordinates[-1])
print(coordinates[1:4])
print(30 in coordinates)
print(coordinates.index(20))
print(coordinates.count(20))
print(coordinates.count(50))
print(len(coordinates))
