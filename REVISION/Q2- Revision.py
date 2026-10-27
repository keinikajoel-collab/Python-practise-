#(a) even numbers
# loop from 1 to 80. step=1, but we filter with an if statement
for num in range(1, 81):
    if num % 2 == 0:
        print(num)


#(b) muktiplication tables 
print("Multiplcation tables for 1 to 5:")
# outer loop controls the first number (1 to 5)
for i in range(1,6):
    # Inner loop controls the second number (1 to 10 is standard, or up to 5/12 depending on preference)
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()

#(c)input validaton
#loop indefinitely until a positive number is entered
while True:
    user_num = float(input("Enter a positive number: "))

    if user_num > 0:
        print("Confirmation: You successfully entered a vald positive!")
        break
    else:
        print("Invalid input. Please try again.")