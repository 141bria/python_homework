# Task 2
import csv
import os
def read_employees ():
    fields = [ ]
    rows = [ ]
    employees = { }
    try:
        with open("../csv/employees.csv") as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader):
                if index == 0:
                    fields = row
                else:
                    rows.append(row)
        employees["fields"] = fields
        employees["rows"] = rows
        return employees

    except Exception as e:
        print(f"Exception type: {type (e).__name__}")
        print(f"Exception message: {e}")
employees = read_employees()

#Task 3
def column_index(column_name):
    return employees["fields"].index(column_name)
employee_id_column = column_index("employee_id")

#Task 4
def first_name(row_num):
    first_name_column = column_index("first_name")
    employee_first_name = employees["rows"][row_num][first_name_column]
    return employee_first_name

# Task5

def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column])== employee_id
    matches = list(filter(employee_match,employees["rows"]))
    return matches

#Task 6
def employee_find_2(employee_id):
    matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id, employees["rows"]))
    return matches

#Task 7
def sort_by_last_name ():
    last_name_column = column_index("last_name")
    employees["rows"].sort(key=lambda row:row[last_name_column])
    return employees ["rows"]
#Task 8
def employee_dict(row):
    employee = {}
    for index in range (len(row)):
        if employees ["fields"][index] != "employee_id":
            employee[employees["fields"][index]] = row[index]
    return employee
#Task 9
def all_employees_dict():
    all_employees={ }
    for row in employees["rows"]:
        all_employees[row[employee_id_column]] = employee_dict(row)
    return all_employees
#Task 10
def get_this_value():
    return os.getenv("THISVALUE")
#Task 11
import custom_module
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)
if __name__ == "__main__":
    set_that_secret("pizza")
    print (custom_module.secret)

#Task 12
def read_csv(filename):
    fields = []
    rows = []
    data = {}
    with open (filename) as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader):
                if index == 0:
                    fields=row
                else:
                    rows.append(tuple(row))
    data["fields"]=fields
    data["rows"]=rows
    return data

def read_minutes():
    minutes1= {}
    minutes2= {}
    minutes1= read_csv("../csv/minutes1.csv")
    minutes2= read_csv("../csv/minutes2.csv")
    return minutes1,minutes2
minutes1,minutes2 = read_minutes()

#Task 13
def create_minutes_set():
    minutes1_set=set(minutes1["rows"])
    minutes2_set=set(minutes2["rows"])
    minutes_set= minutes1_set | minutes2_set
    return minutes_set
minutes_set=create_minutes_set()

#Task 14
from datetime import datetime

def create_minutes_list():
    minutes_list=list(minutes_set)
    minutes_list= list(map (lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")),minutes_list))
    return minutes_list
minutes_list=create_minutes_list()

#Task 15
def write_sorted_list():
    minutes_list.sort(key=lambda x: x[1])
    string_mintues = list(map( lambda x: (x[0],x[1].strftime("%B %d, %Y")),minutes_list
    ))
    with open("./minutes.csv","w") as file:
        writer= csv.writer(file)
        writer.writerow(minutes1["fields"])
        writer.writerows(string_mintues)
    return string_mintues
write_sorted_list()
