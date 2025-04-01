def calculate_discount(price, discount_percent):
    """Calculates the final price after applying a discount."""
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
    else:
        final_price = price  # No discount applied
    return final_price

# Prompt user for inputs
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate and print the final price
final_price = calculate_discount(price, discount_percent)
print(f"The final price after applying the discount is: ${final_price:.2f}")