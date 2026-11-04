print("\nWelcome to the Sameer's Store \n \n")

cart = []
amount = 500

while (amount>0):

    item = input('Enter the item you want to buy: ')
    cart.append(item)
    amount -=100
    
print("\n Your Cart: ")
for x in cart:
    print(x)



