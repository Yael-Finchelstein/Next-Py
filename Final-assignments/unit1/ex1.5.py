with open(r"C:\yaelUser\names.txt", 'r') as file:
    names = file.readlines()

# 1
longest_name = max([name.strip() for name in names], key=len)
print(longest_name)

# 2
total_length = sum(len(name.strip()) for name in names)
print(total_length)

# 3
shortest_length = min(len(name.strip()) for name in names)
shortest_names = [name.strip() for name in names if len(name.strip()) == shortest_length]
for name in shortest_names:
    print(name)

# 4
with open("name_length.txt", "w") as f:
    for name in names:
        f.write(str(len(name.strip())) + "\n")

# 5
length = int(input("Please enter name length: "))
names_of_length = [name.strip() for name in names if len(name.strip()) == length]
for name in names_of_length:
    print(name)
