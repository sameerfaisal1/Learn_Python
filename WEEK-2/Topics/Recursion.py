# def coutdown(n):
#     if n == 0:
#         print("Countdown finished!")
#     else:
#         print(n)
#         coutdown(n - 1)

# coutdown(5)



def outer():
    print("Outer function")

    def inner():
        print("Inner function")

    inner()

outer()