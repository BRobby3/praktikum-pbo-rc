# Create an empty dictionary
student_grades = {}

# Get the number of students
n = int(input("Enter the number of students: "))

# Loop
for i in range(n):
		# Input student name and grade score
		name = input(f"Enter the name of student {i+1}: ")
		grade = float(input(f"Enter the grade score of student {i+1}: "))

		# Insert name and grade into dictionary
		student_grades[name] = grade

# Print the dictionary
print(student_grades)
