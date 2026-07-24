#Task 3
import csv
with open ("csv/employees.csv","r") as file:
    content = csv.reader(file)
    print(content)
    employee_info= [employee for employee in content if employee[0] != "employee_id"]                
    full_names = [employee [1]+ " " + employee[2] for employee in employee_info]
    names_with_e = [name for name in full_names if "e" in name]
    print(names_with_e)