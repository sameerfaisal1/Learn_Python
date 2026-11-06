#positionl only
def greet(name,/):
    print("hello", name)

greet(name="sameer")

#keyword only
def greet(*,name):
    print("hello", name)

greet("sameer")