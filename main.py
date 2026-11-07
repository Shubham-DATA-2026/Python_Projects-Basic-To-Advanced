# Student Marks Calculator

name = input("Enter your name: ")

python = int(input("Enter Python marks: "))
dbms = int(input("Enter DBMS marks: "))
dsa = int(input("Enter DSA marks: "))
emsd = int(input("Enter EMSD marks: "))
cs = int(input("Enter CS marks: "))

# Calculate total
total = python + dbms + dsa + emsd + cs

# Calculate percentage
percentage = (total / 500) * 100

# Calculate grade
if percentage >= 90:
    grade = "O"
elif percentage >= 80:
    grade = "A++"
elif percentage >= 70:
    grade = "A"
elif percentage >= 60:
    grade = "B++"
elif percentage >= 50:
    grade = "B"
elif percentage >= 40:
    grade = "C++"
else:
    grade = "F"

# Display result
print("\n--- Student Result ---")
print("Name:", name)
print("Total:", total, "/ 500")
print("Percentage:", percentage, "%")
print("Grade:", grade)
