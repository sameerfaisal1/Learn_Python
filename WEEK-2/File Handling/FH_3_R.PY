try:
    with open("notes.txt", "r") as f:
        data = f.read()
        print(data)

except FileNotFoundError:
    print("File not found")

except PermissionError:
    print("You don't have permission to open this file")