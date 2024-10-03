from VendingMachine import VendingMachine

class VendingMachineManager:
    # init
    def __init__(self):
        self.machines = {}

    # add machine
    def add_machine(self, location, inventory, max_quantity):
        if location in self.machines:
            print(f"Machine already exists at {location}.")
        else:
            self.machines[location] = VendingMachine(inventory, location, max_quantity)
            print(f"\nAdded new machine at {location}.")

    # select machine
    def select_machine(self, location):
        if location in self.machines:
            return self.machines[location]
        else:
            print(f"\nNo machine fount at {location}.")
            return None
        
    # display all machines
    def display_all_machines(self):
        print("\nAvailable vending macines:")
        for location, machine in self.machines.items():
            print(f"- {location}, Revenue Earned: ${machine.total_money:.2f}")