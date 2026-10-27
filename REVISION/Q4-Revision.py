#(a) numbered name list
names = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]

for index, name in enumerate(names, start=1):
    print(f"{index}. {name}")

#(b)largest and total

#store the given test numbers
numbers_list = [12, 45, 7, 23, 56, 89, 34]

#initialize tracking variables without using max() or sum()
largest = numbers_list[0]
total_sum = 0

