
def find_log_entries(level):
    with open("data_test/application.log", "r") as file:
        for line in file:
            if level in line:
                print(line.strip())


find_log_entries("ERROR")
find_log_entries("WARNING")
find_log_entries("INFO")
