# (a) Square a number

def square_number():
    val = float(input("Enter a number to square: "))
    result = val ** 2 
    print(f"The square of {val} is {result}")


print("Testing square_number()")
square_number()


#(b) student averages
def get_average(marks):
    return sum(marks) /len(marks)

def main_student_averages():
    for i in range(1, 4):
        print(f"\n  Data Entry for student {i}  ")

        student_marks = []
        for m in range(3):
            mark = float(input(f"Enter mark {m+1}: "))
            student_marks.append(mark)

        avg = get_average(student_marks)
        print(f"student {i} Average Mark: {avg:.2f}")

print(" Testing student averages  ")
main_student_averages()

#(c) counting even numbers

def count_even(numbers):
    even_count = 0
    for n in numbers:
        if n % 2 == 0:
            even_count += 1
    return even_count

sample_list = [11, 22, 33, 44, 55, 66, 77, 88, 90]
print(f"Sample list:{sample_list}")
total_evens = count_even(sample_list)
print(f"Number of even items in list: {total_evens}")