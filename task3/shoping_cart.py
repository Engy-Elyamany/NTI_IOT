exit_app = False
cart = {}
your_cart = {}

store_items = {
    1 : ("apples", 90),
    2 : ("milk" , 63),
    3 : ("meat" , 170),
    4 : ("poultry" , 90),
    5 : ("vegetables" , 75),
    6 : ("oranges" , 40),
    7 : ("candy" , 20),
    8 : ("snacks" , 20)
}

features = {
    1 : "View all available items",
    2 : "Add to cart",
    3 : "view cart",
    4 : "Exit",
}

print("\nYour Virtual Shopping Cart\n")


def user_next_step():
    for num,feature in features.items():
        print(f"{num} => {feature}")
    return int(input("Choose your next step "))

def print_available_items(store_items):
    print("\nAll available items : ")
    for id,(item,price) in store_items.items():
        print(f"[{id}] {item} = {price}")
    print(" ")

def add_to_cart(store_items):
        c = 'y'
        while c == 'y':
            print("\nAdd to your cart : ")

            view_items = input("Do you need to view availavle items? [y/n] ")
            if view_items == 'y':
                print_available_items(store_items)
 
            while True:
                 get_id = int(input("[please choose by ID] "))
                 if get_id in store_items.keys():
                    break
                 else:
                    print("Invalid Item ID")

            item_count = int(input(f"How many \"{store_items[get_id][0]}\" do you want? "))
            cart[get_id] = (store_items[get_id][0],item_count)
            c = input("Add another item [y/n] : ")
        print(" ")
        return cart

def view_cart_and_price(cart,store_items):
     total_price = 0
     # this if is true when the cart is empty
     if(not bool(cart)):
         print("\nYour cart is empty")
     else:
        print(" ")
        for id,(_,count) in cart.items():
          print(f"{cart[id][0]} : {cart[id][1]} pieces")
          total_price += count * store_items[id][1]
        print(f"total price = {total_price}")
     print(" ")
     


while not exit_app:
    
    while True:
        get_choice = user_next_step()
        if get_choice in features.keys():
            if get_choice == 1:
                print_available_items(store_items)
            elif get_choice == 2:
                your_cart = add_to_cart(store_items)

            elif get_choice == 3:
                view_cart_and_price(your_cart,store_items)
            
            elif get_choice == 4:
                exit_app = True
            break
        else:
            print("\nInvalid choice, please choose from MENU\n")



