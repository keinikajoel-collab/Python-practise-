#(a) positive, negative or zero

#prompt the user to input a number and convert it to a float
number = float(input("Enter a number: "))

# check the condition using if, elif and else
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

print("-" * 40) # Separator lines for clear output if running the whole file.

# (b) Grading system
# ask the user for their exam mark
mark = float(input("Enter your exam mark (0-100):"))

# determine the grade using a conditional structure
if mark >= 70:
    print("Grade: A")
elif mark >= 60:
    print("Grade: B")
elif mark >= 50:
    print("Grade C")
elif mark >= 40:
    print("Grade: D")
else:
    print("Grade: F")

print("-" * 40)

# (c) Nested comparison
# Read two numbers from the user
i = float(input("Enter first number (i): "))
j = float(input("Enter second number (j):"))

# use nested if statements to compare the two numbers
if i == j:
    print("Equal")
else:
    if i>j:
        print("i greater")
    else:
        print("j greater")