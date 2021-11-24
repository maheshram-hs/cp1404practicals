"""
CP1404/CP5632 - Practical 01
Maheshram Shunmuganand - Electricity Bill
Estimates the electric bill.
"""

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator 2.0")
# Get the data to calculate.
tariff = int(input("Which tariff? 11 or 31: "))
kwh_per_day = float(input("Enter daily use in kWh: "))
number_of_days = int(input("Enter number of billing days: "))

# Calculate the estimate electric bill amount.
if tariff == 11:
    cents_per_kwh = TARIFF_11
elif tariff == 31:
    cents_per_kwh = TARIFF_31
estimation = cents_per_kwh * kwh_per_day * number_of_days
print("Estimated bill: ${:.2f}".format(estimation))
