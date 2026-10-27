# ==========================================
# (a) Square a Number
# ==========================================
def square_number(number):
    return number ** 2

# Testing/Calling Part (a)
print("--- Part (a): Square a Number ---")
user_val = float(input("Enter a number to square: "))
result = square_number(user_val)
print(f"The square of {user_val} is {result}")

print("\n" + "="*40 + "\n")


# ==========================================
# (b) Student Averages
# ==========================================
def get_average(marks):
    # Receives a list of marks and returns the average
    return sum(marks) / len(marks)

print("--- Part (b): Student Averages ---")
# Main program logic tracking 3 students
for student in range(1, 4):
    print(f"\nEntering details for Student {student}:")
    student_marks = []
    
    # Simulating a dynamic list entry for a student's marks (e.g., 3 subjects)
    for i in range(3):
        mark = float(input(f"  Enter mark for subject {i+1}: "))
        student_marks.append(mark)
        
    avg = get_average(student_marks)
    print(f"--> Average mark for Student {student} is: {avg:.2f}")

print("\n" + "="*40 + "\n")


# ==========================================
# (c) Counting Even Numbers
# ==========================================
def count_even(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:  # If the remainder when divided by 2 is 0, it's even
            count += 1
    return count

print("--- Part (c): Counting Even Numbers ---")
# Test list of choice
sample_list = [12, 7, 23, 44, 56, 89, 90, 3]
even_count = count_even(sample_list)

print(f"Sample list: {sample_list}")
print(f"Total number of even numbers in the list: {even_count}")
