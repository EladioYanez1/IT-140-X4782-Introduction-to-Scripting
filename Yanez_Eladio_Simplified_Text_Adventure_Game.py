# Eladio Yanez
# A dictionary for the simplified dragon text game
# The dictionary links a room to other rooms.
dict_rooms = {
    'Great Hall': {'South': 'Bedroom'},
    'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
    'Cellar': {'West': 'Bedroom'}
}

print('Welcome to the Great Dragon Room!')
# This is a neat artwork I thought would add some flare to my project.
# This is just art by the way, this isn't actually a set of bugs even though pycharm insists its so...
print("                \||/")
print("                |  @___oo")
print("      /\  /\   / (__,,,,|")
print("     ) /^\) ^\/ _)")
print("     )   /^\/   _)")
print("     )   _ /  / _)")
print(" /\  )/\/ ||  | )_)")
print("<  >      |(,,) )__)")
print(" | \____(      )___) )___")
print("  \______(_______;;; __;;;")
print("Credit: https://www.asciiart.eu/mythology/dragons")
print("Thou are forever stuck in this layer! All ye can do is explore this area!")
# This gives the instructions the player needs to explore around the area.
print("===== INSTRUCTIONS ======")
print('Acceptable Commands: North, East, South, West, Quit')
print(
    'Make sure you enter commands exactly as stated, uppercase first letter! It will not recognize lowercase "east" '
    'for example')
# This is the starting room, so we set it as 'var_current_room,' this executes ode later in the while statement.
var_current_room = 'Great Hall'
print("Are you ready to get your adventure started?")
print("Type Yes to Play")
# This is the input that initializes the entire code.
user_input = input()
print("You are starting in the Great Hall")
# This means if the user's input isn't quit, this then plays out the program until the user inputs quit.
while user_input != 'Quit':
    # This works because of the line earlier regarding setting var_current_room as 'Great Hall'.
    if var_current_room == 'Great Hall':
        print('You can go South.')
        user_input = input()
        # We use this if statement to have the code scan over the dictionary for the values in the current room.
        if user_input in dict_rooms[var_current_room]:
            # These two lines of code "moves" the player to the Bedroom.
            print("You are in the bedroom.")
            # This sets the new var_current_room as Bedroom, this makes it so the next statement works.
            var_current_room = 'Bedroom'
        else:
            # This statement is for the inputs that don't work for the code.
            print("Incorrect Input, try again. Use Proper Direction Naming Convention")
            # Continue is used to loop if statements.
            continue

    # This very much parallels the last block of code, but with the difference being the two values of the room.
    if var_current_room == 'Bedroom':
        print("You can go North, or East.")
        user_input = input()
        if user_input in dict_rooms[var_current_room]:
            # The if and the elif statements are used for the two directions the player can go into, they set the
            # variable "var_current_room" to different values, this first one makes it, so we arrive back into the first
            # room.
            if user_input == 'North':
                var_current_room = 'Great Hall'
                print('You are in the great hall. ')
            # This statement on the other hand directs the player to the cellar.
            elif user_input == 'East':
                var_current_room = 'Cellar'
                print('You are in the cellar.')
        else:
            print("Incorrect Input, try again. Use Proper Direction Naming Convention")
            continue

    # This block of code is just like the first block, but with the values unique to cellar alone.
    if var_current_room == 'Cellar':
        print("You can go West.")
        user_input = input()
        if user_input in dict_rooms[var_current_room]:
            var_current_room = 'Bedroom'
            print('You are in the bedroom.')
        else:
            print("Incorrect Input, try again. Use Proper Direction Naming Convention")
            continue
# This is when the user input becomes quit, the program stops and the current room becomes "Quit" as a result.
var_current_room = "Quit"
# This terminates the program.
if var_current_room == 'Quit':
    print('Thank you for playing my game, goodbye!')
