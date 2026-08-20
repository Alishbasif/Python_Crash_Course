# Student Result Management Program

# Store multiple students using a dictionary
students = {
    "Ali": {
        "Math": 85,
        "English": 78,
        "Science": 90
    },
    "Sara": {
        "Math": 72,
        "English": 88,
        "Science": 80
    },
    "Ahmed": {
        "Math": 45,
        "English": 55,
        "Science": 40
    }
}

# Set to store unique subjects
subjects = set()

# Add subjects to the set
subjects.add("Math")
subjects.add("English")
subjects.add("Science")

# Display all students
print("Students:", students.keys())

# Process each student's result
for name, marks in students.items():

    # Calculate total and average marks
    total = sum(marks.values())
    average = total / len(marks)

    # Determine Pass or Fail
    if average >= 50:
        result = "Pass"
    else:
        result = "Fail"

    print("\nStudent:", name)
    print("Subjects and Marks:", marks)
    print("Total Marks:", total)
    print("Average Marks:", average)
    print("Result:", result)

# Use dictionary get() method
print("\nAli's Math Marks:", students.get("Ali").get("Math"))

# Display dictionary values
print("Student Records:", students.values())

# Display dictionary items
print("Student Details:", students.items())

# Create another set of subjects
other_subjects = {"Math", "English", "Computer"}

# Union: combine unique subjects from both sets
all_subjects = subjects.union(other_subjects)
print("\nUnion of Subjects:", all_subjects)

# Intersection: find common subjects
common_subjects = subjects.intersection(other_subjects)
print("Common Subjects:", common_subjects)