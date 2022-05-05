# This returns two variables, and sets up something we can use later.
def swap_values(int_user_val1, int_user_val2):
    # This returning 2 variables that are supposed to be swapped.
    return int_user_val2, int_user_val1

# This defines main.
def __main__():
    # This is the two variables we use in our function swap_values. 
    int_user_val1 = int(input())
    int_user_val2 = int(input())
    # This specifically sets up what result 1 and 2 are, while calling swap_values. 
    # We have two result variables specifically because swap_values returns two variables, so it can store both
    # variables. 
    result, result2 = swap_values(int_user_val1, int_user_val2)
    # This outputs the swapped variables in their proper place. 
    print(result, result2)
    # Our return is blank because main is a void function. 
    return