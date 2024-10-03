from VendingMachineManager import VendingMachineManager


inventory = {
    "A1": {"name": "Chips", "price": 1.50, "quantity": 10},
    "A2": {"name": "Soda", "price": 1.25, "quantity": 8},
    "A3": {"name": "Candy Bar", "price": 1.00, "quantity": 8},
    "B1": {"name": "Gum", "price": 0.75, "quantity": 10},
    "B2": {"name": "Water", "price": 1.00, "quantity": 9},
    "B3": {"name": "Cookies", "price": 1.75, "quantity": 5},
    "C1": {"name": "Juice", "price": 1.50, "quantity": 7},
    "C2": {"name": "Pretzels", "price": 1.25, "quantity": 9},
    "C3": {"name": "Granola Bar", "price": 1.00, "quantity": 8},
}


if __name__ == "__main__":
    max_quantity = 10  # Define the maximum quantity for each item in the machine

    # Initialize manager
    manager = VendingMachineManager()

    # Add machines to manager
    manager.add_machine("Mall", inventory, max_quantity)
    manager.add_machine("School", inventory, max_quantity)
    manager.add_machine("Airport", inventory, max_quantity * 2)
    manager.add_machine("Theater", inventory, max_quantity)

    # Interactive menu loop for managing multiple machines
    while True:
        print("\n--- Vending Machine Manager Menu ---")
        print("1. Display All Machines")
        print("2. Select Machine")
        print("3. Exit")

        choice = input("\nEnter your choice (1-3): ")

        if choice == '1':
            manager.display_all_machines()
        elif choice == '2':
            location = input("\nEnter the location of the machine to select: ")
            machine = manager.select_machine(location)
            if machine:
                while True:
                    print(f"\n--- {location} Vending Machine Menu ---")
                    print("1. Display Items")
                    print("2. Select Item")
                    print("3. Display Total Money Collected")
                    print("4. Restock Machine")
                    print("5. Go Back")

                    machine_choice = input("\nEnter your choice (1-5): ")

                    if machine_choice == '1':
                        machine.display_items()
                    elif machine_choice == '2':
                        item_code = input("\nEnter the item code to select: ")
                        machine.select_item(item_code)
                    elif machine_choice == '3':
                        machine.display_total_money()
                    elif machine_choice == '4':
                        machine.restock_machine() #need to fix this, restocking other machines
                    elif machine_choice == '5':
                        break
                    else:
                        print("\nInvalid choice. Please try again.")
        elif choice == '3':
            print("\nExiting Vending Machine Manager. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")