
def calculate_bill(liters:float, price_per_liter:float = 118.9) -> float:
    return liters * price_per_liter
    
def calculate_discount(bill_amount:float) -> float:
    if bill_amount > 500:
        return bill_amount * 0.1
    elif bill_amount > 300:
        return bill_amount * 0.05
    else:
        return 0.0

def loyalty_points(bill_amount:float) -> int:
    return int(bill_amount // 100)

petrol_liters = float(input("Enter petrol in liters: "))
bill_amount = calculate_bill(petrol_liters)

discounted_amount =  bill_amount - calculate_discount(bill_amount)

points = loyalty_points(discounted_amount)
print(f"Loyalty Points Earned: {points}")
print(f"Bill Amount: {bill_amount:.2f}")
print(f"Discount: {discounted_amount:.2f}")