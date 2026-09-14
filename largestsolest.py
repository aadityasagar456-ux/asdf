New_numbers = []
num_new_elements = 7

print(f"\nPlease enter {num_new_elements} integers to find the smallest and largest:")

# Take 7 integers from the user
for i in range(num_new_elements):
    while True:
        try:
            num = int(input(f"Enter integer {i+1}: "))
            New_numbers.append(num)
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

# Find smallest and largest manu ally
if New_numbers:
    smallest = New_numbers[0]
    largest = New_numbers[0]
    for number in New_numbers:
        if number < smallest:
            smallest = number
        if number > largest:
            largest = number
    
    print(f"\nList of new numbers: {New_numbers}")
    print(f"Smallest number: {smallest}")
    print(f"Largest number: {largest}")
else:
    print("No numbers were entered to find smallest and largest.")
