```python
# Python Week 1 Assignment
# Student Grade Calculator

print("===================================")
print("       STUDENT GRADE CALCULATOR")
print("===================================")

# Get user input
name = input("Enter your name: ")
marks = float(input("Enter your marks (0-100): "))

# Calculate grade
if marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "E"

# Display the result using f-strings
print("\n===================================")
print("             RESULT")
print("===================================")
print(f"Student Name : {name}")
print(f"Marks        : {marks}")
print(f"Grade        : {grade}")
print("===================================")

# Final message
print(f"Congratulations {name}, you scored {marks} marks and received grade {grade}.")
```
