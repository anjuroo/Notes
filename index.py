class Menu:
    def __init__(self, choice):
        self.pinakbet = "Pinakbet na Pinasarap"
        self.scallop = "Scallop"
        self.lechon_kawali = "Lechon Kawali"
        self.order_name = ""
        self.bill = 0
        self.choice = choice
    
    def get_order(self):
        menu_orders = {
            1: self.pinakbet,
            2: self.scallop,
            3: self.lechon_kawali
        }
        self.order_name = menu_orders.get(self.choice, "Invalid Choice!")
        return self.order_name
    
    def get_bill(self):
        if self.choice == 1:
            self.bill = 250
        elif self.choice == 2:
            self.bill = 450
        elif self.choice == 3:
            self.bill = 699
        return self.bill
    
    def display_menu(self):
        print("\n-------------Menu-------------")
        print("1. " + self.pinakbet + " = Php250")
        print("2. " + self.scallop + " = Php450")
        print("3. " + self.lechon_kawali +" = Php699\n")


    def display_order(self):
        print(f"Order for table number {self.choice} is {self.order_name}")
        print(f"\nBill is Php{self.bill}.00")
        print("Thank you for Dining!\nCome Again!")

class TestMenu:
    def __init__(self):
        pass
    
    def run(self):
        menu = Menu(0)
        menu.display_menu()
        choice = int(input(""))
        menu.choice = choice
        order = menu.get_order()
        bill = menu.get_bill()
        menu.display_order()


test = TestMenu()
test.run()
