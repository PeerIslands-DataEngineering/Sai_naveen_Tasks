import pandas as pd

data = {
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hannah'],
    'Department': ['HR', 'IT', 'IT', 'HR', 'Finance', 'Finance', 'IT', 'HR'],
    'Age': [25, 32, 29, 41, 37, 45, 26, 38],
    'Salary': [50000, 70000, 65000, 80000, 75000, 90000, 62000, 85000],
    'Experience': [2, 7, 5, 15, 10, 20, 3, 12]
}

df = pd.DataFrame(data)

print(df)

departments = list(set(df['Department']))

print("average salary in each department:")
for dept in departments:
    total = 0
    count = 0
    for i in range(len(df)):
        if df['Department'][i] == dept:
            total += df['Salary'][i]
            count += 1
    if count != 0:
        avg = total / count
        print(dept, ":", avg)


print("highest-paid employee in each department:")
for dept in departments:
    max_salary = 0
    top_employee = ""
    for i in range(len(df)):
        if df['Department'][i] == dept:
            if df['Salary'][i] > max_salary:
                max_salary = df['Salary'][i]
                top_employee = df['Employee'][i]
    print(dept, ":", top_employee, "==", max_salary)


print("Employees with 5 years experience and salary 6500")
count = 0
for i in range(len(df)):
    if df['Experience'][i] > 5 and df['Salary'][i] > 65000:
        print(df['Employee'][i])
        count += 1
print("Total:", count)

