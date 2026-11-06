# def greet(name):
#     print(f"Hey! {name}")

# greet("Sameer")
# greet("Sameer")
# greet("Sameer")

##########################

# def welcome():
#     print("hey function")

# print("start of the program")

# welcome()

# print("end of the program")

##########################

# def multiple(a,b):
#     return a*b

# print(multiple(a=10, b=13))


# =============================

# def student(name,age):
#     print(f"Hey! {name} your age is {age}")

# student(age=25, name="Sameer")

###################################

# def calculate_price(price, tax=10):
#     total = price + (price * tax / 100)
#     return total

# print(calculate_price(1000))
# print(calculate_price(1000, 15))


#####################

def calculate(a,b):
    return a+b, a-b

addition, subtraction = calculate(10,5)
print(f"Addition: {addition}, Subtraction: {subtraction}")