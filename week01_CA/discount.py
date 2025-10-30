# Title: W01 Code-along Project: discount
# Author: Nicholas Nixon
# Class: CSE 111
# Instructor: Thomas Reid
# Date: October 2025

from datetime import datetime

DISCOUNT_DAYS = [2,3]
DISCOUNT_RATE = 0.1
TAX_RATE = 0.06
today = datetime.now()
dow = today.weekday()
subtotal = 0
quantity = 1
while quantity != 0:
    quantity = int(input("Enter the quantity: "))
    if quantity != 0:
        price = float(input("Enter the price: "))
        subtotal += quantity * price
        
print(f"Total order ${subtotal:.2f}")
discount = 0
if dow in DISCOUNT_DAYS:
    if subtotal >= 50:
        discount = round(subtotal * DISCOUNT_RATE,2)
    else:
        short = 50 - subtotal
        print(f"You can get a discount by ordering ${short:.2f} more.")
        
print(f"Discount ${discount:.2f}")
subtotal -= discount
tax = round(subtotal * TAX_RATE,2)
total = subtotal + tax

print(f"Tax {tax:.2f}")
print(f"Total Due ${total:.2f}")