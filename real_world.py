sales = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200]
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

month = input("enter month to calculate total sales: ")
months_index = months.index(month) if month in months else -1

def total_sales(index: int) -> float:
    if index == len(sales):
        return 0
    else:
        return sales[index] + total_sales(index + 1)

total = total_sales(months_index)
print(f"Total sales from {month} to {months[-1]}: {total:.2f}")