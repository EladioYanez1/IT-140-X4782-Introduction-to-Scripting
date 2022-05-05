# Defines the function.
def exact_change(user_total):
    # This divides the user total by 100.
    int_dollars = user_total // 100
    # This creates the new variable "int_dollar_remainder," this is used, so we can use when we're finding the quarters
    # we have to use, and the remaining quarters.
    int_dollar_remainder = user_total % 100
    # We take from the remaining dollars and use it for the quarters.
    int_quarters = int_dollar_remainder // 25
    # We take the remainder of the unused quarters, and do what we did with the dollars.
    int_quarter_remainder = int_dollar_remainder % 25
    int_dimes = int_quarter_remainder // 10
    # We take the remainder of the unused dimes, and do what we did with the dollars, and quarters.
    int_dime_remainder = int_quarter_remainder % 10
    int_nickels = int_dime_remainder // 5
    # We take the remainder of the unused dimes, and do what we did with the dollars, quarters, and
    # dimes.
    int_nickels_remainder = int_dime_remainder % 5
    # Since pennies is the bare basic of the currency, we don't need to make a remainder for pennies.
    int_pennies = int_nickels_remainder
    return int_dollars, int_quarters, int_dimes, int_nickels, int_pennies
# Main is a void function we are establishing in the first place.
def __main__():
    user_total = int(input())
    int_dollars, int_quarters, int_dimes, int_nickels, int_pennies = exact_change(user_total)
    # This is in case someone inputs 0, so there wouldn't be any calculations to run.
    if user_total == 0:
        print('no change')
    else:
    # These few lines are for if we have a single, or multiple dollars.
        if int_dollars > 1:
            # We use int_dollars as the number of dollars, and dollars for plural.
            print(int_dollars, 'dollars')
        elif int_dollars == 1:
            # This is for a single dollar.
            print('1 dollar')

    # These few lines are for if we have a single, or multiple quarters.
        if int_quarters > 1:
            # We use int_quarters as the number of quarters, and quarters for plural.
            print(int_quarters, 'quarters')
        elif int_quarters == 1:
            # This is for a single quarter.
            print('1 quarter')

    # These few lines are for if we have a single, or multiple dimes.
        if int_dimes > 1:
            # We use int_dimes as the number of dimes, and dimes for plural.
            print(int_dimes, 'dimes')
        elif int_dimes == 1:
            # This is for a single dime.
            print('1 dime')

        # These few lines are for if we have a single, or multiple nickels.
        if int_nickels > 1:
            # We use int_nickel as the number of dimes, and dimes for plural.
            print(int_nickels, 'nickels')
        elif int_nickels == 1:
            # This is for a single nickel.
            print(int_nickels, 'nickel')

        # These few lines are for if we have a single, or multiple pennies.
        if int_pennies > 1:
            # We use int_pennies as the number of dimes, and pennies for plural.
            print(int_pennies, 'pennies')
        elif int_pennies == 1:
            # This is for a single penny.
            print('1 penny')
    return

if __name__ == '__main__':
    __main__()