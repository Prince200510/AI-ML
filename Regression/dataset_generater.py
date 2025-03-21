import pandas as pd
import random
import numpy as np

names = [
    "Prince", "Harsh", "Lalit", "Krishna", "Nobita", "Shichan", "Rahul", "Sartak", "Sahil", "Karan",
    "Aman", "Vivek", "Anjali", "Rohit", "Priya", "Sneha", "Raj", "Meena", "Akash", "Simran",
    "Kunal", "Ankit", "Ritika", "Aditya", "Kavita"
]

data = []
for i in range(1, 5001):
    name = random.choice(names) + " " + random.choice(["Sharma", "Patel", "Yadav", "Singh", "Verma", "Gupta"])
    result = random.choice([np.nan] * 5 + list(range(40, 101)))  
    attendance = round(random.uniform(50, 100), 2)  
    assignment_score = random.randint(0, 20)  
    project_marks = random.randint(0, 30)  
    data.append([i, name, result, attendance, assignment_score, project_marks])

df = pd.DataFrame(data, columns=["Roll_No", "Name", "Result", "Attendance", "Assignment_Score", "Project_Marks"])

df.to_csv("student_results_advanced.csv", index=False)
print("✅ 5000 rows generated and saved to 'student_results_advanced.csv'")
