# Write a program to calculate the credit card balance after one year if 
# a person only pays the minimum monthly payment required by the credit 
# card company each month.

# The following variables contain values as described below:

# 1. balance - the outstanding balance on the credit card
# 2. annualInterestRate - annual interest rate as a decimal
# 3. monthlyPaymentRate - minimum monthly payment rate as a decimal

# For each month, calculate statements on the monthly payment and remaining balance. 
# At the end of 12 months, print out the remaining balance. Be sure to print 
# out no more than two decimal digits of accuracy - so print

# Remaining balance: 813.41

# instead of

# Remaining balance: 813.4141998135 

# So your program only prints out one thing: the remaining balance at the end 
# of the year in the format:

# Remaining balance: 4784.0
# A summary of the required math is found below:

# Monthly interest rate= (Annual interest rate) / 12.0
# Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
# Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
# Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x 
# Monthly unpaid balance)

# Paste your code into this box
month = 0
totalPay = 0
monthlyInterestRate = annualInterestRate / 12.0
while month <12:
    minPay = monthlyPaymentRate * balance
    unpayBal = balance - minPay
    totalPay += minPay
    balance = unpayBal + (monthlyInterestRate * unpayBal)
    month += 1
print(' Remaining balance: ' + str(round(balance,2)))