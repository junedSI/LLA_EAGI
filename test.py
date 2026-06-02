class PetrolPump:
    def __init__(self, petrol_in_liters: float, price: float = 118.9, petrol_pump_id: str = "PP001"):
        self.petrol_in_liters = petrol_in_liters
        self.price = price
        self.petrol_pump_id = petrol_pump_id

    def calculate_bill(self) -> float:
        return self.petrol_in_liters * self.price
    
    def calculate_discount(self, bill_amount: float) -> float:
        if bill_amount > 1000:
            return bill_amount * 0.1  # 10% discount
        return 0  # No discount
    
    def loyalty_points(self, bill_amount: float) -> int:
        return int(bill_amount // 100)  # 1 point for every 100 currency units spent
    
    def log_transaction(self):
        bill_amount = self.calculate_bill()
        discount = self.calculate_discount(bill_amount)
        final_amount = bill_amount - discount
        points = self.loyalty_points(final_amount)

        log_entry = f"{self.petrol_pump_id},{self.petrol_in_liters:.2f},{bill_amount:.2f},{discount:.2f},{final_amount:.2f},{points}\n"
        
        with open("petrol_pump_transactions.csv", "a") as file:
            file.write(log_entry)

    def generate_recipt(self):
        bill_amount = self.calculate_bill()
        discount = self.calculate_discount(bill_amount)
        final_amount = bill_amount - discount
        points = self.loyalty_points(final_amount)

        receipt = (
            f"Petrol Pump ID: {self.petrol_pump_id}\n"
            f"Liters Purchased: {self.petrol_in_liters:.2f} L\n"
            f"Price per Liter: {self.price:.2f}\n"
            f"Total Bill: {bill_amount:.2f}\n"
            f"Discount: {discount:.2f}\n"
            f"Final Amount: {final_amount:.2f}\n"
            f"Loyalty Points Earned: {points}\n"
        )
        return receipt
    
# Example usage
petrol_liters = float(input("Enter petrol in liters: "))
pump = PetrolPump(petrol_in_liters=petrol_liters, petrol_pump_id="PP002")
pump.log_transaction()
print(pump.generate_recipt())