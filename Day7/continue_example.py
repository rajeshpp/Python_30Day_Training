print('''
for item in sequence:
    if condition:
        continue
''')

students = ["Raj", "Ravi", "Absent", "Sita"]

for student in students:
    if student == "Absent":
        continue

    print("Attendance Marked:", student)