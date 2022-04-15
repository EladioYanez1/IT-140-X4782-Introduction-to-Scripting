# Eladio Yanez

# This is the list of rooms and the values they have.

dict_rooms = {

    'Player Cell': {'Move North': 'Hallway', },
    'Hallway 1': {'Move South': 'Player Cell', 'Move West': 'Throne Room'},
    'Throne Room': {'Move North': 'Boss Room', 'Move West': 'Hallway 1', 'Move East': 'Hallway 2'},
    'Boss Room': {'Move South': 'Throne Room', 'Move West': 'Desolate Room', },
    'Desolate Room': {'Move North': 'Barracks', 'Move East': 'Boss Room'},
    'Barracks': {'Move South': 'Desolate Room', 'Move East': 'Armory', },
    'Armory': {'Move South': 'Hallway 2', 'Move West': 'Barracks'},
    'Hallway 2': {'Move North': 'Armory', 'Move West': 'Throne Room'}

}

# This is the dictionary of the items in the world, whenever the player takes an item it will be removed from the world
# inventory and be added to the player inventory. If the player wants the true ending, they need all 6 items, there is
# also the bad ending the player receives if they don't have the items. The keys are keys into other areas, so they are
# through the virtue of the player's tools, necessary to complete this game.
dict_world_inventory = {

    'Pendant': 1,
    'Key 1': 1,
    'Shield': 1,
    'Special Armor': 1,
    'Sword': 1,
    'Key 2': 1

}

list_player_inventory = []

# We will use this a few areas for specific requirements I'll go over soon.
times_vist_area = {

    'Player Cell': 0,
    'Hallway 1': 0,
    'Throne Room': 0,
    'Boss Room': 0,
    'Desolate Room': 0,
    'Barracks': 0,
    'Armory': 0,
    'Hallway 2': 0,

}

# This is a function we use throughout the project.
def helps():
    print('Look Around is an important command you should take advantage of as much as you can, it will')
    print('tell you where to go as well as point out items within the area.')
    print('Items you can grab will be denoted by capitalization, for example:')
    print('"There is a Knife in the box."')
    print('> Grab Knife')
    print('You grabbed the knife.')
    print('Commands: Move North, Move West, Move East, Move South, Look Around,')
    print('Grab [Insert Item Here], Fight, Check Inventory, Check Location, HELP, Quit.')

# This is the introductory text the player will first meet when they start up the program.
print("Welcome to Dark Mystery,")
print("You were out casted by your society and imprisoned in the dark")
print("dungeon with a vile and wretched demon. Your goal is to escape")
print("this dungeon and the clutches the demon. You will have to gather")
print("the supplies necessary to escape this area alive.")
print('-------------------------------------------------------------------------')
print('Commands: Move North, Move West, Move East, Move South, Look Around,')
print('Grab [Insert Item Here], Fight, Check Inventory, Check Location, HELP, Quit.')
print('Look Around is a highly important command, please use it.')
print('-------------------------------------------------------------------------')
print('Please write your commands with the proper capitalization of the inputs.')
# I have this as the statement because for some reason if the players input isn't start, the program turns itself
# off rather than staying on. I felt as if this was more convenient and this isn't really relevant beyond this bit.
print('Type Start when you are ready to start your adventure into the depths...')
print('Otherwise this program will terminate itself.')
print('-------------------------------------------------------------------------')
user_input = input()
# This makes it so the starting room is the Player Cell, which we want.
var_current_room = 'Player Cell'
# This means if the user input is start, then the rest of the code starts playing.
if user_input == 'Start':
    # This means if the user's input isn't quit, this then plays out the program until the user inputs quit.
    while user_input != 'Quit':
        if var_current_room == 'Player Cell':
            # This is the first time we call into the dictionary for the times visited, this is just so when the player
            # first starts up, they see this. After words, the player will not see this text since the value of player
            # cell in times_vist_area goes from 0 to 1.
            if times_vist_area['Player Cell'] == 0:
                print('-------------------------------------------------------------------------')
                print('You are within a dark and grim cell, the smell of blood and iron')
                print('fills your nose. This is certainly a place you don’t want to stay for')
                print('long... The only path available is northwards.')
                # This adds 1 to the times the player has visited the area.
                times_vist_area['Player Cell'] = times_vist_area['Player Cell'] + 1
            print('-------------------------------------------------------------------------')
            print('What do you do?')
            user_input = input()
            # "Move North/East/South/West" are the directional inputs, I felt as if they should have gotten represented
            # even if the player doesn't move in that direction. Thus, I made the code output "You ran into a wall."
            # I thought it would be a nice detail that shows that I tried to account for everything the player can do.
            if user_input == 'Move North':
                print('You walk out of your cell into a lifeless, messy, and dingy room.')
                print('It is rather damp. Maybe you should Look Around.')
                # This changes the value of the room the player is in to the first hallway, this means the player has
                # moved from 1 room to another.
                var_current_room = 'Hallway 1'
            elif user_input == 'Move East':
                print('You ran into a wall, be more careful next time.')
            elif user_input == 'Move South':
                print('You ran into a wall, be more careful next time.')
            elif user_input == 'Move West':
                print('You ran into a wall, be more careful next time.')
                # Look Around is the main gimmick of this code I think? It is the informational text that gives flavor
                # to this setting. Generally I tried writing this piece of code similar to that of classic Fallout.
                # Look Around does give the player important information, specifically where they can go and what items
                # would be around the room.
            elif user_input == 'Look Around':
                print('The hollowness of this cell can be felt from a glace. Staying here might')
                print('be a temporary comfort, but you must step out if you want to make anything')
                print('out of yourself.')
            # This prints the current inventory of the player, which is useful for players checking what items they
            # have. If the player missed an item, they can check and go back to where they once where.
            elif user_input == 'Check Inventory':
                print(list_player_inventory)
            # This is for the player to get a straight forward conformation for where they are at.
            elif user_input == 'Check Location':
                print(var_current_room)
            # At some point the player needs to fight a beast, so I have this there just so the player can type it in
            # and see that "yes, it can be used."
            elif user_input == 'Fight':
                print('There is nothing to fight here, you are wasting your time...')
            # For some reason if I did not have this line of code, the program would print ('Invalid Input') even though
            # I have the While Statement above. This was made to just avoid long term headaches for myself.
            elif user_input == 'Help':
                helps()
            elif user_input == 'Quit':
                print('-------------------------------------------------------------------------')
            # Whenever a user makes an input that doesn't fit amongst these lines, they get this phrase.
            else:
                print('Invalid Input.')
            # This makes the statement loop for an infinite amount of times, this is arguably the most important piece
            # of code for this project. It isn't hyperbolic for me to say if I didn't know the continue statement
            # existed, I don't think I could have done the project at my current skill level.
            continue
        # I won't be commenting on the pieces of code that reflects previous code I've written, I'll only comment on
        # the times applications of code pops up.
        if var_current_room == 'Hallway 1':
            print('-------------------------------------------------------------------------')
            print('What do you do?')
            user_input = input()
            if user_input == 'Move North':
                print('You ran into a wall, be more careful next time.')
            elif user_input == 'Move East':
                print('You enter upon an old throne room, lacking in the relics of the past...')
                print('You ponder your current location... You feel an ominous feeling in a')
                print('certain direction... Danger looms closely.')
                var_current_room = 'Throne Room'
            # These commands are for when the player moves back to old areas in the first place.
            elif user_input == 'Move South':
                print('You slithered back into your cage, either out of fear,')
                print('or out of ignorance...')
                var_current_room = 'Player Cell'
            elif user_input == 'Move West':
                print('You ran into a wall, be more careful next time.')
            elif user_input == 'Look Around':
                print('The stone hallway felt cold, and lifeless... You feel alone, for awhile you simply')
                print('gazed upon the room... Eventually you noticed a Pendant shinning dimly... You')
                print('noticed a minor entrance to a somewhat alluring room at the eastern front...')
            # This is the first time the player can actually grab an item, this is an important feature for the project.
            elif user_input == 'Grab Pendant':
                # This means if the current value of pendant in the world inventory equals to 1.
                if dict_world_inventory['Pendant'] == 1:
                    print('You grabbed the pendant out of curiosity, maybe it will serve some use.')
                    print('Or maybe you just wasted time...')
                    # This adds the Pendant item to the player inventory.
                    list_player_inventory.append('Pendant')
                    # This makes the value of the Pendant 0 in the world dictionary which is needed for the next
                    # statement.
                    dict_world_inventory['Pendant'] = dict_world_inventory['Pendant'] - 1
                # This prints when the Pendant Item has already been grabbed, meaning the player already has the
                # Pendant.
                else:
                    print('You have already grabbed that item, stop being nonsensical.')
            elif user_input == 'Fight':
                print('There is nothing to fight here, you are wasting your time...')
            elif user_input == 'Check Inventory':
                print(list_player_inventory)
            elif user_input == 'Check Location':
                print(var_current_room)
            elif user_input == 'Help':
                helps()
            elif user_input == 'Quit':
                print('-------------------------------------------------------------------------')
            else:
                print('Invalid Input.')
            continue

        if var_current_room == 'Throne Room':
            print('-------------------------------------------------------------------------')
            print('What do you do?')
            user_input = input()
            if user_input == 'Move North':
                # This line of code scans for the item 'Key 1' in the player inventory, this is to make sure the player
                # actually has the item to move forwards.
                if 'Key 1' in list_player_inventory:
                    print('With the key you grabbed, you walked straight into the room')
                    print('with the unbearable and ominous presence. You feel the fierce')
                    print('gaze of the beast pierce straight into your soul. Choose wisely,')
                    print('You are on a thin thread of life right now.')
                    var_current_room = 'Boss Room'
                # This plays when the player doesn't have the item.
                else:
                    print('You cannot walk into that room, you ought to look around for')
                    print('Something, although danger looks close.')
            elif user_input == 'Move East':
                # Key 2 is the item the player gets at the end of the game, and it is what allows them to move around
                # the area safely.
                if 'Key 2' in list_player_inventory:
                    print('You walk back within the second hallway to see')
                    print('if you missed anything of value. You feel as if')
                    print('the end is nigh.')
                    var_current_room = 'Hallway 2'
                else:
                    print('You ran into the locked door, think with your head.')
            elif user_input == 'Move South':
                print('You ran into a wall, be more careful next time.')
            elif user_input == 'Move West':
                print('You walk back into the hallway, little is known of why, but')
                print('you trudge onwards regardless.')
                var_current_room = 'Hallway 1'
            elif user_input == 'Look Around':
                if 'Key 1' in list_player_inventory:
                    print('You have a key, you can try opening the doors at the north, or east end')
                else:
                    print('Carefully you scan around the room... You notice on top of')
                    print('the throne a key, and two locked doors on the north side,')
                    print('and the east side.')
            elif user_input == 'Grab Key':
                if dict_world_inventory['Key 1'] == 1:
                    print('You grabbed the key sitting upon the top of the throne.')
                    list_player_inventory.append('Key 1')
                    dict_world_inventory['Key 1'] = dict_world_inventory['Key 1'] - 1
            elif user_input == 'Fight':
                print('There is nothing to fight here, you are wasting your time...')
            elif user_input == 'Check Inventory':
                print(list_player_inventory)
            elif user_input == 'Check Location':
                print(var_current_room)
            elif user_input == 'Help':
                helps()
            elif user_input == 'Quit':
                print('-------------------------------------------------------------------------')
            else:
                print('Invalid Input.')
            continue

        if var_current_room == 'Boss Room':
            print('-------------------------------------------------------------------------')
            print('What do you do?')
            user_input = input()
            # The main purpose behind these lines of code is to punish the player for not looking around and seeing
            # that the west end is the only safe end. I'd rather have the fail condition in this circumstance to not
            # be immediate death. Partially because the player has to go here to get the rest of the items. This is
            # a very small check in the grand scheme of things, and I wanted the 'Look Around' command to play
            # an important part in the players' success here.
            if user_input == 'Move North':
                print('You idiotically run into the beast, within seconds you')
                print('were torn apart. Your fragile life met its tragic end')
                print('Due to sheer ignorance. In the end, ignorance is the')
                print('most silent and lethal of killers...')
                print('-------------------------------------------------------------------------')
                print('GAME OVER')
                quit()
            elif user_input == 'Move East':
                print('You recklessly ran into a wall, the demon lunged right on')
                print('top of you. Your life within a flash was taken away.')
                print('Only your bones were left. At least your suffering was brief...')
                print('-------------------------------------------------------------------------')
                print('GAME OVER')
                quit()
            elif user_input == 'Move South':
                print('You turned around to run back into the throne room, unfortunately')
                print('you fell over leaving yourself exposed to the beast')
            elif user_input == 'Move West':
                # This is the other major instance where the times_vist_area is an important factor, this makes it so
                # the player gets two versions of the text whether they've already escaped from the West Side or not.
                # In the first attempt, the can move to the west side because the door hasn't slammed down yet.
                if times_vist_area['Boss Room'] == 0:
                    print('You decidedly and quickly ran to your left side without hesitation, as you ran')
                    print('you heard a door slam on the ground behind you. You turn around to see a trap')
                    print('door stuck in place... It seems as if it protected you from certain death...')
                    var_current_room = 'Desolate Room'
                    # This makes it so the room has been visited more than once, adding onto the variable and leading
                    # into the else statement the next time the player arrives.
                    times_vist_area['Boss Room'] = times_vist_area['Boss Room'] + 1
                # This is the game over condition for the player here if they've already visited this area, due to the
                # common sense reason of "this area is gated off."
                else:
                    print('The pathway to the desolate room was locked, in your moment of ignorance')
                    print('your death had come at a swift, yet merciless end. It all ended in this moment.')
                    print('May you find some comfort in the afterlife, as your comfort in this world was thin...')
                    print('-------------------------------------------------------------------------')
                    print('GAME OVER')
                    quit()
            elif user_input == 'Look Around':
                # This gives the player different analysis depending on whether they've escaped here before or not.
                if times_vist_area['Boss Room'] == 0:
                    print('You see an immense beast right in front of you, you feel a tangible sense of')
                    print('of fear and dread consume you. Your eyes rapidly looks around the room as you')
                    print('notice an escape on your west side. It is your only possible chance for safety.')
                    print('Act quickly.')
                else:
                    print('The door from last time is clamped down, it would be suicidal try')
                    print('to escape westwards again. You must face the beast or die trying.')
            elif user_input == 'Fight':
                # This scans for every item in the players inventory.
                # This is the true ending, I wanted to make the Pendant an optional item rather than a required item
                # because I felt as if having it being an optional item would have encouraged the player to look
                # around more if they were to replay this. This does not exactly have the most replay-ability, but
                # I think this tiny detail is neat.
                if 'Sword' and 'Shield' and 'Special Armor' and 'Pendant' in list_player_inventory:
                    print('The battle you had with the beast in the end was a long and arduous fight, you felt the')
                    print('lethality of its claws trying to claw into you... But you were than prepared for the')
                    print('wrath of the beast. Each slash was careful and thought out, yet afterwards you stood')
                    print('victorious after the beast... You felt a looming darkness consume the room, you were')
                    print('faced with a confusing and threatening end trudging closer to you... Yet the pendant')
                    print('That you had gotten earlier shined at its brightest. The darkness was repelled as you')
                    print('saw a glimmer of light appear before where the beast once was... It was nearly blinding')
                    print('blinding for your eyes, yet at the same time it gave you the strongest form of relief')
                    print('that you had felt yet... You looked deeper into the light and you had seen your escape')
                    print('escape out of this horrendous land. It seems as if your perseverance, and intelligence')
                    print('had saved you from a tragic fate... Now leave, and never look back. Whatever is ahead')
                    print('must be far better than the horrors you had experienced.')
                    print('Congratulations, you have managed to get the true ending!')
                    print('Thank you for playing, goodbye!')
                    print('-------------------------------------------------------------------------')
                    quit()
                    # This is the ending the player gets if they have everything but the pendant, it is bitter compared
                    # to the true ending just to encourage a replay.
                elif 'Sword' and 'Shield' and 'Special Armor' in list_player_inventory:
                    print('The battle you had with the beast in the end was a long and arduous fight, you felt the')
                    print('lethality of its claws trying to claw into you... But you were than prepared for the')
                    print('wrath of the beast. Each slash was careful and thought out, yet afterwards you stood')
                    print('victorious after the beast... Yet you felt as if something was wrong. The all too')
                    print('consuming darkness loomed over you with a cruel tinge of resentment. You noticed a door')
                    print('behind where the beast once was, but it was locked... The intensity of the dark would')
                    print('soon consume you without a second thought. No longer did you hold a human form, you')
                    print('yourself had become the beast that you had defeated before... The cycle of pain and')
                    print('suffering had only just repeated, rather than truly being broken...')
                    print('You have managed to get the bad ending, play again for a potentially better ending!')
                    print('Tip, be more careful about your environment.')
                    print('Thank you for playing, goodbye.')
                    print('-------------------------------------------------------------------------')
                    quit()
                    # This is the failure condition if the player tries to fight the beast without any equipment at all.
                else:
                    print('In your vain attempt to start a fight, you met')
                    print('an immediate and swift death. Your final breath')
                    print('was full of pain and agony. You will be forgotten.')
                    print('GAME OVER')
                    print('-------------------------------------------------------------------------')
                    quit()
            elif user_input == 'Check Inventory':
                print(list_player_inventory)
            elif user_input == 'Check Location':
                print(var_current_room)
            elif user_input == 'Help':
                helps()
            elif user_input == 'Quit':
                print('-------------------------------------------------------------------------')
            else:
                print('Invalid Input.')
            continue

        if var_current_room == 'Desolate Room':
            print('-------------------------------------------------------------------------')
            print('What do you do?')
            user_input = input()
            if user_input == 'Move North':
                print('Barely managing to walk past the clutter,')
                print('you stumble across what seems to be the former barracks')
                print('of the former kingdom... Nothing but silence pierces the room now.')
                var_current_room = 'Barracks'
            elif user_input == 'Move East':
                print('You gaze at the door, you gave a brief sigh of relief... Life is too')
                print('Valuable to throw it away in such a hasty situation.')
            elif user_input == 'Move South':
                print('You ran into a wall, be more careful next time.')
            elif user_input == 'Move West':
                print('You ran into a wall, be more careful next time.')
            elif user_input == 'Look Around':
                print('A messy and cluttered room, after a bit of examination your eyes')
                print('manage to spot a Shield, perhaps it might serve a use to you...')
                print('You see northwards a door past all the clutter.')
            elif user_input == 'Grab Shield':
                if dict_world_inventory['Shield'] == 1:
                    print('You grabbed onto the shield. Perhaps it will safe your life.')
                    list_player_inventory.append('Shield')
                else:
                    print('You already have the shield.')
            elif user_input == 'Fight':
                print('There is nothing to fight here, you are wasting your time...')
            elif user_input == 'Check Inventory':
                print(list_player_inventory)
            elif user_input == 'Check Location':
                print(var_current_room)
            elif user_input == 'Help':
                helps()
            elif user_input == 'Quit':
                print('-------------------------------------------------------------------------')
            else:
                print('Invalid Input.')
            continue

        if var_current_room == 'Barracks':
            print('-------------------------------------------------------------------------')
            print('What do you do?')
            user_input = input()
            if user_input == 'Move North':
                print('You ran into a wall, be more careful next time.')
            elif user_input == 'Move East':
                print('You move past the area of the cold silence of barracks as you stumble upon')
                print('a room full of weaponry... The blades look as sharp as they should be.')
                var_current_room = 'Armory'
            elif user_input == 'Move South':
                print('You stumble back into the messy room...')
                var_current_room = 'Desolate Room'
            elif user_input == 'Move West':
                print('You ran into a wall, be more careful next time.')
            elif user_input == 'Look Around':
                print('Silence fills the room, you can faintly feel the life that once was apart of this area.')
                print('Time has taken its toll on this, the walls are withered... The tables are far from clean,')
                print('and the area feels barron... After upon inspection, you noticed Armor over in the corner.')
                print('Perhaps you should wear it. Your gaze also notices on the eastern side to be another entrance.')
                print('You faintly see what would be an armory. ')
            elif user_input == 'Grab Armor':
                if dict_world_inventory['Special Armor'] == 1:
                    print('Without hesitation you decided to done the armor, maybe this will protect you...')
                    list_player_inventory.append('Special Armor')
                    dict_world_inventory['Special Armor'] = dict_world_inventory['Special Armor'] - 1
                else:
                    print('You are already wearing the armor, there is not any purpose to this.')
                    list_player_inventory.append('Special Armor')
            elif user_input == 'Fight':
                print('There is nothing to fight here, you are wasting your time...')
            elif user_input == 'Check Inventory':
                print(list_player_inventory)
            elif user_input == 'Check Location':
                print(var_current_room)
            elif user_input == 'Help':
                helps()
            elif user_input == 'Quit':
                print('-------------------------------------------------------------------------')
            else:
                print('Invalid Input.')
            continue

        if var_current_room == 'Armory':
            print('-------------------------------------------------------------------------')
            print('What do you do?')
            user_input = input()
            if user_input == 'Move North':
                print('You ran into a wall, be more careful next time.')
            elif user_input == 'Move East':
                print('You ran into a wall, be more careful next time.')
            elif user_input == 'Move South':
                print('You decide you have spent enough time in the armory, you step on out')
                print('to see a new hallway... It is less dim and depressing than before, perhaps')
                print('there is hope ahead... Or this is simply ignorance posing as relief.')
                var_current_room = 'Hallway 2'
            elif user_input == 'Move West':
                print('You decide to walk back in the hollow barracks, perhaps you feel as if')
                print('you felt like you missed something valuable... Whatever may it be, the')
                print('choice is yours...')
                var_current_room = 'Barracks'
            elif user_input == 'Look Around':
                print('There was a cold and... "mechanical" feeling to this location, it felt lifeless but... Your')
                print('eyes gleam across a particular Sword, honestly given your current circumstances it would be a')
                print('wise choice to grab it. You see a hallway down at the southern end of the area, it looks...')
                print('Vaguely familiar.')
            elif user_input == 'Grab Sword':
                if dict_world_inventory['Key 2'] == 1:
                    print('You hastily grabbed the blade, maybe this will save you...')
                    list_player_inventory.append('Sword')
                    dict_world_inventory['Sword'] = dict_world_inventory['Sword'] - 1
                else:
                    print('You already have the blade, stop wasting your time.')
            elif user_input == 'Fight':
                print('There is nothing to fight here, you are wasting your time...')
            elif user_input == 'Check Inventory':
                print(list_player_inventory)
            elif user_input == 'Check Location':
                print(var_current_room)
            elif user_input == 'Help':
                helps()
            elif user_input == 'Quit':
                print('-------------------------------------------------------------------------')
            else:
                print('Invalid Input.')
            continue

        if var_current_room == 'Hallway 2':
            print('-------------------------------------------------------------------------')
            print('What do you do?')
            user_input = input()
            if user_input == 'Move North':
                print('You walked back into the armory, perhaps you left something behind.')
                var_current_room = 'Armory'
            elif user_input == 'Move East':
                print('You ran into a wall, be more careful next time.')
            elif user_input == 'Move South':
                print('You ran into a wall, be more careful next time.')
            elif user_input == 'Move West':
                if 'Key 2' in list_player_inventory:
                    print('With the key you managed to open the door up to the throne room... Yet again to the')
                    print('north is the beast near you... Consider preparing for the worst.')
                    var_current_room = 'Throne Room'
                else:
                    print('The door is locked, perhaps you should try finding a way to open the door.')
            elif user_input == 'Look Around':
                print('Upon looking around for a bit... You realize this room is connected to the Throne room on the')
                print('western end! Upon further inspection you notice another Key, you should grab it. It is your way')
                print('out of this room.')
            elif user_input == 'Grab Key':
                if dict_world_inventory['Key 2'] == 1:
                    print('You hastily grabbed the key, perhaps it is your way out of this room...')
                    list_player_inventory.append('Key 2')
                    dict_world_inventory['Key 2'] = dict_world_inventory['Key 2'] - 1
                else:
                    print('You already have grabbed key, stop wasting your time.')
            elif user_input == 'Fight':
                print('There is nothing to fight here, you are wasting your time...')
            elif user_input == 'Check Inventory':
                print(list_player_inventory)
            elif user_input == 'Check Location':
                print(var_current_room)
            elif user_input == 'Help':
                help()
            elif user_input == 'Quit':
                print('-------------------------------------------------------------------------')
            else:
                print('Invalid Input.')
            continue
    # This closes the program once the player inputs "Quit".
    var_current_room = 'Quit Room'
    if var_current_room == 'Quit Room':
        print('Thank you for playing this game, have a nice day!')
        quit()
# This makes it so the termination of the program makes sense.
else:
    print('Invalid Input, shutting down program.')
