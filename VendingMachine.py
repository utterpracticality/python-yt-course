class VendingMachine:
    # init function
    def __init__(self, inventory, location, max_quantity):
        self.inventory = inventory
        self.total_money = 0.0
        self.location = location
        self.max_quantity = max_quantity

    # display items
    def display_items(self):
        print(f"\nItmes availabe in {self.location} machine:")
        for code, details in self.inventory.items():
            print(f"{code}: {details['name']} - ${details['price']:.2f} {details['quantity']} in stock")

    # process payment
    def process_credit_card_payment(self, amount):
        confirmation = input(f"\nConfirm payment of ${amount:.2f} with credit card? (yes/no): ")
        if confirmation.lower() == "yes":
            self.total_money += amount
            print(f"\nPayment of ${amount:.2f} successful.")
            return True
        else:
            print("\nPayment canceled.")
            return False

    # item selection
    def select_item(self, item_code):
        if item_code in self.inventory:
            item = self.inventory[item_code]
            if item["quantity"] > 0:
                if self.process_credit_card_payment(item["price"]):
                    self.dispense_item(item_code)
            else:
                print(f"\nSorry, {item['name']} is out of stock.")
        else:
            print("\nInvalid item code. Please select valid item.")

            
    # dispense item
    def dispense_item(self, item_code):
        item = self.inventory[item_code]
        item["quantity"] -= 1
        print(f"\nDispensing {item['name']}. Enjoy!")

    # restock machine
    def restock_machine(self):
        for item_code, details in self.inventory.items():
            details["quantity"] = self.max_quantity
        print(f"\nAll items in the {self.location} machine have been restocked.")

    # display total revenue
    def display_total_money(self):
        print(f"\nTotal money collected by the machine at {self.location}: ${self.total_money:.2f}")