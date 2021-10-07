try:
    with open("alice.txt",encoding="utf-8") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found")
else:
    print(content.lower().count("the "))