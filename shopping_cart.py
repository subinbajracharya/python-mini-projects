# Shopping Cart Program

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food name to purchase or C to Checkout: ").lower()

    # Check if food input is a number
    if food == "c":
        break
    elif food.replace('.', '', 1).isdigit() or food.isdigit():
        print("Invalid input! Please enter a valid food name, not a number.")
        continue
    else:
        while True:
            try:
                # Ask for the price and ensure it's a valid number (integer or float)
                price = float(input(f"Enter the price of a {food}: $"))
                if price <= 0:
                    print("Price must be greater than zero. Please enter a valid price.")
                    continue
                break  # Exit the loop if price is valid
            except ValueError:
                print("Invalid input! Please enter a valid number for the price.")

        foods.append(food)
        prices.append(price)

# Check if the cart is empty
if not foods:
    print("Your cart is empty")
else:
    print("----- YOUR CART -----")

    for food, price in zip(foods, prices):
        print(f"{food} - ${price}")

    for price in prices:
        total += price

    print(f"\nYour total is ${total}")
