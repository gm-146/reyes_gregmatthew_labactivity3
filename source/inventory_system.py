class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def restock(self, amount):
        self.quantity += amount
        print(f"Restocked {amount} units of {self.name}. New total: {self.quantity}")

    def sell(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount
            print(f"Sold {amount} units of {self.name}. Remaining: {self.quantity}")
        else:
            print(f"Error: Not enough stock to sell {amount} of {self.name}. Only {self.quantity} available.")

    def display_info(self):
        return f"[{self.product_id}] {self.name} - ${self.price:.2f} | Stock: {self.quantity}"


class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        if product.product_id not in self.products:
            self.products[product.product_id] = product
            print(f"Added {product.name} to the inventory.")
        else:
            print(f"Product ID {product.product_id} already exists.")

    def display_all(self):
        print("\n--- Current Inventory ---")
        if not self.products:
            print("Inventory is empty.")
        for product in self.products.values():
            print(product.display_info())
        print("-------------------------\n")


if __name__ == "__main__":
    store_inventory = Inventory()

    print(">>> TEST CASE 1: Adding Products")
    item1 = Product("P001", "Mechanical Keyboard", 89.99, 15)
    item2 = Product("P002", "Wireless Mouse", 45.50, 30)
    item3 = Product("P003", "HD Monitor", 199.99, 10)
    
    store_inventory.add_product(item1)
    store_inventory.add_product(item2)
    store_inventory.add_product(item3)
    
    store_inventory.display_all()

    print(">>> TEST CASE 2: Selling Items")
    item1.sell(5)  
    item3.sell(15) 
    
    store_inventory.display_all()

    print(">>> TEST CASE 3: Restocking Items")
    item2.restock(20)
    item3.restock(10)
    
    store_inventory.display_all()