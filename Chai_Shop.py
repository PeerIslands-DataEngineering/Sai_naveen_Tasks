from abc import ABC,abstractmethod
class Chai(ABC):
    def __init__(self,name,base_price,quantity_in_stock):
        self.name=name
        self.base_price=base_price 
        self.quantity_in_stock=quantity_in_stock
    
    @abstractmethod 
    def calculate_price(self):
        pass
    @abstractmethod 
    def display_info(self):
        pass
class MasalaChai(Chai):
    def calculate_price(self):
        return self.base_price+10
    def display_info(self):
        print(f"name: {self.name} and base price is {self.base_price} and stock {self.quantity_in_stock}")
class GingerChai(Chai):
    def calculate_price(self):
        return self.base_price+8
    def display_info(self):
            print(f"name: {self.name} and base price is {self.base_price} and stock {self.quantity_in_stock}")

class ElaichiChai(Chai):
    def calculate_price(self):
        return self.base_price+12
    
    def display_info(self):
            print(f"name: {self.name} and base price is {self.base_price} and stock {self.quantity_in_stock}")

chai1 = MasalaChai("Masala Chai", 20, 50)
chai2 = GingerChai("Ginger Chai", 18, 40)
chai3 = ElaichiChai("Elaichi Chai", 25, 30)

chai1.display_info()
chai2.display_info()
chai3.display_info()
