# Defines the input.
string_user_input = input()
# Creates the list, using split to make the list multiple pieces.
list_numbers = string_user_input.split()
# This creates the list we will be taking for the following function.
list_converted_numbers = []
# This is the function we need to make the numbers into integers rather than a string.
for i in list_numbers:
    # Since i is already defined in list numbers, we only have to do int(i).
    list_converted_numbers.append(int(i))
# This sorts the list by itself.
list_sorted_numbers = sorted(list_converted_numbers)
# This creates a list we put the non-negative numbers in after sorting the list.
non_negative_numbers = []
# This is so if a number is greater than negative 1, it is used. Otherwise, we ignore it. 
for i in list_sorted_numbers:
    if i > -1:
        # This adds the code into the list.
        non_negative_numbers.append(i)
# This is so we can print the list based on i. 
for i in non_negative_numbers:
    print(i, end=" ")

