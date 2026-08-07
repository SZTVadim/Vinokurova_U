# ЗАДАНИЕ 1

temps = [18, 22, -3, 25, 19, -1, 21]
temps_f = [x * 9 / 5 + 32 for x in temps]

print(temps_f)

# ЗАДАНИЕ 2

users = {
    "ivan": "qwerty",
    "maria": "12345",
    "petr": "admin",
    "anna": "pass",
    "guest": "guest"
}
users_len_password = {key: len(value) for key, value in users.items()}

print(users_len_password)

# ЗАДАНИЕ 3

scores = (10, 7, 0, 9, 8, 5)
scores_x_10 = tuple(element * 1.1 for element in scores)

print(scores_x_10)
