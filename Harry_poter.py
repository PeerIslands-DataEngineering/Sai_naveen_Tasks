from collections import ChainMap, namedtuple, defaultdict

# Point logs by professors
snape_log = {'Harry': 10, 'Hermione': 20}
mcgonagall_log = {'Harry': 5, 'Ron': 15}
flitwick_log = {'Luna': 25}

# Student records
Student = namedtuple('Student', ['name', 'house', 'year'])
students = [
    Student('Harry', 'Gryffindor', 5),
    Student('Hermione', 'Gryffindor', 5),
    Student('Ron', 'Gryffindor', 5),
    Student('Luna', 'Ravenclaw', 4)
]

# Step 1: Combine all logs using ChainMap
combined_logs = ChainMap(snape_log, mcgonagall_log, flitwick_log)

# Step 2: Compute total points per house
house_points = defaultdict(int)

for student in students:
    points = combined_logs.get(student.name, 0)
    house_points[student.house] += points

# Step 3: Find the house with the highest total points
top_house = max(house_points.items(), key=lambda x: x[1])[0]
print(top_house)
