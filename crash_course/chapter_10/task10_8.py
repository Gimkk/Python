def read_file(file):
    try:
        with open(file) as f:
            content = f.read()
    except FileNotFoundError:
        print(f"{file} not found.")
    else:
        print(content)

files = ["cats.txt", "dogs.txt"]

for file in files:
    read_file(file)