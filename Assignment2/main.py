"""
Course: BSE2302	PROFESSIONAL SOFTWARE ENGINEERING MINI PRACTICAL PROJECT II
Assignment2: Ecommerce Split Calculator
Name: Mukisa Ben Ezra
RegNo: 24/U/21328
Date: June 11, 2026
"""


# --- E-commerce Pricing Calculator ---
def calculate_final_price(subtotal, location_tax_rate, coupon_code):
    discount = 0.0

    # Nested conditions for discount levels based on subtotal
    if subtotal >= 200:
        if coupon_code == "SAVE50":
            discount = 50.0
        elif coupon_code == "SAVE20":
            discount = 20.0
        else:
            discount = 10.0  # Standard discount for high orders
    elif subtotal >= 100:
        if coupon_code == "SAVE10":
            discount = 10.0

    # Ensure discount doesn't exceed subtotal
    if discount > subtotal:
        discount = subtotal

    discounted_subtotal = subtotal - discount

    # Nested conditions for tax rates based on location/region
    if location_tax_rate == "local":
        tax = discounted_subtotal * 0.05  # 5% tax
    elif location_tax_rate == "national":
        tax = discounted_subtotal * 0.10  # 10% tax
    elif location_tax_rate == "international":
        tax = discounted_subtotal * 0.15  # 15% tax
    else:
        tax = 0.0  # Default if no valid location matches

    final_price = discounted_subtotal + tax

    print(f"--- Invoice ---")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Discount: -${discount:.2f}")
    print(f"Tax: +${tax:.2f}")
    print(f"Final Price: ${final_price:.2f}\n")
    return final_price


# --- Multi-Level Login System ---
def login_system(username, password):
    # Used dummy credentials and access roles
    users_db = {
        "admin_user": {"password": "admin_pass", "role": "Admin"},
        "cashier_user": {"password": "cashier_pass", "role": "Cashier"},
        "customer_user": {"password": "cust_pass", "role": "Customer"}
    }

    # Check if user exists
    if username in users_db:
        if users_db[username]["password"] == password:
            role = users_db[username]["role"]
            print(f"Login Successful! Welcome {username} (Role: {role})")

            # Access control based on user type
            if role == "Admin":
                print("Access Granted: Admin can access ALL features (Inventory, Users, Sales).")
            elif role == "Cashier":
                print("Access Granted: Cashier can process payments and manage the register.")
            elif role == "Customer":
                print("Access Granted: Customer can browse products and make purchases.")
        else:
            print("Access Denied: Incorrect password.")
    else:
        print("Access Denied: Username not found.")


# --- Testing the Application ---
print(">>> Testing Pricing Logic:")
calculate_final_price(250, "local", "SAVE50")  # High subtotal, valid coupon

print(">>> Testing Login System:")
login_system("admin_user", "admin_pass")
print("")
login_system("customer_user", "wrong_password")