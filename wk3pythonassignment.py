def calculate_discount(price, discount_percent):
    """
    Returns the final price after applying the discount if discount_percent >= 20.
    Otherwise, returns the original price.
    """
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    else:
        return price

if __name__ == "__main__":
    try:
        price = float(input("Enter the original price: "))
        discount_percent = float(input("Enter the discount percentage: "))
        final_price = calculate_discount(price, discount_percent)
        if final_price != price:
            print(f"Final price after discount: {final_price:.2f}")
        else:
            print(f"No discount applied. Original price: {price:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values for price and discount percentage.")
