def save_student(name, marks):

    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100")

    with open("students.txt", "a", encoding="utf-8") as f:
        f.write(f"{name},{marks}\n")


def show_students():

    try:
        with open("students.txt", "r", encoding="utf-8") as f:

            for line in f:
                print(line.strip())

    except FileNotFoundError:
        print("No student records found.")


try:
    name = input("Enter student name: ")
    marks = int(input("Enter student marks: "))

    save_student(name, marks)

    print("Student saved successfully!")

except ValueError as e:
    print("Error:", e)

show_students()