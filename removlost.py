def remove_last(lst):
    """Removes the last element from a list and returns it."""
    if lst:
        return lst.pop()
    return None

# Create a sample list
my_list = [1, 2, 3, 4, 5]
print(f"Original list before function call: {my_list}")

# Call the function
removed_element = remove_last(my_list)

print(f"List after calling remove_last(): {my_list}")
print(f"Removed element: {removed_element}")

# Check if the original list changed outside the function
print(f"Did the original list change? {'Yes' if len(my_list) == 4 else 'No'}")
