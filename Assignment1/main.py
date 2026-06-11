"""
Course: BSE2302	PROFESSIONAL SOFTWARE ENGINEERING MINI PRACTICAL PROJECT II
Assignment: Bill Split Calculator
Name: Mukisa Ben Ezra
RegNo: 24/U/21328
Date: June 9, 2026
"""


def get_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a non-negative value.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def main():
    print("--- Bill Split Calculator ---")

    bill_amount = get_int_input("Enter the total bill amount (UGX): ")
    num_people = get_int_input("Enter the number of people: ")

    print("\nTip Percentages: 10%, 15%, 20% or enter 0 for a custom amount.")
    tip_choice = get_int_input("Select tip percentage: ")

    if tip_choice == 0:
        tip_percentage = get_int_input("Enter custom tip percentage: ")
    else:
        tip_percentage = tip_choice

    # Calculations
    # Tip is calculated as float then rounded to nearest UGX int
    tip_amount = int(round(bill_amount * (tip_percentage / 100)))
    total_bill = bill_amount + tip_amount
    # Per person amount is rounded up or down to the nearest whole UGX
    amount_per_person = int(round(total_bill / num_people))

    # Output Receipt
    print("\n" + "=" * 35)
    print("           RECEIPT")
    print("=" * 35)
    print(f"Subtotal:          {bill_amount:>10,} UGX")
    print(f"Tip ({tip_percentage:>3}%):        {tip_amount:>10,} UGX")
    print("-" * 35)
    print(f"Total Bill:        {total_bill:>10,} UGX")
    print(f"Number of People:  {num_people:>10}")
    print("-" * 35)
    print(f"Amount Per Person: {amount_per_person:>10,} UGX")
    print("=" * 35)


if __name__ == "__main__":
    main()
