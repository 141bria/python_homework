#Task 1
import pandas as pd
data={
'Name':["Alice","Bob","Charlie"],
'Age':[25,30,35],
'City':["New York","Los Angeles","Chicago"]
}
df = pd.DataFrame(data)
print(df)
task1_data_frame = df
task1_with_salary = task1_data_frame.copy()
task1_with_salary['Salary']=[70000,80000,90000]
print(task1_with_salary)
task1_older = task1_with_salary.copy()
task1_older['Age'] = task1_older["Age"]+1
print(task1_older)
task1_older.to_csv("employees.csv",index=False)

#Task 2
import json
with open('assignment4/additional_employees.json') as file:
    json_data = json.load(file)
    json_employees = pd.DataFrame(json_data)
task2_employees = pd.read_csv("employees.csv")
print(task2_employees)
print(json_employees)

more_employees = pd.concat([task2_employees,json_employees],ignore_index=True)

#Task 3
first_three = more_employees.head(3)
last_two = more_employees.tail(2)
employee_shape = more_employees.shape
print(first_three.head(3))
print(more_employees.tail(2))
print(employee_shape)
print(more_employees.info())

#Task 4
dirty_data = pd.read_csv('assignment4/dirty_data.csv')
print(dirty_data)
clean_data = dirty_data.copy()
clean_data = clean_data.drop_duplicates()
print(clean_data)
clean_data["Age"]= pd.to_numeric(clean_data["Age"],errors="coerce")
print(clean_data)
clean_data["Salary"] = clean_data["Salary"].replace(["unknown","n/a"],pd.NA)
clean_data["Salary"]=pd.to_numeric(clean_data["Salary"],errors="coerce")
print(clean_data)
age_mean = clean_data["Age"].mean()
print(age_mean)
salary_median = clean_data["Salary"].median()
clean_data["Age"] =  clean_data["Age"].fillna(age_mean)
clean_data["Salary"] =  clean_data["Salary"].fillna(salary_median)
print(salary_median)
clean_data["Hire Date"] = pd.to_datetime(clean_data["Hire Date"],format="mixed",errors="coerce")
clean_data["Name"]=clean_data["Name"].str.strip()
clean_data["Department"]=clean_data["Department"].str.strip().str.upper()
print(clean_data)
print(clean_data['Hire Date'])