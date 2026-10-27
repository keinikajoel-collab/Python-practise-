# ==========================================
# (a) Even Numbers
# ==========================================
print("--- Part (a): Even Numbers between 1 and 80 ---")
# Using 2 as starting point and stepping by 2 up to 80
for number in range(2, 81, 2):
    print(number)

print("\n" + "="*40 + "\n")

# ==========================================
# (b) Multiplication Tables
# ==========================================
print("--- Part (b): Multiplication Tables (1 to 5) ---")
for row in range(1, 6):
    for col in range(1, 6):
        # Format string to output in the form: 2 x 3 = 6
        print(f"{row} x {col} = {row * col}")
    print("-" * 15)  # Visual separator between tables

print("\n" + "="*40 + "\n")

# ==========================================
# (c) Input Validation
# ==========================================
print("--- Part (c): Input Validation ---")
while True:
    user_num = float(input("Please enter a positive number: "))
    if user_num > 0:
        print("Confirmation: Thank you! You entered a valid positive number.")
        break
    else:
        print("Invalid input. Try again.")
