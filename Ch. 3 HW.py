"""
Program: Employee's total weekly pay
Author: JJ Hernandez
Last date modified:2/4/2024
"""
down_payment_rate = 0.10
annual_interest_rate = 0.12
monthly_payments_rate = 0.05

purchase_price = float(input("Enter the purchase price: "))

if purchase_price <= 0:
    print("Invalid purchase price. Please enter a positive value.")
else:
    month = 1
    starting_balance = purchase_price - (purchase_price * down_payment_rate)
    monthly_payment = starting_balance * monthly_payments_rate
    monthly_interest_rate = annual_interest_rate / 12
    print("\n%s%19s%18s%19s%10s%17s" % ("Month", "Starting Balance", "Interest to Pay", "Principal to Pay", "Payment", "Ending Balance"))

    while starting_balance > 0:

        if starting_balance < monthly_payment:
            principal_to_pay = starting_balance
            monthly_payment = starting_balance
            interest_to_pay = 0
        else:
            interest_to_pay = starting_balance * monthly_interest_rate
            principal_to_pay = monthly_payment - interest_to_pay

        ending_balance = starting_balance - principal_to_pay

        print("%2d%16.2f%16.2f%18.2f%18.2f%15.2f" % (month, starting_balance, interest_to_pay, principal_to_pay, monthly_payment, ending_balance))

        starting_balance = ending_balance
        month = month + 1