# ==========================================
# (a) Numbered Name List
# ==========================================
print("--- Part (a): Numbered Name List ---")
# Create a list of 5 student names
names_list = ["Alice", "Brian", "Chloe", "David", "Ethan"]

# Loop through and print numbered 1 to 5
for index in range(len(names_list)):
    print(f"{index + 1}. {names_list[index]}")

print("\n" + "="*40 + "\n")


# ==========================================
# (b) Largest and Total (Without max() or sum())
# ==========================================
print("--- Part (b): Largest and Total ---")
numbers = [12, 45, 7, 23, 86, 89, 34]

# Initialize variables using the first element of the list
largest = numbers[0]
total = 0

for num in numbers:
    total += num         # Accumulating total sum
    if num > largest:    # Checking for new largest item
        largest = num

print(f"Given list: {numbers}")
print(f"Largest number: {largest}")
print(f"Total sum: {total}")

print("\n" + "="*40 + "\n")


# ==========================================
# (c) Filtering a List
# ==========================================
print("--- Part (c): Filtering a List ---")
user_numbers = []

# Ask user for 5 numbers and store them in a list
print("Please enter 5 numbers:")
for i in range(5):
    val = float(input(f"Enter number {i+1}: "))
    user_numbers.append(val)

# Filter items greater than 10
filtered_items = []
for num in user_numbers:
    if num > 10:
        filtered_items.append(num)

print("\n--- Results ---")
print(f"Original List: {user_numbers}")
print(f"Number of items in original list: {len(user_numbers)}")
print(f"Items greater than 10: {filtered_items}")
