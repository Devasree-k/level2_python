

employee_name = input("Enter Employee name : ")
basic_salary = float(input("Enter the Basic Salary : "))
experience = int(input("Enter your experience : "))

if basic_salary > 20000:
    da = basic_salary * 58.5/100 
    hra = basic_salary * 15.0/100
elif basic_salary > 15000:
    da = basic_salary * 0.46/100 
    hra = basic_salary * 0.12/100
else:
    da= basic_salary * 0.425
    hra= 1500

gross = basic_salary + hra + da


if experience > 10:
    bonus = 20000
elif experience > 5:
    bonus = 12000
elif experience > 2:
    bonus = 8000
else:
    bonus = 2000

total_salary = gross + bonus

if total_salary > 50000:
    category = "High salary"
elif total_salary > 25000:
    category = "Medium Salary"
elif total_salary > 10000:
    category = "Low Salary"
else:
    category = "Fresher / Trainee"

print("\nEmployee Details ")
print("Employee Name : ", employee_name)
print("Basic Salary : ", basic_salary)
print("Experience : ", experience)
print("Gross Salary : ", gross)
print("Bonus Salary : ", bonus)
print("Salary with bonus :" , total_salary)
print("Category : ",category)


