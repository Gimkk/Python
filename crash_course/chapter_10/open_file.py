#task10-1

file_path = 'learning_python.txt'
with open(file_path) as file_object:
    content = file_object.read()
print(content.strip())

print("\n--Read file line by line using for loop--")
with open(file_path) as file_object:
    for line in file_object:
        print(line.rstrip())

print("\n--Read file line by line using readlines--")
with open(file_path) as file_object:
    lines = file_object.readlines()

print(lines)

#task10-2
print("\n--Read file line by line and replace word--")
with open(file_path) as file_object:
    for line in file_object:
        print(line.replace("love", "like").strip())