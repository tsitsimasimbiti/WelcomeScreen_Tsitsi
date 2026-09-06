# Question 1
while True:
    try:
        age = int(input("Please enter your age: "))
        print(f"Your age is {age}.")
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Question 2

# List of favourite fruits
fruits = ["Apple", "Banana", "Orange", "Mango", "Guava"]

# Write fruits to file
with open("fruits.txt", "w") as file:
    for fruit in fruits:
        file.write(fruit + "\n")

# Read and display contents of the file
print("Contents of fruits.txt:")
with open("fruits.txt", "r") as file:
    for line in file:
        print(line.strip())

#Question 3

student_marks = {
    "Tatenda": 85,
    "Monica": 92,
    "Miriam": 78,
    "Brian": 95,
    "Tinashe": 88}

print("Student Marks")
for student, mark in student_marks.items():
    print(student, ":", mark)

# Find highest mark
top_student = max(student_marks, key=student_marks.get)
highest_mark = student_marks[top_student]

print(f"\nTop Student: {top_student} with {highest_mark} marks")

#Question 3 (ii)

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ${self.price}")
        print("-" * 30)

# Create book objects
book1 = Book("Python Programming", "John Smith", 15.99)
book2 = Book("Database Systems", "Jane Doe", 12.50)

# Display details
book1.display_details()
book2.display_details()

#Question 4

# Sample log entries
logs = [
    "2026-08-01 ERROR Database connection failed",
    "2026-08-02 INFO User login successful",
    "2026-08-03 ERROR File not found",
    "2026-08-04 INFO Backup completed",
    "2026-08-05 ERROR Network timeout"
]

def process_logs(log_entries):
    error_count = 0

    print("Log Analysis Report")
    print("=" * 30)

    for log in log_entries:
        print(log)

        if "ERROR" in log:
            error_count += 1

    print("\nTotal Errors:", error_count)

process_logs(logs)