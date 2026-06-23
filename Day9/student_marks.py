students = ["Ram", "Shyam", "Sita", "Gita", "Hari"]
num_students = len(students)

total_percentage = 0

for student in students:
    total_marks = 500
    marks = int(input(f"Enter marks for {student} out of {total_marks}: "))    
    percentage = (marks / total_marks) * 100
    print(f"{student}'s Percentage: {percentage:.2f}%")
    total_percentage += percentage

print(f"Overall Percentage of College: {total_percentage / num_students:.2f}%")