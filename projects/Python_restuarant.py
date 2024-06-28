print("Welcome to PYTHON restaurant. Here's the menu:")
menu={
    "Pizza":50,
    "Pasta":40,
    "Burger": 50,
    "Salad":70,
    "Coffee": 80
}
totalprice=0
print("Pizza:50\nPasta:40\nBurger: 50\nSalad:70\nCoffee: 80")
order=input("Enter your order ")
if order in menu:
    print(f" Item {order} has been added to order ")
    totalprice+=menu[order]
else:
    print("Please order something from the menu ")

choice=input("You want to order something else : (yes/no) ")
if(choice =="yes"):
    order=input("Enter your order ")
    if order in menu:
        print(f" Item {order} has been added to order ")
        totalprice+=menu[order]
    else:
        print("Please order something from the menu ")
print("Your total order prize is Rs ",totalprice)