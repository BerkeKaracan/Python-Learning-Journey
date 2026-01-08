import os
import time
class Product :
    # Base class representing a product in the store.
    #     Contains product name, price, and stock information.
    def __init__(self,product_name,product_price,product_stock):
        self.product_name = product_name
        self.product_price = product_price
        self.product_stock = product_stock

    def __str__(self):
        return f"{self.product_name}"

class Store :
    # Manages store operations such as loading data,
    # updating the database, and handling product searches.
    def __init__(self):
        self.products = []

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def load_products(self):
        # Loads products from 'products.txt' into memory (RAM) at startup.
        # Creates the file if it doesn't exist. Skips empty or malformed lines.
        if not os.path.exists("products.txt"):
            open("products.txt", "w").close()
            return
        with open('products.txt','r') as f:
            lines = f.readlines()
            for line in lines:
                line2 = line.strip().split(',')
                if len(line2) < 3:
                    continue
                self.products.append(Product(line2[0],int(line2[1]),int(line2[2])))

    def show_products(self):
        print("\n" + "-" * 50)
        counter = 0
        for product2 in self.products:
            counter+= 1
            print(f"{counter} : Product : {product2.product_name} - Price: {product2.product_price} - Stock: {product2.product_stock}")
        print("\n" + "-" * 50)
    def finder_product(self,product_name):
        # Searches for a product by name (Case-insensitive). Returns the object or None.
        for i in self.products:
            if i.product_name.upper() == product_name.upper():
                return i
        return None

    def update_db(self):
        # Saves the current state of products (stock updates) back to 'products.txt'
        with open('products.txt','w') as f:
            for i in self.products:
                f.write(f"{i.product_name},{i.product_price},{i.product_stock}\n")
            print("Database updated")

    def save_db(self, username, new_balance):
        # Updates the specific user's balance in 'users.txt'.
        # Reads all lines, updates only the matching user, and rewrites the file.
        with open('users.txt','r') as f:
            n = f.readlines()
        with open('users.txt','w') as f:
            for i in n:
                m = i.strip().split(',')
                if len(m) <2 :
                    continue
                else:
                    if username == m[0]:
                        f.write(f"{username},{new_balance}\n")
                    else:
                        f.write(i)

    def save_orders(self, username, cart):
        if not os.path.exists("orders.txt"):
            open("orders.txt", "w").close()
        with open("orders.txt", "a") as f:
            for item in cart:
                f.write(f"{username},{item.product_name},{item.product_price}\n")

class User :
    # Manages user actions: shopping cart, balance, and checkout process.
    def __init__(self,username):
        self.username = username
        self.cart = []
        self.balance = 0
        # Load user balance from file
        try:
            with open("users.txt","r") as f:
                lines = f.readlines()
                for line in lines:
                    line2 = line.strip().split(',')
                    if line2[0] == self.username:
                        self.balance = int(line2[1])
                        break
        except FileNotFoundError:
            pass

    def add_to_cart(self,prdct_name,active_store):
        # Adds a product to the cart if stock is available.
        pr_obj = active_store.finder_product(prdct_name)
        if pr_obj:
            if pr_obj.product_stock > 0 :
                self.cart.append(pr_obj)
            else:
                print("Out of stock")
        else:
            print("Product not found! ")

    def check_out(self,active_store):
        # Handles the payment process:
        # 1. Checks balance.
        # 2. Deducts money and stock.
        # 3. Updates both databases (User & Product).
        if self.balance == 0 and not self.cart:
            print("Insufficient funds or empty cart.")
            return
        total_price = 0
        for i in self.cart:
            total_price += i.product_price
        if total_price > self.balance:
            print(f" Insufficient balance! Total: {total_price}, Your Balance: {self.balance}")
        else:
            self.balance -= total_price
            active_store.save_db(self.username,self.balance)
            active_store.save_orders(self.username, self.cart)
            for i in self.cart:
                i.product_stock -= 1
                #  Update User DB
            active_store.update_db()
            self.cart.clear()
            print("Your payment was successful, your receipt is being created.")
            time.sleep(2)
            print("You complete your shopping . Thank you for choosing us ")

    def show_cart(self):
        print("Your cart :")
        if not self.cart:
            print("Empty")
        for i in self.cart:
            print(f"{i.product_name},{i.product_price},{i.product_stock}")


shop = Store()
shop.load_products()
shop.clear_screen()
print("***********************************")
print("  WELCOME  ")
print("     TO    ")
print("THE SHOP APP ")
print("***********************************")
name = input("Please, Enter Your  Name : ")
user = User(name)
while True :
    shop.clear_screen()
    print(f"👤 {user.username.upper()} | 💰 Balance: {user.balance} USD | 🛒 Cart: {len(user.cart)} Products")
    print("*" * 50)
    a = input('''
    [1] - Show products
    [2] - Add to cart 
    [3] - Pay 
    [4] - Show my cart
    [5] - Exit
    Select Option :   ''')
    if a == "1" :
        shop.show_products()
        input("Press enter to continue")
    elif a == "2" :
        shop.show_products()
        c = input("Enter product name to buy :  ")
        user.add_to_cart(c,shop)
        user.show_cart()
        time.sleep(1.5)
    elif a == "3" :
        user.check_out(shop)
        input("Press enter to continue")
    elif a == "4" :
        user.show_cart()
        input("Press enter to continue")
    elif a == "5" :
        print("Goodbye 👋")
        break
    else:
        print("Invalid option")









