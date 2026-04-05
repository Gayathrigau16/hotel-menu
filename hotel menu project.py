print("==============Hotel Menu==============")
menu = {"Dhosa":20,
        "Idly":10,
        "Pongal":30,
        "Vada":15,
        "Meal":80,
        "Poori":10,
        "Sappathi":10,
        "Tea":15,
        "Coffee":10
}

cart = {}
total = 0

while True:
    print("\nMenu:")
    for item,prize in menu.items():
        print(f"{item} - {prize}")

    choice = input("Enter Item (or 'Done'):")

    if choice == "done":
        break

    if choice in menu:
        qty = int(input("Enter Quantity:"))
        cart[choice] = cart.get (choice ,0) + qty
        total += menu[choice] * qty

    else:
        print("Invalid Item")

print("\nOrder Summary:")
print(f"{cart} X {qty} = {menu[item]*qty}")
print(f"Total Bill:{total}")

print("====================Thank You====================")

          
        


































    
    
