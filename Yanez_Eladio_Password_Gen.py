# This is all fairly self explainatory, just create different inputs. 
favorite_color = input('Enter favorite color:\n')
favorite_flower = input('Enter favorite flower:\n')
favorite_number = input('Enter favorite number:\n')
# Prints all 3 inputs together.
print('You entered:', favorite_color, favorite_flower, favorite_number)

# This is based on "yellow_Daisy," the color first, the underscore next, then the flower. 
password1 = favorite_color + "_" + favorite_flower
# This is based on 6yellow6, the number first, the color, then the number again. 
password2= favorite_number + favorite_color + favorite_number
# This prints out a blank space. 
print()
# It is important printing both versions of the password! 
print('First password:', password1)
print('Second password:', password2)

# Len is used to count the length of the passwords.
passsword1_characters = len(password1)
passsword2_characters = len(password2)
print()
print('Number of characters in', password1+":", passsword1_characters)
print('Number of characters in', password2+":", passsword2_characters)