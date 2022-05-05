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
# This is to find the max number of the equation.
int_max_num = max(list_converted_numbers)
# We need to have the sum to do the math later on.
int_sum_num = sum(list_converted_numbers)
# We use the equation to find the average here, len is the amount of numbers in the input.
# This is just so we can do the proper "all numbers added up together divided by the amount
# of numbers" formula.
int_average_num = int_sum_num / len(list_converted_numbers)
# Prints both results, we use int to get a whole number rather than a decimal.
print(int(int_average_num), int_max_num)