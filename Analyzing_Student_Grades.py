import pandas as pd

data = {
    'Student': ['John', 'Sara', 'Mike', 'Anna', 'David', 'Emily', 'Chris', 'Sophia'],
    'Subject': ['Math', 'Science', 'Math', 'Science', 'Math', 'Science', 'Math', 'Science'],
    'Marks': [85, 72, 90, 65, 78, 88, 92, 55],
    'Attendance': [92, 80, 95, 70, 85, 90, 97, 60]  
}

df = pd.DataFrame(data)

subjects = list(set(df['Subject']))
for sub in subjects:
    total = 0
    count = 0
    for i in range(len(df)):
        if df['Subject'][i] == sub:
            total += df['Marks'][i]
            count += 1
    if count != 0:
        avg = total / count
        print(sub, ":", avg)


for i in range(len(df)):
    if df['Marks'][i] > 85 and df['Attendance'][i] < 90:
        print(df['Student'][i])
        
grades = []
for i in range(len(df)):
    m = df['Marks'][i]
    if m >= 90:
        grades.append("A")
    elif m >= 80:
        grades.append("B")
    elif m >= 70:
        grades.append("C")
    else:
        grades.append("D")
df['Grade'] = grades
print(df)

