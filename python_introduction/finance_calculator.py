monthly_income_str = int(input("Enter your monthly income: "))
total_monthly_expenses_str = int(input("Enter your total monthly expenses: "))


monthly_income = float(monthly_income_str)
total_monthly_expenses = float(total_monthly_expenses_str)
monthly_savings = monthly_income - (total_monthly_expenses)

annual_savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)

print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${annual_savings}")

