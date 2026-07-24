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
additional_employees.json = [
    'Name':["Eve","Frank"],
    'Age': [28,40],
    'City':["Miami","Seattle"]
    'Salary':[60000,95000]
]