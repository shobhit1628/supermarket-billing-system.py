class SupermarketBillingSystem:
    def __init__(self):
        self.products = {
            '1001': {'name': 'Rice', 'price': 40.0},
            '1002': {'name': 'Sugar', 'price': 30.0},
            '1003': {'name': 'Milk', 'price': 25.0},
            '1004': {'name': 'Bread', 'price': 20.0},
            '1005': {'name': 'Butter', 'price': 50.0},
            '1006': {'name': 'surf', 'price':30.0},
            '1007': {'name': 'tamato', 'price':40.0},
            '1008': {'name': 'onion', 'price':35.0},
            '1009': {'name': 'oil', 'price':102.0},
            '1010': {'name': 'apple','price':55.0},
            '1011': {'name': 'light bulbs', 'price':20.0},
            '1012': {'name': 'pens', 'price':10.0},
            '1013': {'name': 'pencils','price':5.0},
            '1014': {'name': 'shampoo','price':2.0},
            '1015': {'name': 'body wash','price':50.0},
            '1016': {'name': 'hand soap','price':23.0},
            '1017': {'name': 'toothpast','price':57.0},
            '1018': {'name': 'mouthwash','price':100.0},
            '1019': {'name': 'deodorant','price':67.0},
            '2020': {'name': 'hand sanitizer','price':70.0}
                    }
        self.cart = {}

    def display_products(self):
        print("\nAvailable Products:")
        print(f"{'Product ID':<15}{'Name':<15}{'Price (per unit)'}")
        for product_id, details in self.products.items():
            print(f"{product_id:<15}{details['name']:<15}{details['price']}")

    def add_to_cart(self, product_id, quantity):
        if product_id in self.products:
            if product_id in self.cart:
                self.cart[product_id]['quantity'] += quantity
            else:
                self.cart[product_id] = {
                    'name': self.products[product_id]['name'],
                    'price': self.products[product_id]['price'],
                    'quantity': quantity
                }
            print(f"Added {quantity} of {self.products[product_id]['name']} to the cart.")
        else:
            print("Invalid Product ID. Please try again.")

    def remove_from_cart(self, product_id):
        if product_id in self.cart:
            del self.cart[product_id]
            print("Item removed from the cart.")
        else:
            print("Item not found in the cart.")

    def view_cart(self):
        if not self.cart:
            print("\nYour cart is empty.")
            return
        print("\nYour Cart:")
        print(f"{'Product ID':<15}{'Name':<15}{'Price':<15}{'Quantity':<15}{'Total'}")
        for product_id, details in self.cart.items():
            total_price = details['price'] * details['quantity']
            print(f"{product_id:<15}{details['name']:<15}{details['price']:<15}{details['quantity']:<15}{total_price}")

    def generate_bill(self):
        if not self.cart:
            print("\nYour cart is empty. No bill to generate.")
            return
        print("\nFinal Bill:")
        print(f"{'Product ID':<15}{'Name':<15}{'Price':<15}{'Quantity':<15}{'Total'}")
        grand_total = 0
        for product_id, details in self.cart.items():
            total_price = details['price'] * details['quantity']
            grand_total += total_price
            print(f"{product_id:<15}{details['name']:<15}{details['price']:<15}{details['quantity']:<15}{total_price}")
        print("-" * 60)
        print(f"{'Grand Total:':<45}{grand_total}")

# Main function to run the billing system
def main():
    system = SupermarketBillingSystem()
    while True:
        print("\n--- Supermarket Billing System ---")
        print("1. Display Products")
        print("2. Add to Cart")
        print("3. Remove from Cart")
        print("4. View Cart")
        print("5. Generate Bill")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            system.display_products()
        elif choice == '2':
            product_id = input("Enter the Product ID to add: ")
            try:
                quantity = int(input("Enter the quantity: "))
                system.add_to_cart(product_id, quantity)
            except ValueError:
                print("Invalid quantity. Please enter a number.")
        elif choice == '3':
            product_id = input("Enter the Product ID to remove: ")
            system.remove_from_cart(product_id)
        elif choice == '4':
            system.view_cart()
        elif choice == '5':
            system.generate_bill()
        elif choice == '6':
            print("Thank you for using the Supermarket Billing System!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
