numbers = []
num_elements = 10

print(f"Please enter {num_elements} integers:")


for i in range(num_elements):
    while True:
        try:
            num = int(input(f"Enter integer {i+1}: "))
            numbers.append(num)
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")



total_sum = 0
for number in numbers:
    total_sum += number


if num_elements > 0:
    average = total_sum / num_elements
else:
    average = 0 


print(f"\nList of numbers: {numbers}")
print(f"Sum of numbers: {total_sum}")
print(f"Average of numbers: {average}")
