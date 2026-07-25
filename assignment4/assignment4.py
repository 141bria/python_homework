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
task2_employees =  task1_older
print(task2_employees)
import pandas as pd
df = pd.read_json('assignment4/additional_employees.json')
json_employees = pd.read_json('assignment4/additional_employees.json')
print(json_employees)

more_employees = pd.concat([task1_older,json_employees],ignore_index=True)

#Task 3
first_three = more_employees
print(first_three.head(3))
last_two = more_employees
print(more_employees.tail(2))
print(more_employees.info())

#Task 4
df = pd.read_csv('assignment4/dirty_data.csv')
dirty_data = df
print(dirty_data)
clean_data = dirty_data.copy()
clean_data = clean_data.drop_duplicates()
print(clean_data)
clean_data["Age"]= pd.to_numeric(clean_data["Age"],errors="coerce")
clean_data["Age"]=pd.to_numeric(clean_data["Age"])
print(clean_data)
clean_data["Salary"]=pd.to_numeric(clean_data["Salary"],errors="coerce")
clean_data["Salary"]=pd.to_numeric(clean_data["Salary"])
print(clean_data)
age_mean = clean_data["Age"].mean()
print(age_mean)
salary_median = clean_data["Salary"].median()
print(salary_median)
clean_data["Hire Date"] = pd.to_datetime(clean_data["Hire Date"],errors="coerce")
clean_data["Name"]=clean_data["Name"].str.strip()
clean_data["Department"]=clean_data["Department"].str.strip()
#Uppercase
clean_data["Name"]=clean_data["Name"].str.upper()
clean_data["Department"]=clean_data["Department"].str.upper()
print(clean_data)