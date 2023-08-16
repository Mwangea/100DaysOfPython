shopping_list = []

while True:
    item = input("Enter an item (or 'done' to finish): ")
    if item.lower() == 'done':
        break
    
    try:
        price = float(input(f"Enter the price of {item}: "))
        shopping_list.append((item, price))
    except ValueError:
        print("Invalid price. Please enter a valid number.")

total_cost = 0
for _, price in shopping_list:
    total_cost += price

print("\nShopping List:")
for item, price in shopping_list:
    print(f"{item}: ${price:.2f}")

print(f"Total cost: ${total_cost:.2f}")
