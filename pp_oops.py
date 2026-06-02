from abc import ABC, abstractmethod

class Fuel:
    def __init__(self, fuel_type: str, price_per_liter: float):
        self.fuel_type = fuel_type
        self.price_per_liter = price_per_liter

    def update_price(self, new_price: float):
        self.price_per_liter = new_price
        return f"Price of {self.fuel_type} updated to {self.price_per_liter:.2f}"
    
    def add_stock(self, liters: float):
        return f"Added {liters:.2f} liters of {self.fuel_type} to stock."
    
    def update_stock(self, liters: float):
        return f"Updated stock of {self.fuel_type} to {liters:.2f} liters."
    

class Petrol(Fuel):
    pass

class Diesel(Fuel):
    pass

class customer:
    def __init__(self, name: str, customer_id: str):
        self.name = name
        self.customer_id = customer_id

    def update_name(self, new_name: str):
        self.name = new_name
        return f"Customer name updated to {self.name}"
    
    def update_customer_id(self, new_id: str):
        self.customer_id = new_id
        return f"Customer ID updated to {self.customer_id}"
    
class employee:
    def __init__(self, name: str, employee_id: str):
        self.name = name
        self.employee_id = employee_id

    def update_name(self, new_name: str):
        self.name = new_name
        return f"Employee name updated to {self.name}"
    
    def update_employee_id(self, new_id: str):
        self.employee_id = new_id
        return f"Employee ID updated to {self.employee_id}"
    

class payment(ABC):
    @abstractmethod
    def process_payment(self, amount: float):
        pass

class cash_payment(payment):
    def process_payment(self, amount: float):
        return f"Processed cash payment of {amount:.2f}"
    
class card_payment(payment):
    def process_payment(self, amount: float):
        return f"Processed card payment of {amount:.2f}"
    
class mobile_payment(payment):
    def process_payment(self, amount: float):
        return f"Processed mobile payment of {amount:.2f}"
    

class petrol_pump:
    def __init__(self, pump_id: str, location: str):
        self.pump_id = pump_id
        self.location = location
        self.__total_sales = 0.0  # private attribute to track total sales

    def update_location(self, new_location: str):
        self.location = new_location
        return f"Petrol pump location updated to {self.location}"
    
    def update_pump_id(self, new_id: str):
        self.pump_id = new_id
        return f"Petrol pump ID updated to {self.pump_id}"
    
    def fill_fuel(self, customer: customer, fuel: Fuel, liters: float, payment_method: payment):

        if liters <= 0:
            return "Liters must be greater than zero."
        
        if not fuel.update_stock(liters):
            return f"Not enough {fuel.fuel_type} in stock to fill {liters:.2f} liters."
    
        
        bill_amount = fuel.price_per_liter * liters
        payment_result = payment_method.process_payment(bill_amount)
        self.__total_sales += bill_amount
        return f"Filled {liters:.2f} liters of {fuel.fuel_type} for customer {customer.name}. {payment_result}"
