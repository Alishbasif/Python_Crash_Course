# Student Information Dictionary

# Create a dictionary to store student information
student = {
    "name": "Alishba",
    "age": 20,
    "cgpa": 3.5,
    "marks": {
        "Python": 85,
        "Math": 78,
        "English": 82
    }
}

# Access different values from the dictionary
print("Name:", student["name"])
print("Age:", student["age"])
print("CGPA:", student["cgpa"])

# Access marks of a specific subject
print("Python Marks:", student["marks"]["Python"])

# Add a new key to the dictionary
student["city"] = "Karachi"

# Update an existing value
student["cgpa"] = 3.7

# Use keys() method
print("\nKeys:", student.keys())

# Use values() method
print("Values:", student.values())

# Use items() method
print("Items:", student.items())

# Use get() method
print("Name using get():", student.get("name"))
print("City using get():", student.get("city"))

# Display updated student information
print("\nUpdated Student Information:")
print(student)