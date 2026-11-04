print("\nWelcome to the Sameer's Store \n \n")

cart = []
amount = 500

while (amount>0):

    item = input('Enter the item you want to buy: ')
    cart.append(item)
    amount -=100
    
    if(amount==0):
        print("\n Cart: ")
        for x in cart:
            print(x)


        print("\n Do you want remove any item from the cart? (yes/no)")
        choice=input().lower()

        if(choice=='yes'):
            remove_item = input('Enter product name:  ').lower()
            cart.remove(remove_item)
            amount += 100
            continue
        else:
            print("\n Cart: ")
            for x in cart:
                print(x)
            break