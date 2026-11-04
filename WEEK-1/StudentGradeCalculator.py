print('Student Grade Calculator \n \n')

name = input('Enter Your Name: ')
print(f"\n Hello {name}, Welcome to the Student Grade Calculator \n Enter your marks out of 100: \n")

total_Marks=100
try:
    input_marks = int(input('Enter your marks: '))

    if(input_marks > total_Marks or input_marks < 0):
        print("Invalid marks. Please enter a number between 0 and 100.")

    if(input_marks > 90):
        print("Your Grade is A \n")
    elif(input_marks > 80):
        print("Your Grade is B \n")
    elif(input_marks > 70):
        print("Your Grade is C \n")
    elif(input_marks > 60):
        print("Your Grade is D \n")
    else:
        print("Fail, Your Grade is F \n")
except ValueError:
    print("Invalid input. Please enter a number.")
