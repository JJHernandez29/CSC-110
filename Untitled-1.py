"""
Program: Employee's total weekly pay
Author: JJ Hernandez
Last date modified:2/4/2024
"""

hourly_wage = int(input("Please enter your hourly wage:"))
regular_hours = int(input("Please enter your work hours:"))
overtime_hours = int(input("Please enter your overtime hours:"))
total_weekly_pay = int(hourly_wage * regular_hours + (float(hourly_wage * 1.5 * overtime_hours)))
print("Your total weekly pay is:$", total_weekly_pay, "this week")
