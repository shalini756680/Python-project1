#Define the menu of restaurant
menu = {
    'Pizza':40,
    'Pasta':50,
    'Burger':60,
    'Salad':70,
    'Coffee':80,
}
#Great
print("Welcome to PYTHON Restuarant")
print("Pizza: Rs40\nPasta: Rs50\n Burger: Rs60\nSalad:Rs70\nCoffee: Rs80")
order_total = 0
#80 + 70 = 150
item_1 = input("Enter the name of item you want to order =")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item{item_1} has been added to your order")
