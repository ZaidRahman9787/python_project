import sys

ALLOWED_CATEGORIES = ["Electronics", "Grocery", "Clothing"]
PAYMENT_METHODS = ["UPI", "Card", "COD"]

products = {
    101: {"name": "Laptop", "price": 55000, "category": "Electronics"},
    102: {"name": "Headphones", "price": 2000, "category": "Electronics"},
    201: {"name": "Rice Bag", "price": 1200, "category": "Grocery"},
    301: {"name": "T-Shirt", "price": 800, "category": "Clothing"},
}

def display_products():
    print("\nAvailable Products:")
    print("-" * 60)
    print(f"{'ID':<6}{'Name':<15}{'Price(₹)':<12}{'Category'}")
    print("-" * 60)
    for pid, data in products.items():
        print(f"{pid:<6}{data['name']:<15}{data['price']:<12}{data['category']}")
    print("-" * 60)

def calculate_discount(total, payment_method):
    discount = 0
    if total >= 5000:
        discount = 20
    elif total >= 2000:
        discount = 10
    if payment_method == "Card" and total > 30000:
        discount += 5
    return discount

def admin_panel():
    while True:
        print("\n--- ADMIN PANEL ---")
        print("1. View Products")
        print("2. Add New Product")
        print("3. Exit to Main Menu")

        choice = input("Choose an option: ")

        if choice == "1":
            display_products()

        elif choice == "2":
            try:
                pid = int(input("Enter Product ID: "))
                if pid in products:
                    print("❌ Product ID already exists!")
                    continue

                name = input("Enter Product Name: ").strip()
                price = float(input("Enter Price: "))
                category = input("Enter Category: ").strip().title()

                if category not in ALLOWED_CATEGORIES:
                    print("❌ Invalid category!")
                    continue

                products[pid] = {
                    "name": name,
                    "price": price,
                    "category": category
                }
                print("✅ Product added successfully!")

            except ValueError:
                print("❌ Invalid input! Please try again.")

        elif choice == "3":
            break

        else:
            print("❌ Invalid choice!")

def customer_panel():
    name = input("\nEnter your name: ").strip()
    if not name:
        print("❌ Name cannot be empty.")
        return

    cart = {}
    categories_purchased = set()
    total = 0

    while True:
        display_products()
        choice = input("Enter Product ID to add (or 'done' to checkout): ").strip()

        if choice.lower() == "done":
            break

        try:
            pid = int(choice)
            if pid not in products:
                print("❌ Invalid Product ID!")
                continue

            qty = int(input("Enter quantity: "))
            if qty <= 0:
                print("❌ Quantity must be positive!")
                continue

            product = products[pid]
            cart[pid] = cart.get(pid, 0) + qty
            total += product["price"] * qty
            categories_purchased.add(product["category"])

            print("✅ Item added to cart!")

        except ValueError:
            print("❌ Invalid input!")

    if not cart:
        print("❌ Cart is empty.")
        return

    payment_method = input("Select Payment Method (UPI/Card/COD): ").strip().title()
    if payment_method not in PAYMENT_METHODS:
        print("❌ Invalid payment method.")
        return

    order_status = "Order Successful"
    if payment_method == "COD" and "Electronics" in categories_purchased:
        order_status = "Order Not Allowed"

    discount_percent = calculate_discount(total, payment_method)
    discount_amount = (discount_percent / 100) * total
    final_amount = total - discount_amount

    print("\n" + "=" * 50)
    print("🧾 PURCHASE SUMMARY")
    print("=" * 50)
    print(f"Customer Name     : {name}")
    print("\nItems Purchased:")
    print("-" * 50)

    for pid, qty in cart.items():
        p = products[pid]
        print(f"{p['name']} (x{qty}) - ₹{p['price'] * qty}")

    print("-" * 50)
    print(f"Categories        : {', '.join(categories_purchased)}")
    print(f"Payment Method    : {payment_method}")
    print(f"Cart Total        : ₹{total}")
    print(f"Discount Applied  : {discount_percent}%")
    print(f"Final Amount      : ₹{final_amount}")
    print(f"Order Status      : {order_status}")
    print("=" * 50)

def main():
    while True:
        print("\n" + "=" * 30)
        print("SMART CLI SHOPPING SYSTEM")
        print("=" * 30)
        print("1. Admin Panel")
        print("2. Customer Panel")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            admin_panel()
        elif choice == "2":
            customer_panel()
        elif choice == "3":
            print("👋 Exiting system...")
            sys.exit()
        else:
            print("❌ Invalid choice!")

main()
