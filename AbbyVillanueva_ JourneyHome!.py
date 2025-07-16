#first name: Abby
#last name: Villanueva
#date submitted: 1/14/2024

#note: the game (especially the printed statements) is best enjoyed with 
# full-screen or with zen-mode (CTRL + K Z).

###

#INITIALISE IMPORTS, GLOBAL LISTS, ETC.
import sys              #to support time (access the sys)
import time             #to access different features from time
from time import sleep  #get sleep to adjust timing of print statements
import math             #get math to access ceil to round up values 
import random           #to generate random numbers

#INITIALISE GLOBAL LISTS & DICTIONARIES
Str_inputs = [ #the list of Acceptable string inputs 
    'profile',
    'Profile',
    'PROFILE', 
    'side quests', 
    'Side quests', 
    'Side Quests',
    'SIDE QUESTS',
    'Ethos',
    'Pathos',
    'Logos',
    ]  
Players_attributes = { #the players attributes, they start at 20 
        'Ethos': 20,
        'Pathos': 20,
        'Logos': 20
    } 

#INITIATE GLOBAL VARIABLES
# FORMATTING AND COLOUR: concept from (https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal/39452138#39452138)  
    #formatting
CEND      = '\33[0m'        #to reset it, or END the fancy embelishments
CBOLD     = '\33[1m'
CITALIC   = '\33[3m'
CURL      = '\33[4m'
CURLUP    = '\33[53m'
CDOUBLEURL = '\33[21m'      #TO REFER TO THE PLAYER (APPLIED TO THEIR NAME)
CCROSSOUT = '\33[09m'       #death screen
CSELECTED = '\33[7m'        #Titles of sections/main functions 
                            # makes the text colour the bg colour (when you select)
    #text colours
CWHITE  = '\33[37m'         #player SPEECH colour
CWHITE2  = '\33[97m'        #"what do you do?"
CBLACK  = '\33[30m'         #me talking to the player (dev notes)
CRED    = '\33[31m'         #Pathos Colour
CGREEN  = '\33[32m'         #LOKI Dialouge
CYELLOW = '\33[33m'         #Ethos colour
CBLUE   = '\33[34m'         #Logos Colour
CVIOLET = '\33[35m'         #SIDE QUESTS 
CBEIGE  = '\33[36m'         #hero twins arc highlight
CGREY    = '\33[90m'        #hero twins arc highlight
CBEIGE2  = '\33[96m'        #twins dialouge + Ixbalanke colour
CRED2    = '\33[91m'        #anansi dialouge
CGREEN2  = '\33[92m'        #anansi arc highlight
CYELLOW2 = '\33[93m'        #wukong dialouge
CBLUE2   = '\33[94m'        #Junajpu colour
CVIOLET2 = '\33[95m'        #Hestia colour (speech)
    #background colours    
CBLUEBG   = '\33[44m'       #LOGOS bg colour 
CGREENBG    = '\33[42m'     #Loki's colour    
CVIOLETBG   = '\33[45m'     #Bajie's colour
CGREYBG     = '\33[100m'    #side quests highlights 
CREDBG2     = '\33[101m'    #Anansi's colour (titlecard)
CYELLOWBG2  = '\33[103m'    #Sun Wukong's colour (titlecard)
CVIOLETBG2  = '\33[105m'    #Hestia's colour, (titlecard/name)
CCYANBG     = '\33[106m'    #HERO Twins colour (titlecard)  
CBEIGEBG    = '\33[46m'     #HERO Twins colour (titlecard)
CWHITEBG    = '\33[47m'   
Users_inventory_string = '' #the string of items in the user's inventory that is printed every 
                            #time player_profile() is called
Id_enchanteditem = ''       #allows the enchanted_item_activated() to tell what enchanted item's 
                            # characteristics shoud be applied                            
Enchanted_item_attribute = ''   #is the attribute associated with the enchanted item.
                                #is used in the ask_activate_enchanteditem() function
Enchanteditem_use_counter = 0   #keeps track of how many times the player used their enchanted item      
Sidequest_use_counter = 0       #keeps track of how many times the player went on a side quest
True_ending_confirmation = 0    #will switch to one if player meets the requirements to get the 
                                #true ending: they used their enchanted item during the last round

###

# INPUT
Player_name = input(f'{CBOLD}Enter your name:{CEND} ')  #let the player name themselves anything 

###

#PROCESS
def the_menu():                                                 #the first thing the player sees  
    """
    Allows the player to choose if they want to play, access the game instructions, 
    your profile, side quests, or exit by typing in a number in their terminal.

    Args:
        none
    Returns:
        menu_choice (str): the varibale that has the user's input 
    """
    #initialise lists
    menu_gamestart_intro_list = [   #the intro of the game
        f'With a reputation built on years of experience, you have never once lost an argument nor a fight.',
        f'As you travel to your hometown, your unfortunate unluckiness strikes as you'
        f' encounter gods from different pantheons.',
        f'In this win or die situation you have to use all your '
        f'{CBLUE}wit{CEND}, {CRED}strength{CEND}, and powers of {CYELLOW}persuasion{CEND}', 
        f'to convince the gods to let you go home and eat your mother’s home cooked meal.\n',
        f'{CVIOLET2}❁{CEND}  ━{CSELECTED} Game Start {CEND}━ {CVIOLET2}❁{CEND}'
        ]

    #initiate varibales
    sleep_time = 0      #the amount of time that is delayed during prints

    #no input

    #process
    print(' ')  #adds space
    while True:     #loop the menu so that the user can keep chosing where to go
        print(f'1: Start Game \n2: Game Instructions \n3: Quit Game \n')

        #input
        menu_choice = input_system_ingame(3, 1)      #use the input_checking function with the assigned
                                                #parameters to check the user's input

        #process
        if menu_choice == '1':      #player chooses to start game 
            #add the intro text
            for i in range(len(menu_gamestart_intro_list)): 
                temp = 26       #constant that adjusts indenetation
                temp_2 = 0      #variable that adjusts indenetation

                #adjust the indentation
                if i == 0:
                    print(' ')  #adds space
                    temp_2 = -5
                    sleep_time = 0.5
                elif i == 1:
                    temp_2 = -14
                elif i == 2:
                    temp_2 = -3
                elif i == 3:
                    temp_2 = 4
                elif i == 4:
                    temp_2 = 26
                    sleep_time = 1

                x = (temp + (temp_2))   #the equation that helps adjust indentation
                
                print(' '*x + f'{menu_gamestart_intro_list[i]}')    #print the str
                sleep(sleep_time)               #use timer + delay to add suspense
            
            #start the game IN OTHER WORDS break out of the menu loop
            break       
        elif menu_choice == '2':    #player sees game instructions
            game_instructions() #present the game instructions
        elif menu_choice == '3':    #player quits game 
            #add emeblishments
            sys.exit()      #shuts down the program 
                            #source: (https://www.geeksforgeeks.org/python-exit-commands-quit-exit-sys-exit-and-os-_exit/#:~:text=exit()%20)%3A%20Exits%20Python%20by,the%20program%20without%20any%20cleanup.) 

    #no output
    return menu_choice

def linear_search_through_list(my_list, item):                  #used in str checking (linear search) 
    """
    Searches through a list until the specified item is found, if it is not it says so
    Args:
        my_list (list): the list that will be sifted through
        item (str): the specific item that needs to be found
    Returns
        status_of_word (str): indicates whether the item is found or not
    """
    #initiate variables
    position = 0                    #changes the index each time
    status_of_word = 'not found'    #the varibale to be returned, is set to not found but if 
                                    #found, will change to 'found' (input_str_checking function)
    found = False                   #the sentinel

    #process + input
    while position < len(my_list) and not found:    #if the index is within the and is not found yet
        if my_list[position] == item:
            found = True                #stops the loop
            status_of_word = 'found'    #changes the status of the word if found
        else:
            position = position + 1     #changes the position
    
    #output
    return status_of_word       #return if the word is found or not

def input_str_checking(accepted_str_inputs, user_str_input):    #checks str inputs from player 
    """
    Checks the user's STRING inputs to see if it is valid. 
    Args:
        accepted_str_inputs (list): the list that has the words the user CAN enter
        user_str_input (str): the string that the user entered
    Returns:
        user_str_input (str): the string that the user entered
    """
    #no inputs
    #process
    while True:
        # saves the status of their input in a varible to be checked later
        status = linear_search_through_list(accepted_str_inputs, user_str_input)     
        if status == 'found':   
            break                               #if the word is in the list, break the loop
        else:
            break
        
    #ouput
    return status   #returns the string that the user entered. 

def input_checking(highest, lowest):                            #checks all inputs from player 
    """
    Checks the user's INTEGER and STRING input to see if it is valid.

    Args:
        highest (int): the upper limit to what number the user can type in.
        lowest (int): the lower limit to what number the user can type in.
    Returns:
        user_input (str): the number that the user inputted
    """
    #no input
          
    #process
    while True:
        try:
            user_input = input(CBOLD + 'Enter your choice: ' + CEND) # the variable that contains 
                                                                    # the user's input specifcy that the 
                                                                    # user_int_input is in fact a number 
                                                                    # Use formatting from stack <3
            if input_str_checking(Str_inputs, user_input) != 'found':           # if the input is not part of the 
                                                                    # accepted strings then either: they got it 
                                                                    # wrong (str) or they typed in a number
                if int(user_input) <= highest and int(user_input) >= lowest:
                    break
            else:
                break 
        except:
            print('Invalid input. Try again.')
    # my debugging journey  — The problem is that the function kept asking the user to input again 
    # even when they typed in the right thing after a series of wrong inputs:
        #letter-number-proper(word+num) = okay
        #number-letter-proper(word+num) = not okay -> asks the user 1 extra time
        #num-num = okay
        #word-word = okay
    
    #ouput/return
    return user_input.lower()   #makes all the letters lowercase ()

def input_system_ingame(greaternum, leastnum):                  #is the main input checker when-ingame 
    """
    Allows the user to make decisions in-game and access to other aspects of the game.
    Args:
        greaternum (int): the upper limit to the choices a user can pick
        leastnum (int): the lower limit to the choices a user can pick
    Returns:
        ingame_choice (str): the variable that has what the user inputted.
    """
    #display
    print(f'{CBLACK}To access the following, type: "profile" or "side quests"{CEND}')

    #call global variable
    global Sidequest_use_counter

    # input
    ingame_choice = input_checking(greaternum, leastnum)    #checks if their input is valid or not
    
    #process  
    if ingame_choice == 'profile':          #if they typed 'profile', it leads them there 
        player_profile()
    elif ingame_choice == 'side quests':    #if they typed side quests, it leads them there
        if Sidequest_use_counter < 3:
            Sidequest_use_counter += 1      #keeps track of how man times the user used sidequests
            side_quest()                    #leads player to the side quest section
        else:
            print('\n', end = '') #add space
            print(' ' * 26 + f'{CDOUBLEURL}{CURLUP}You have exceeded side quest privileges.{CEND}\n')

    #output
    return ingame_choice

def game_instructions():                                        #houses the game instructions 
    """
    Displays the game's instructions to the player.
    Args:
        none
    Return:
        none    
    """
    #initialise lists
    instructions_intro = [      #This list is the 1st one! -> INtroduces the game and its main concept 
        f'Using your powers of persuasion you fight against gods to get home.', 
        f'You, {CDOUBLEURL}{Player_name}{CEND}, have 3 attributes that you use to persuade the gods:', 
        f'{CYELLOW}Ethos{CEND}, {CRED}Pathos{CEND}, and {CBLUE}Logos{CEND}',    #have the text in 1 line w/ f''
        f'You start off with {CBOLD}20 points each{CEND} but throughout the game you will accumulate and lose points.\n'
    ]   
    instructions_body = {       #this is a dictionary. It shows the body of the text W/ FORMATTING 
        # idea is from a book: Eric Matthes PYTHON CRASH COURSE (dictionaries)
        f'{CBOLD}{CSELECTED}Win or Lose mechanics:{CEND}': [
            f'To win the game you must reach the end without having 2 or more' 
            f' attributes worth less than 0.', 'If at any point ' 
            f'{CURL}two (2) of your attributes are negative{CEND} you will automatically lose.' #sep. line!
            ],
        f'{CBOLD}{CSELECTED}Gameplay mechanics:{CEND}': [
            f'You have the chance to {CURL}view your stats and inventory real-time{CEND} as you play. '
            f'Simply typing ', '"profile" will give you access to the contents of your '
            f'inventory and the amount of points ','you have. While typing "side quests" '
            f'will allows you to gain points by playing a ', 'smaller-scale game.'
            ],
        f'{CBOLD}{CSELECTED}Side-quests:{CEND}': [
            f'You have the chance to gain more points by participating in sidequests. ' 
            f'You will gain ', 'different magnitudes of boosted points depending on what random'
            f' side quest you are given.', 
            f'Note: {CURL}You are limited to only 3 side quests.{CEND} '    #have the special fonts be on a sep. line!
            ],
        f'{CBOLD}{CSELECTED}Enchanted Items:{CEND}': [
            f'These gifts from the sweet librarian will help you throughout your journey.',
            f'Each is different in which attribute it aids. ', 
            f'Access your {CURL}inventory{CEND} to discover'
            f' more!'
            ],
        f'{CBOLD}{CSELECTED}Endings:{CEND}': [
            f'You are able to achieve a variety of different endings based on the outcome of', 
            f'your journey and the choices you make.'
            ]
    }

    #no input
    
    #process & output
    print(' ')      #adds space

    for j in range(len(instructions_intro)):    # displays the intro w/ timer
                                                # use the range function to access the indexes
        temp = 26     #use temporary variables!
        temp_2 = 0

        if j == 1:
            temp_2 = 2              #indent the text a bit more
        elif j == 2:
            temp_2 = 20             #indent the text much more
        elif j == 3:
            temp_2 = 0              #reset the indent
            temp = 15               #have the text start w/ less indent

        #equation that adjusts how many spaces there will be
        x = (temp + (temp_2))    
        
            #prints the text
        print(' ' * x, end = '')      #prints space to 'center' the lines of text
        print(instructions_intro[j])        #j is the number in the range
        sleep(0.5)
    
    for name, descriptions in instructions_body.items():     #display the body w/ format 
        print(' ' * 5 + name)     #name = key, goes thorugh the dictionary one by one
        for description in descriptions:    #description = values in list, goes thorugh each value in list
            print(' ' * 10 + description)     #adds indent and description
        print(' ')
        sleep(0.5)  #delays printing of each body of text

    ending_embelishment('reg')  #add emeblishment

def the_inventory(index_address):                               #adds items to the user's inventory 
    """
    Adds items from the Master_inventory to the User's inventory and returns the items in a str.
    args:
        index_address (int): the index number of the item in Master_inventory
    returns:
        user_inventory_list (list): the list that has all of the user's inventory
    """
    # initialise lists
    master_inventory_list = [
    #enchanted items (index: 0-2)
    f'{CYELLOW}Embroidered Vest{CEND}\n\t Reduces cost of {CYELLOW2}Ethos{CEND} points by 50%. '
                f'{CBOLD}Valid for only 3 Rounds.{CEND}',
    f'{CRED}6 Rings{CEND}\n\t{CBOLD}Adds 10 {CRED}Pathos{CEND} points{CEND} for each activation. '
                f'{CBOLD}Valid for only 3 Rounds.{CEND}',
    f'{CBLUE}Vintage Pocket Watch{CEND}\n\tNullifies cost of {CBLUE}Logos{CEND} points. ' 
                f'{CBOLD}Valid for only 3 Rounds.{CEND}',
    #arc rewards (index: 3-5)
    f'Mini Magic Staff\n\tA gift from {CYELLOWBG2}Sun Wukong{CEND}. A miniature of Ruyi Jingu Bang. ' 
                f'It can help the user cast illusions.',
    f'Spindle of Webs\n\tA gift from {CREDBG2}Anansi{CEND}. A spindle of webs not even the strongest '
                f'of gods could escape without a fight.',
    f'Mosquito Jar\n\tA gift from the Hero Twins {CBLUE2}Junajpu{CEND} and {CBEIGE2}Ixb’alanke{CEND}. ' 
                f'It houses 1 mosquito that can multiply and absorb the life force of its victims.'
    ]
    user_inventory_list = []                    #the list that holds the player's inventory
    
    #no input
    
    #process
    if type(index_address) == int:
        #checks if the index_address is correct
        if index_address > -1 and index_address < 6:    #limits it to the indexes within the list (5)
            item_in_inventory = master_inventory_list[index_address]   #gets the specfici item description and saves it in a 
                                                                    #variable 'item_in_inventory' to be used later on  

            user_inventory_list.append(item_in_inventory)   #adds the item the player earned to their personal inventory list

            for i in user_inventory_list:           #loops through each value in the user's inventory list
                global Users_inventory_string       #accesses and allows me to modify the global variable
                                                    #^idea from: (https://realpython.com/python-use-global-variable-in-function/#using-global-variables-in-python-functions)
                Users_inventory_string += f'{i}\n'  #adds the item description to the string that will be returned
                sleep(0.5)

            #output/return
            return user_inventory_list           #returns the user's inventory in a string format
        else:   #if it is not within the list it sends an 'error'
        #output/return
            return 'indexerror_payattention_abby' 
    else:
        #output/return
        return 'shouldbeanint_abby'


    #no output/return

def player_profile():                                           #optimisation is possible 
    """
    Displays the name, inventory, and points of the player. 
    Args:
        none
    Return:
        none
    """
    # no input
    # process & output
    for i in range(2):
        print(' ')  #adds space

    for i in range(0, 4, 1):
        if i == 0:  #prints the word 'PROFILE' 
            title_profile = CBOLD + CSELECTED + 'PROFILE' + CEND + '\n' #title of page
            print(f' ' * 46, end = '')     #put empty space on the same line
            for l in title_profile:     #code that mimics a type-writer: from stackoverflow!
                sys.stdout.write(l)
                sys.stdout.flush()
                time.sleep(0.1)

        elif i == 1:
            print(f'{CBOLD}{CURL}Alias{CEND}: {Player_name}' + '\n')    #name/title of player
            sleep(0.5)

        elif i == 2:
            print(CBOLD + CURL + 'Stats' + CEND + ':')  #heading of section --> STATS
            print(CYELLOW + f'Ethos:' + CEND, Players_attributes['Ethos'], end = '')  #ethos points
            print(' ' * 16, end = '')                                     #adds space on the same line
            print(CRED + f'Pathos:' + CEND, Players_attributes['Pathos'], end = '')    #pathos points
            print(' ' * 16, end = '')                                     #adds space on the same line
            print(CBLUE + f'Logos:' + CEND, Players_attributes['Logos'], '\n')  # logos points
                                                                                # no end because we want a space
            sleep(0.5)      #delays prints

        elif i == 3:
            print(CBOLD + CURL + 'Inventory' + CEND + ':')  #heading of section --> Inventory
            print(Users_inventory_string)       #prints the final (updated) contents of
                                                #the user's inventory
            print('\n')

    ending_embelishment('reg')      #add embelishments

def points_tally(attribute_affected, dec_num):                  #keeps track of points 
    """
    Updates the points of the player throughout the game. Monitors the points of the player and 
    initiates a game over if the player has negative points in two attributes.
    Args:
        attribute_affected (str): the attribute that is being affected
        dec_num (int): the subtrahend, the number that the attribute will be subtracted by
    Returns:
        players_attributes[attribute_affected]: the value of the attribute affected.
    """
    #initialise globals (variables/lists/dictionaries)
    global Players_attributes

    #initiate (local)varibles
    negataive_counter = 0       #keeps track of how many attributes are below 0
    negative_attributes = ''    #records which attributes are below 0

    #no input
    
    #process 
    #checking the validity of the attribute_affected 
    if input_str_checking(Str_inputs, attribute_affected) == 'found':
        #checks if the dec_num is an int
        if type(dec_num) == int:
            # defining a new value for an attribute
            new_attribute_value = Players_attributes[attribute_affected] - dec_num  #calculates the new value 
                                                                                    # for the attribute
            Players_attributes[attribute_affected] = new_attribute_value            #changes the attribute's value
                
            #if the player has two attributes below zero, they will get game over'd
            for i in Players_attributes:                #loops through each key in the dictionary
                if Players_attributes[i] < 0:           #if the value of the key is less than zero; 
                    negataive_counter += 1              #it adds 1 to the negative counter
                    negative_attributes += (f'{i}, ')   #the key is also added to the str of negative attributes
                if negataive_counter > 1:   #if the negative counter is equal to 2 or;
                                            #two attributes are negative
                                            #it had to be another if statement becaus if it was an elif, 
                                            #only the first if statement would pass i.e. no game over's 
                                            #when there should have been game over's
                    #prints the message
                    title_profile = CITALIC + CBLACK + '2 out of your 3 attributes are below zero.' + CEND
                    print('\n' + f' ' * 46, end = '')     #put empty space on the same line
                    for l in title_profile:     #code that mimics a type-writer: from stackoverflow! 
                        sys.stdout.write(l)
                        sys.stdout.flush()
                        time.sleep(0.1)
                    sleep(1)            #add delay for suspense
                
                    #trigger gameover
                    game_over() 

            #if the player has an attribute below 5, they will get a warning
            for key, value in Players_attributes.items():
                if value <= 5:
                    print('\n' + f'{CBOLD}{CSELECTED}WARNING: {CITALIC}{key}{CEND}', end = '')
                    print(f'{CBOLD}{CSELECTED} is getting very low!{CEND}\n')
                    sleep(0.5)

            #output
            return Players_attributes[attribute_affected]       #the new value of the attribute affected
        else:
            #error message
            return 'change_decnum_abby'
    else: 
        #error message
        return 'change_attributeaffected_abby'

def choose_enchanted_item():                                    #lets the user choose an enchanted item + 
    """
    Allows the user to pick 1 out of 3 special items to boost their points 
    and adds it and its description to their inventory.
    Args:
        none
    Returns:
        none
    """
    #initiate lists
        #list to be printed
    enchanted_item_intro_list = [
        f'You begin your journey exiting a library.', 
        f'You thought to stop by before your trip home.',
        f'Before you exit the door the {CVIOLETBG2}librarian{CEND} pulls you to the side.',
        f'The wrinkles around her eyes deepen as she looks over you.', 
        f'“{CVIOLET2}Child, the journey laid in front of you is arduous.{CEND}”',
        f'“{CWHITE}Oh but that is life, ma’am. Thank you for your concern.{CEND}” you smile.',
        f'“{CVIOLET2}As accomplished as you may be,{CEND}” she implores you,',
        f'“{CVIOLET2}Allow me some peace of mind that assures me you may see home safely.{CEND}”',
        f'You nod, sensing the genuine concern this very clearly not-librarian has for you.', 
        f'She leads you to a chest and heaves it open.',
        f'“{CVIOLET2}Take one child. It will help you greatly.{CEND}”\n'
    ]
    enchanted_item_choice_list = [
        f'1: {CYELLOW}A dark vest with light embroidery.{CEND}',
        f'2: {CRED}Six rings tucked inside a pouch.{CEND}',
        f'3: {CBLUE}A dusty vintage pocket watch{CEND}\n'
        ]      
    enchanted_item_outro_list = [
        'You take your pick and thank the old not-so-woman.', 
        'As you exit the library you ruminate on what is to come.',
        'Whatever it is, you will be prepared.',
    ]

    #initiate variables

    #no input

    #process
    for i in range(2):   #adds a space in at the beginning of the story
        print(' ')  #adds space

    for i in range(len(enchanted_item_intro_list)):     #prints the intro (standard looks for every body of text) 
        #adjust indentaion of text
        temp = 26       #temporary value that is the standard indentation
        temp_2 = 0      #another temporary value that modifies the indentaion of the text
            
            #this portion modifies the indentation/layout of the text
        if i >= 4 and i <= 7 or i == 10:   #the lines w/ quotes
            if i == 5:          #if it is the player that is talking, it indents less
                temp_2 = -10
            else:
                temp_2 = 16     #if it is the librarian who is talking, indent a bit more
        else:                   #the lines without the quotes
            temp_2 = -16            #if it descriptive text, it will get the least indentation
        
        x = (temp + (temp_2))       #equation that adjusts how many spaces there will be

        #modifies the time when the lines will print
        if i >= 4 and i <= 7 or i == 10:   #the lines w/ quotes  
            sleep(0.5)                                      #adds time delay w/ quotes 
            print(' ' * x + f'{enchanted_item_intro_list[i]}')   #add the indents and then print the lines
        else: 
            #no time delay for the description part of the story
            print(' ' * x + f'{enchanted_item_intro_list[i]}') #add the indents and then print the lines
    
    sleep(1)    #delays the printing for 1 second

    while True:                             #acts on the user's choice 
        for i in enchanted_item_choice_list:    #displays the user's choices (enchanted items)
            print(i)    #prints one of the 3 choices
    
        enchanteditem_choice = input_system_ingame(3, 1)   #checks if the user's input is valid   
        global Id_enchanteditem     # get the global Id_enchanteditem so that the 
                                    # following statements can affect it; 
        global Enchanted_item_attribute     #update the characteristic of the enchanted item
                                            #as an extra layer of security

            #1(+ 2 & 3) is a string because the way I built the function
        if enchanteditem_choice == '1':     #if the user chose the vest 
                                                # it returns a str. see: input_system_ingame docstrings
            #lets the game know which item they choose
            Id_enchanteditem = 'vest'

            #identifies the attribute assigned to the enchanteditem
            Enchanted_item_attribute = 'Ethos'

            #adds the item to the user's inventory using the index
            the_inventory(0)

            #add embelishments
            name_of_enchanteditem = f'{CYELLOW}Embroidered Vest{CEND}'
            break                               #Breaks the loop once the user is done choosing.
        
        elif enchanteditem_choice == '2':   #if the user chose the rings 
            #lets the game know which item they choose
            Id_enchanteditem = 'rings'
            
            #identifies the attribute assigned to the enchanteditem
            Enchanted_item_attribute = 'Pathos'

            #adds the item to the user's inventory using the index
            the_inventory(1)

            #add embelishments
            name_of_enchanteditem = f'{CRED}6 Rings{CEND}'
            break                               #Breaks the loop once the user is done choosing.
        
        elif enchanteditem_choice == '3':   #if the user chose the watch 
            #lets the game know which item they choose
            Id_enchanteditem = 'watch'
            
            #identifies the attribute assigned to the enchanted item
            Enchanted_item_attribute = 'Logos'

            #adds the item to the user's inventory using the index
            the_inventory(2)

            #add embelishments
            name_of_enchanteditem = f'{CBLUE}Vintage Pocket Watch{CEND}'

            break                               #Breaks the loop once the user is done choosing.
        
        print(' ')                          #adds space

    for j in range(len(enchanted_item_outro_list)):     #prints the outro
        temp = 26   #temporary value that is the standard indentation
        temp_2 = 0  #another temporary value that modifies the indentaion of the text

        
        if j > 3:               #adjusts indentataion
            temp_2 = -10

        x = (temp + (temp_2))   #the equation that applies the indentation

        print(' ' * x + enchanted_item_outro_list[j]) #prints the line
        sleep(0.5)      #adds a delay
    
    #output
    print(f'\n{CITALIC}You have chosen the {name_of_enchanteditem}.{CEND}')
    print(f'{CITALIC}This choice is irreversible, use your item wisely.{CEND}\n')   #because coding that will make
                                                                                    # me go bald
    ending_embelishment('reg')
#^^assigns the value to the Id_enchanteditem variable

def enchanted_item_activated(old_points_value, enchanteditem_id):   #activates the enchanted item 
    """
    Applies the effects of the user's chosen enchanted item to their attributes.
    Is used every time points are affected during a boss fight.
    Args:
        old_points_value (int): the old value of the cost of points
        enchanteditem_id (str): identifies which enchanted item will be used
    Returns:
        new_points_value (int): the new subtrahend of the attribute affected
    """
    #initialise globals (variables/lists/dictionaries)
    global Players_attributes   #Get player's attributes
    global Id_enchanteditem     #get which enchanted item they picked
    global Enchanteditem_use_counter

    #initiate variables
    enchanteditem_id = Id_enchanteditem #identifies what enchanted item is being used from the global variable
                                        #haha they are flipped I know I'm running out of names
    new_points_value = 0        #the new points variable is set to 0. It is the number that is being 
                                # subtracted to the points of the user
    #no input
    
    #process
    if enchanteditem_id == 'vest': 
        new_points_value = math.ceil(old_points_value * 0.5)#use math.ceil to round down the 
                                                            #overall cost of points
        
        #keeps tack of how many times the enchanted item has been used
        Enchanteditem_use_counter += 1 
    elif enchanteditem_id == 'rings': 
        new_points_value = old_points_value     #the cost of points is not affected, but;
        Players_attributes['Pathos'] += 10     #adds 10 to the user's pathos attribute
        
        #keeps tack of how many times the enchanted item has been used
        Enchanteditem_use_counter += 1 
    elif enchanteditem_id == 'watch': 
        new_points_value = -old_points_value    #nullifies the cost of points completely

        #keeps tack of how many times the enchanted item has been used
        Enchanteditem_use_counter += 1  

    #output 
    print(' ' * 26 + f'You used your {CBOLD}{CITALIC}ENCHANTED ITEM{CEND}.')  #add embelishment.1
    print(' ' * 28 + f'Remaining attempts: {CBOLD}({(3 - Enchanteditem_use_counter)}/3){CEND}') #add embelishment.2
    
    #return
    return new_points_value     #the new cost of points!

def test_the_enchanteditemlimit():                              #is in every boss fight. Tells the user- 
    """
    The algorithm that every question should have to check if the user is eligible to use 
    their enchanted item
    argrs:
        none
    returns:
        status_enchanteditem (str): signifies if the user can continue using their enchanted item.
    """
    #initiate variables
    global Enchanteditem_use_counter    #summon the global variable!!
    status_enchanteditem = 'True'     #tells us if the user can use their enchanted item
    
    #no input
    
    #process
    if Enchanteditem_use_counter > 3:   #if the user is within the set bounds (3 times);
        status_enchanteditem = 'False'    #change status_enchanteditem to False 
    
    #output
    return status_enchanteditem
#^^-whether they can use their enchanted item or not

def ask_activate_enchanteditem(attribute_in_choice):            #asks if the enchanted item should be used 
    """ 
    Asks the player if they want to use thier enchanted item or not.
    Args:
        attribute_in_choice (str): the attribute that is being affected in the story.
    Returns:
        activate_enchanteditem_confirmation (str): confirm whether or not they want to use or are able 
                                                   to use their enchanted item.
    """
    #initiate varibales

    #display
    print(' ')
    print(' ' * 26 + f'{CBOLD}{CVIOLET2}Do you want to use enchanted item?{CEND}')
    print(' ' * 27 + f'{CBOLD}{CITALIC}Type 0 for no. Type 1 for yes!{CEND}\n')    

    #input
    activate_enchanteditem_confirmation = input_system_ingame(1, 0)

    #process
    if activate_enchanteditem_confirmation == '1':
        if attribute_in_choice != Enchanted_item_attribute:     #if both their attributes are the same
            activate_enchanteditem_confirmation = 'incompatible'

    #output
    return activate_enchanteditem_confirmation

def side_quest():                                               #contains all the side quests 
    """
    Generates a random situation where the user has the change to boost thier points. 
    Updates their points and keeps track of how many times they are able to do their side quests.
    Args:
        none
    Returns:
        none
    """
    #initialise lists
    side_quest_intro_list = [       #all the str's in the intro   
        f'You stop by to gather your spirit for the remaining journey.',
        f'You enter a {CBOLD}guild{CEND} and the employees beckon you to a seat.',
        f'The way we assign duties is by the {CURL}{CITALIC}roll of the dice{CEND}, they say.',
        f'They hand you a dice that is shaped to have only the number one, two, and three.', 
        f'You roll it.'
        ]
    babayaga_scenario_list = [      #all the str's in scenario #1 
        f'{CBOLD}{CVIOLET}Baba Yaga{CEND} {CITALIC}– {CYELLOW}The Cannibalistic Witch{CEND}',
        f'{CBOLD}{CGREYBG}CHALLENGE — Fetch the Seasoning!{CEND}',
        f'{CITALIC}What Seasoning do you pick?{CEND}',
        f'1: Tarragon',
        f'2: Caraway Seeds',
        f'3: Salt\n',
        f'{CVIOLET}Baba Yaga{CEND} gives you a yellow grin and shoos you away.',
        f'{CVIOLET}Baba Yaga{CEND} purses her lips and sends you off unimpressed.',
        f"On your way out of {CVIOLET}Baba Yaga's{CEND} house you suspect you may have been cursed."
        ]
    pinang_scenario_list = [        #all the str's in scenario #2 
        f'{CBOLD}{CVIOLET}Pinang{CEND} {CITALIC}– {CRED}The Hundred-Eyed Girl{CEND}',
        f'{CBOLD}{CGREYBG}CHALLENGE — Prevent her Curse!{CEND}',
        f'{CITALIC}What do you do?{CEND}',
        f'1: Bring her to her mother',
        f'2: Give her a spoon',
        f'3: Cast a spell on her\n',
        f'{CVIOLET}Pinang{CEND} thanks your profousley as she runs home with the spoon.',
        f'{CVIOLET}Pinang{CEND} sends you a thankful smile as she continues her frantic search.',
        f'{CVIOLET}Pinang{CEND} curses your name as she is dragged away by her mother.'
    ]
    naga_scenario_list = [          #all the str's in scenario #3 
        f'{CBOLD}{CVIOLET}The Naga{CEND} {CITALIC}– {CBLUE}The Half-Human Half-Serpent{CEND}',
        f'{CBOLD}{CGREYBG}CHALLENGE — Feed the Naga!{CEND}',
        f'{CITALIC}What do you feed it?{CEND}',
        f'1: Water',
        f'2: Human Meat Burger',
        f'3: Chicken Tikka Masala\n',
        f'The {CVIOLET}Naga{CEND} happily chows down on the meal you set.',
        f'The {CVIOLET}Naga{CEND} looks at you unimpressed but still drinks.',
        f'The {CVIOLET}Naga{CEND} roars in outrage and you make a run for it.'
    ]
    
    #initiate variables
    added_points = 0                    #the number that will be displayed at the end
    sidequest_attribute_affected = ''   #the attribute affected by the sidequest
    sleep_time = 0                      #assign a variable to delay time
    move_on = True                      #allows user to access profile while in a side quest

    #no input
    
    #process
    #prints the title of the page
    print('\n')                                                 #adds space
    title_profile = f'{CSELECTED}{CBOLD}SIDE QUESTS{CEND}\n'    #title of page
    print(f' ' * 46, end = '')                                    #put empty space on the same line
    for l in title_profile:                         #code that mimics a type-writer: stackoverflow 
        sys.stdout.write(l) #prints the character
        sys.stdout.flush()  #helps with buffers in the file
        time.sleep(0.1)     #delays print

        #prints the intro
    print(' ')                                                  #adds a space  

    #prints the intro of the page
    for i in range(len(side_quest_intro_list)):     #prints the intro sequence 
        temp = 26
        temp_2 = 5
    
            #adjusts the indentation
        if i == 0:
            temp_2 = -2
        elif i == 1:
            temp_2 = -1
        elif i == 2:
            temp_2 = -3
        elif i == 3:
            temp_2 = -11
        elif i == 4:
            temp_2 = 20

        x = (temp + (temp_2))

        sleep(0.5)
        print(' ' * x + f'{side_quest_intro_list[i]}')
    print(' ')    #add space 

    # generates a random number
    sidequest_assigned = random.randint(1, 3)   #generates a random number (and thus, 
                                                #side quest senario) from #'s 1-3
    print(f'The die has been rolled, you got: {CURL}{sidequest_assigned}{CEND}')  #use that number to
                                                                                  #assign each scenario
    
    if sidequest_assigned == 1:         #player encounters baba yaga 
        sidequest_attribute_affected = f'{CYELLOW}Ethos{CEND}'     #let the player know which attribute is 
                                                                #affected during their side quest
        while move_on: 
            for i in range(6):        #prints the intro scenario ONLY 
                temp = 26
                temp_2 = 0
                
                #customise indentation
                if i == 0:          #i's 1 - 2 will be moved all to the left-side
                    temp_2 = 26     #title will be indented by 46 and everything else follows
                elif i == 1: 
                    temp_2 = 29
                elif i == 2:
                    temp_2 = 34
                    sleep_time = 1  #delay time
                elif i > 2:         #the choices (1-3) will have no indentation
                    temp_2 = -26
                    sleep_time = 0.5    #delay time
                    
                x = (temp + (temp_2))   #equation that changes indentation

                print(' ' * x + f'{babayaga_scenario_list[i]}')   #print the scenario
                sleep(sleep_time)

            #acts on the player's choice
            sidequest_choice = input_system_ingame(3, 1)   #checks the user's input
            
            if sidequest_choice == '1':     #adds the most points 
                #updates attributes
                added_points = 25
                points_tally('Ethos', -25)    #adds 25 to the player's pathos points

                #outro
                print(' ')                  #adds space
                sleep(1)
                print(' ' * 35 + f'{babayaga_scenario_list[6]}')    #prints hint to player
                
                #breaks loop
                move_on = False
            elif sidequest_choice == '2':   #adds mid points 
                #updates attributes
                added_points = 20
                points_tally('Ethos', -20)

                #outro
                print(' ')                  #adds space
                sleep(1)
                print(' ' * 31 + f'{babayaga_scenario_list[7]}')    #prints hint to player
                
                #breaks loop
                move_on = False
            elif sidequest_choice == '3':   #adds the least points 
                #updates attributes
                added_points = 15
                points_tally('Ethos', -15)

                #outro
                print(' ')                  #adds space
                sleep(1)                    #delays print for suspense
                print(' ' * 14 + f'{babayaga_scenario_list[8]}')      #prints hint to player
                
                #breaks loop
                move_on = False
    elif sidequest_assigned == 2:       #player encounters pinang    
        sidequest_attribute_affected = f'{CRED}Pathos{CEND}'    #let the player know which attribute is 
                                                                #affected during their side quest
        while move_on:
            for i in range(6):       #prints the intro sequence only
                temp = 26
                temp_2 = 0
                
                #customise indentation
                if i == 0:          #i's 1 - 2 will be moved all to the left-side
                    temp_2 = 26     #title will be indented by 46 and everything else follows
                elif i == 1:
                    temp_2 = 26
                elif i == 2:
                    temp_2 = 41
                    sleep_time = 1  #delay time
                elif i > 2:         #the choices (1-3) will have no indentation
                    temp_2 = -26
                    sleep_time = 0.5    #delay time
                    
                x = (temp + (temp_2))   #equation that changes indentation

                print(' ' * x + f'{pinang_scenario_list[i]}')   #print the scenario
                sleep(sleep_time)

            #acts on the player's choice
            sidequest_choice = input_system_ingame(3, 1)   #checks the user's input
            
            if sidequest_choice == '2':     #adds the most points 
                #updates attributes
                added_points = Players_attributes['Pathos'] * 2
                if added_points > 0:
                    points_tally('Pathos', -added_points)    #adds 25 to the player's pathos points
                else:
                    points_tally('Pathos', added_points)

                #outro
                print(' ')                                      #adds space
                sleep(1)                                        #delays print for suspense
                print(' ' * 20 + f'{pinang_scenario_list[6]}')    #prints hint to player
                
                #breaks loop
                move_on = False
            elif sidequest_choice == '3':   #adds mid points 
                #updates attributes
                added_points = Players_attributes['Pathos'] * 1
                if added_points > 0:
                    points_tally('Pathos', -added_points)    #adds 25 to the player's pathos points
                else:
                    points_tally('Pathos', added_points)

                #outro
                print(' ')                                      #adds space
                sleep(1)                                        #delays print for suspense
                print(' ' * 12 + f'{pinang_scenario_list[7]}')    #prints hint to player
                
                #breaks loop
                move_on = False
            elif sidequest_choice == '1':   #adds the least points 
                #updates attributes
                added_points = math.ceil(Players_attributes['Pathos'] * 0.5)
                if added_points > 0:
                    points_tally('Pathos', -added_points)    #adds 25 to the player's pathos points
                else:
                    points_tally('Pathos', added_points)

                #outro
                print(' ')     #adds space
                sleep(1)                                        #delays print for suspense
                print(' ' * 21 + f'{pinang_scenario_list[8]}')    #prints hint to player
                
                #breaks loop
                move_on = False
    elif sidequest_assigned == 3:       #player encounters the naga  
        sidequest_attribute_affected = f'{CBLUE}Logos{CEND}'    #let the player know which attribute is 
                                                                #affected during their side quest
        while move_on:
            for i in range(6):       #prints the intro sequence only 
                temp = 26
                temp_2 = 0
                
                #customise indentation
                if i == 0:          #i's 1 - 2 will be moved all to the left-side
                    temp_2 = 26     #title will be indented by 46 and everything else follows
                elif i == 1:
                    temp_2 = 38
                elif i == 2:
                    temp_2 = 44
                    sleep_time = 1  #delay time
                elif i > 2:         #the choices (1-3) will have no indentation
                    temp_2 = -26
                    sleep_time = 0.5    #delay time
                    
                x = (temp + (temp_2))   #equation that changes indentation

                print(' ' * x + f'{naga_scenario_list[i]}')   #print the scenario
                sleep(sleep_time)

            #acts on the player's choice
            sidequest_choice = input_system_ingame(3, 1)   #checks the user's input
            
            if sidequest_choice == '3':     #adds the most points 
                #updates attributes
                added_points = Players_attributes['Logos'] * 2
                points_tally('Logos', -added_points)    #adds 25 to the player's pathos points

                #outro
                print(' ')                  #adds space
                sleep(1)
                print(' ' * 35 + f'{naga_scenario_list[6]}')    #prints hint to player

                #breaks loop
                move_on = False
            elif sidequest_choice == '1':   #adds mid points 
                #updates attributes
                added_points = 20
                points_tally('Logos', -20)

                #outro
                print(' ')                  #adds space
                sleep(1)
                print(' ' * 31 + f'{naga_scenario_list[7]}')    #prints hint to player

                #breaks loop
                move_on = False
            elif sidequest_choice == '2':   #adds the least points 
                #updates attributes
                added_points = 15
                points_tally('Logos', -15)

                #outro
                print(' ')                  #adds space
                sleep(1)                    #delays print for suspense
                print(' '*14 + f'{naga_scenario_list[8]}')      #prints hint to player
                
                #breaks loop
                move_on = False
    
    #output
    print(' ') #adds space to conclude the scenario
        #lets user know what has changed
    print(' ' * 26 + f'{CITALIC}You added {CBOLD}{added_points} points{CEND} ', end = '') 
    print(f'{CITALIC}to your {sidequest_attribute_affected} {CITALIC}attribute!{CEND}')
        #lets player know how many time they can still go on a side quest
    print(' ' * 36 + f'Remaining attempts: {CBOLD}({(3 - Sidequest_use_counter)}/3){CEND}') 
        #add embelishments
    ending_embelishment('reg')  

def ending_embelishment(type_of_embelishment):                  #adds embelishmenet at the end of functions 
    """
    To add aesthetic embeishment at the footnotes of a function
    Args:
        type_of_embelishment (str): what type of desing is appropriate for the function.
    Returns:
        none
    """
    #no input

    #process & output
    if type_of_embelishment == 'reg':           #for regular functions
        print('\n')                      #add embelishment
        print(' ' * 46 + ' ╚══ ஓ ๑ ♡ ๑ ஓ ══╝')    #add embelishment
                                        #^^Source: (https://aestheticsymbols.tumblr.com/)
        print('\n')
    elif type_of_embelishment == 'anansi':      #for the anansi arc specifically
        print('\n')
        print((' ' * 16 + f'{CBOLD}{CGREEN2}˚{CEND}{CBOLD} {CRED2}‿︵‿︵୨{CEND}{CBOLD} {CREDBG2}🕷{CEND}{CBOLD}  {CRED2}୧‿︵‿︵{CEND}{CBOLD} {CGREEN2}˚{CEND}') * 3)
                                        #^^Source: (https://emojicombos.com/spider)
        print('\n')
    elif type_of_embelishment == 'twins':       #for the hero twins arc 
        print('\n')
        print((' ' * 16 + f'{CBOLD}{CBEIGE2}┕━ 𖤓{CEND}{CBOLD} 【  {CBEIGE}𓀂{CEND}{CBOLD}  】{CBLUE2}☾ ━┙{CEND}') * 3)
        #^^Source: (https://www.aestheticsymbols.me/triangle.html)
        print('\n')
    elif type_of_embelishment == 'sunwukong':   #for the sun wukong arc 
        print('\n')
        print((' ' * 16 + f'{CBOLD}{CYELLOW2}˗ˏˋ{CEND}{CBOLD} ꒰ 𐔌  {CYELLOWBG2}鬥戰勝佛{CEND}{CBOLD} 𐦯 ꒱ {CYELLOW2}ˎˊ˗{CEND}') * 3)
        #^^Source: (https://emojicombos.com/border)
        print('\n')
    elif type_of_embelishment == 'loki':        #for the loki arc 
        print('\n')
        print((' ' * 16 + f'{CBOLD}┌──═══╡ {CGREEN}°˖ 𓆚  ˖°{CEND}{CBOLD} ╞═══──┐{CEND}') * 3)
        #^^Source: (https://emojicombos.com/border)
        print('\n')
    elif type_of_embelishment == 'end':         #for the start of the endings 
        print('\n')
        print((' ' * 16 + f'╔═══ ⌂ ═══╗') * 3)
        #^^Source: (https://www.cute-symbols.com/p/borders.html)
        print('\n')
    elif type_of_embelishment == 'ending':      #for the end of the endings
        print('\n')
        print((' ' * 56 + f'° ˛ ° ˚* _Π_____* ☽* ˚ ˛           '))
        print((' ' * 57 + f'✩ ˚˛˚*/______/__＼。✩ ˚˚˛          '))
        print((' ' * 56 + f'˚ ˛˚˛˚｜ 田田｜門｜ ˚ ˚             '))
        print((' ' * 7 + f'´´ ̛ ̛ ´´ ´´ ´´ ̛ ̛ ´´ ´´ ´´ ̛ ̛ ´´ ´´   ') * 3)
        #^^Source: (https://emojicombos.com/house)
        print('\n')

def game_over():                                                #bad ending -> game over 
    """
    Shows the user the game-over-screen. 
    Args:
        none
    Returns:
        none
    """
    #initiate variables + lists
    badending_cards = [
        f'{CWHITE}{CSELECTED}Your weakened body leads you to be {CCROSSOUT}slain{CEND}'
            f'{CWHITE}{CSELECTED} by a {CITALIC}mischievous kitsune.{CEND}',
        f'{CWHITE}{CSELECTED}Exhhaustion overtakes you. You are {CCROSSOUT}killed{CEND}'
            f'{CWHITE}{CSELECTED} by {CITALIC}vetala{CEND}'
            f'{CWHITE}{CSELECTED} possessing corpses nearby.{CEND}',
        f'{CWHITE}{CSELECTED}After days without proper food you {CCROSSOUT}die{CEND}'
            f'{CWHITE}{CSELECTED} after eating a {CITALIC}poisonous berry{CEND}.',
        f'{CWHITE}{CSELECTED}You {CCROSSOUT}die{CEND}{CWHITE}{CSELECTED}. '
            f'Your mother continues to make food. She will eat alone.{CEND}'
    ]
    game_over = [CBOLD + '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀',
        '⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⣶⡆⠀⣰⣿⠇⣾⡿⠛⠉⠁',
        '⠀⣠⣴⠾⠿⠿⠀⢀⣾⣿⣆⣀⣸⣿⣷⣾⣿⡿⢸⣿⠟⢓⠀⠀',
        '⣴⡟⠁⣀⣠⣤⠀⣼⣿⠾⣿⣻⣿⠃⠙⢫⣿⠃⣿⡿⠟⠛⠁⠀',
        '⢿⣝⣻⣿⡿⠋⠾⠟⠁⠀⠹⠟⠛⠀⠀⠈⠉⠀⠉⠀⠀⠀⠀⠀',
        '⠀⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⣀⢀⣠⣤⣴⣤⣄⠀',
        '⠀⠀⠀⠀⣀⣤⣤⢶⣤⠀⠀⢀⣴⢃⣿⠟⠋⢹⣿⣣⣴⡿⠋⠀',
        '⠀⠀⣰⣾⠟⠉⣿⡜⣿⡆⣴⡿⠁⣼⡿⠛⢃⣾⡿⠋⢻⣇⠀⠀',
        '⠀⠐⣿⡁⢀⣠⣿⡇⢹⣿⡿⠁⢠⣿⠷⠟⠻⠟⠀⠀⠈⠛⠀⠀',
        '⠀⠀⠙⠻⠿⠟⠋⠀⠀⠙⠁\n' + CEND
    ]

    #no input

    #process
    unqiue_statement = random.choice(badending_cards)
    
    #output
    #adds personalied reason of death
    print(f'\n\n{unqiue_statement}\n')
    sleep(1)  #add suspense
    for i in range(len(game_over)):
        print(' ' * 46 + game_over[i])
        sleep(0.09)


    #close the game / exit the game
    sys.exit()

def anansi_arc():                                               #the anansi arc 
    """
    Contains all the action in the Anansi Arc. Anasi is a trickster spider god from Akan folktale.
    Args:
        none
    Returns:
        none
    """
    #initialise lists and dictionaries
    anansi_arc_storyline_list = [       #the list that has all the prints in this arc 
        #pre (index: 0-7)
        f'Deeper into your journey, the days grow hotter as you cross large expanses of land.', 
        f'You have fun, greeting the locals and playing with the children with what little ' 
        f'time you can spare.',
        f'Your new friends lead you to a hut and inside is a…',
        f'{CWHITE}“Spider?”{CEND} you ask in confusion.',
        f'Your friends explain that the spider is {CREDBG2}Anansi{CEND} {CITALIC}the ' 
        f'mischievous trickster god.{CEND}',
        f'He has come down to investigate who stole his {CBOLD}magic bag{CEND}.',
        f'Hearing your infamous reputation {CREDBG2}Anansi{CEND} asks for your help.',
        f'{CBOLD}{CITALIC}{CWHITE2}What do you do?{CEND}\n',

        #anansi_pre_questions (index: 8-10)
        f'{CBOLD}1:{CEND} Use your reputation to assure {CRED2}Anansi{CEND} '
        f'that his bag will be found. [{CYELLOW}ETHOS {CITALIC}(-8){CEND}]',
        f'{CBOLD}2:{CEND} Comfort and empathise with {CRED2}Anansi{CEND}. '
        f'[{CRED}PATHOS {CITALIC}(-8){CEND}]',
        f'{CBOLD}3:{CEND} Ask for more details surrounding '
        f'{CRED2}Anansi’s{CEND} bag. [{CBLUE}LOGOS {CITALIC}(-8){CEND}]\n',

        #encounter (index: 11-16 )
        f'As you set out to find the magic bag along with {CRED2}Anansi{CEND} you discover that his '
        f'{CITALIC}magic bag{CEND} has been',
        f'stolen by none other than {CGREEN2}Mmoatia{CEND} the forest spirit.',
        f'{CREDBG2}Anansi{CEND} had angered her in his quest of storytelling.', 
        f'Seeking to make the spider god feel the humiliation she felt, the only way to calm ' 
        f'{CGREEN2}Mmoatia’s{CEND} anger ', 
        f'is through bargaining.',
        f'{CBOLD}{CITALIC}{CWHITE2}What do you say?{CEND}\n',

        #anansi_encounter_choices (index: 17-22)
        f'{CBOLD}1:{CEND} {CWHITE}"I am the infamous {CDOUBLEURL}{Player_name}{CEND}'
        f', hand over the bag before I make you!"{CEND} '
        f'[{CYELLOW}ETHOS {CITALIC}(-8){CEND}]',
        f'{CBOLD}2:{CEND} {CWHITE}"I understand your frustration, so how about we talk '
        f'about it?"{CEND} [{CRED}PATHOS {CITALIC}(-10){CEND}]', 
        f'{CBOLD}3:{CEND} {CWHITE}"There are other ways to deal with '
        f'{CRED2}Anansi{CEND} {CWHITE}so hand over the bag."{CEND} '
        f'[{CBLUE}LOGOS {CITALIC}(-8){CEND}]\n',
            #ETHOS choice leads to:
        f'{CBOLD}1:{CEND} {CWHITE}"We do not want to fight you so please hand over '
        f'the bag."{CEND} [{CRED}{CBOLD}PATHOS {CITALIC}(-5){CEND}]\n',
            #LOGOS choice leads to:
        f'{CBOLD}1:{CEND} {CWHITE}"Before the both of you destroy something precious '
        f'how about we call it quits!', 
        f'{CRED2}Anansi{CEND}{CWHITE}, stand down… please. '
        f'And {CGREEN2}Mmoatia{CEND}{CWHITE}, hand over the bag… please"{CEND} '
        f'[{CRED}{CBOLD}PATHOS {CITALIC}(-5){CEND}]\n',
        
        #encounter_EP (index: 23-24)
        f'{CGREEN2}Mmoatia{CEND} is not pleased and {CRED2}Anansi{CEND} is ready '
        f'to teach the forest spirit a lesson.',  
        f'You now realise your mistake and before a brawl begins you act quickly.\n',

        #encounter_LP (index: 25-27)
        f'{CGREEN2}Mmoatia{CEND} vehemently disagrees with you and you see a fight beginning to brew'
        f'between the two mythical beings.',
        f'If they get into a fight, {CRED2}Anansi’s{CEND} bag will most surely be destroyed.', 
        f'So you act quickly.\n',
        
        #anansi_ending (index: 28-31)
        f'After successfully returning the Magic bag to {CREDBG2}Anansi{CEND}, you bid your friends '
        f'farewell and restart your journey home.', 
        f'Before you continue on under the blazing sun {CREDBG2}Anansi{CEND} looks down on you from '
        f'the noisy hill',
        f'where your friends begin their own chores.',
        f'The god gives you a tricky smile and you tip your head to a new friend.'
    ]
    anansi_arc_ending_dictionary = {    #the dictionary (and list) that has the ending description 
        f'{CITALIC}You gained:{CEND}' : [
            f'{CRED}{CBOLD}Spider Webs{CEND} {CSELECTED}{CITALIC}(+ Inventory){CEND}',
            f'x3 {CRED}{CBOLD}Pathos Points{CEND} {CSELECTED}{CITALIC}(+ Points){CEND}'  
        ]
    }
    
    #initiate variables
    proceed_1 = True        #sentinel for the 'pre' poriton's option's
    proceed_2 = True        #sentinel for the 'encounter' portion's every 1st 
                            # while loop
    proceed_2A = True       #sentinel for the 'encounter' portion's every 
                            # nested encounter OR 2nd while loop
    anansi_newpoints = 0    #the new value being subtracted from the player's
                            #attributes after altered by their enchanted item 

    #no input

    #process
    #prints the title card of this arc
    while True:     #nested under a true loop to keep it clean 
        #title of page
        title_profile = CBOLD + CSELECTED + f'{CRED2}🕷{CEND}  {CBOLD}THE SPIDER STORYTELLER ARC{CEND} ' + CRED2 + CSELECTED + '🕷' + CEND + '\n' 
        
        #put empty space on the same line
        print(f' ' * 46, end = '')     

        #code that mimics a type-writer: from stackoverflow!
        for l in title_profile:     
            sys.stdout.write(l)
            sys.stdout.flush()
            time.sleep(0.1)

        print('\n') #add space

        #break out of loop
        break

    #prints the intro to the Anansi arc
    while True:     #nested under a true loop to keep it clean 
        for i in range(len(anansi_arc_storyline_list)):
            #adjust indentation of strings
            temp = 26   #the constant that controls indentation
            temp_2 = 0  #the variable that controls indentation
            
            if i < 7:                   #limits index to less than 7 
                if i > 3 or i < 3:      #limits index to 0-2 + 4-8 (description)
                    temp_2 = -16
            elif i == 3:                #limits index to 3  (dialouge)
                temp_2 = -10
            elif i == 7:                #limits index to 7 (the question)
                temp_2 = 26

            x = (temp + (temp_2))   #the equation that controls indentation
            
            #modifies time it will print and prints the lines
            if i == 3 or i == 7:            #limits to the quotes and the question
                sleep(1)        #add delay for suspense
                print(' ' * x + f'{anansi_arc_storyline_list[i]}')
                sleep(1)        #add delay for suspense
            elif i < 3 or i > 3 and i < 8:  #limits to description 
                print(' ' * x + f'{anansi_arc_storyline_list[i]}')
        break     #break out of loop
    
    #the 'pre' portion of the Anansi Arc 
    while True:     #nested here for optimal cleanliness 
        #print the pre ecounter choices 
        for j in range(len(anansi_arc_storyline_list)):
            #adjust indentation of strings
            temp = 26   #the constant that controls indentation
            temp_2 = 0  #the variable that controls indentation

            #customises the indentation
            temp_2 = -26

            x = (temp + (temp_2))    #the equation that adjusts the inentation of str's
            
            #prints the lines
            if j > 7 and j < 11:    #limits it to the questions
                print(' ' * x + anansi_arc_storyline_list[j])
                sleep(0.5)          #add timer for suspense
                
        #lets user make their choice
        anansi_choice_pre = input_system_ingame(3, 1)

        #acts on what the user chose
        if anansi_choice_pre == '1':    #user chooses option 1 
            #acts on the user's choice
            while proceed_1:
                #checks if they would like to use their enchanted item and if they CAN use it 
                enchanteditem_checker_argument = ask_activate_enchanteditem('Ethos')

                #updates the points, etc.
                if enchanteditem_checker_argument == '0':       #if user does not want to use their item
                    #update the player's points
                    points_tally('Ethos', 8) 

                    #print message to user
                    print('\n' + ' ' * 26 + f'You have spent {CBOLD}{CITALIC}{CYELLOW}8{CEND} ', end = '')
                    print(f'{CBOLD}{CYELLOW}Ethos points{CEND}!')

                    #break out of mini-loop
                    proceed_1 = False
                else:       
                    if enchanteditem_checker_argument == '1':   
                        if test_the_enchanteditemlimit() == 'True': #checks if user can use enchanted item
                            #saves the new points
                            anansi_newpoints = enchanted_item_activated(8, Id_enchanteditem)
                            
                            #update points 
                            points_tally('Ethos', anansi_newpoints)
                            
                            #print message to user
                            print(' ' * 26 + f'You have spent ', end = '')
                            print(f'{CBOLD}{CITALIC}{CYELLOW}{anansi_newpoints} ', end = '')
                            print(f'{CBOLD}{CYELLOW}Ethos points{CEND}!')

                            #break out of mini-loop
                            proceed_1 = False
                        else:
                            #print message to player that their chances are maxxed out
                            print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You exceeded uses for the{CEND}', end = '')
                            print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n')
                    elif enchanteditem_checker_argument == 'incompatible':       #in other words, if the enchanted item is incompatible 
                        #print out message that they cannot use thier enchanted item
                        print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You cannot use your{CEND}', end = '')
                        print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n') 
            
            #break out of big while loop
            break
        elif anansi_choice_pre == '2':  #user chooses option 2 
            #acts on the user's choice
            while proceed_1:
                #checks if they would like to use their enchanted item and if they CAN use it 
                enchanteditem_checker_argument = ask_activate_enchanteditem('Pathos')
                
                #updates the points, etc.
                if enchanteditem_checker_argument == '0':       #if user does not want to use their item
                    #update the player's points
                    points_tally('Pathos', 8) 

                    #print message to user
                    print('\n' + ' ' * 26 + f'You have spent {CBOLD}{CITALIC}{CRED}8{CEND} ', end = '')
                    print(f'{CBOLD}{CRED}Pathos points{CEND}!')

                    #break out of mini-loop        
                    proceed_1 = False
                else:                                       #if user want to use their item
                    if enchanteditem_checker_argument == '1':
                        if test_the_enchanteditemlimit() == 'True': #checks if user can use enchanted item 
                            #saves the new points
                            anansi_newpoints = enchanted_item_activated(8, Id_enchanteditem)
                            
                            #update points 
                            points_tally('Pathos', anansi_newpoints)

                            #print message to user
                            print(' ' * 26 + f'You have spent ', end = '')
                            print(f'{CBOLD}{CITALIC}{CRED}{anansi_newpoints} ', end = '')
                            print(f'{CBOLD}{CRED}Pathos points{CEND}!')

                            #break out of loop 
                            proceed_1 = False
                        else:
                            #print message to player that their chances are maxxed out
                            print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You exceeded uses for the{CEND}', end = '')
                            print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n')            
                    elif enchanteditem_checker_argument == 'incompatible': #enchanted item = incompatible
                        #print out message that they cannot use thier enchanted item
                        print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You cannot use your{CEND}', end = '')
                        print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n') 
        
            #break out of big while loop
            break
        elif anansi_choice_pre == '3':  #user chooses option 3 
            #acts on the user's choice
            while proceed_1:
                #checks if they would like to use their enchanted item and if they CAN use it 
                enchanteditem_checker_argument = ask_activate_enchanteditem('Logos')

                #updates the points, etc.
                if enchanteditem_checker_argument == '0':       #if user does not want to use their item
                    #update the player's points
                    points_tally('Logos', 8) 

                    #print message to user
                    print('\n' + ' ' * 26 + f'You have spent {CBOLD}{CITALIC}{CBLUE}8{CEND} ', end = '')
                    print(f'{CBOLD}{CBLUE}Logos points{CEND}!')

                    #break out of mini-loop        
                    proceed_1 = False
                else:   #if user wants to use their item 
                    if enchanteditem_checker_argument == '1':
                        if test_the_enchanteditemlimit() == 'True': #checks if user can use enchanted item 
                            #saves the new points
                            anansi_newpoints = enchanted_item_activated(8, Id_enchanteditem)
                            
                            #update points 
                            points_tally('Logos', anansi_newpoints)
                            
                            #print message to user
                            print(' ' * 26 + f'You have spent ', end = '')
                            print(f'{CBOLD}{CITALIC}{CBLUE}{anansi_newpoints} ', end = '')
                            print(f'{CBOLD}{CBLUE}Logos points{CEND}!')

                            #break out of mini-loop 
                            proceed_1 = False
                        else: 
                            #print message to player that their chances are maxxed out
                            print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You exceeded uses for the{CEND}', end = '')
                            print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n')            
                    elif enchanteditem_checker_argument == 'incompatible': #enchanted item = incompatible
                        #print out message that they cannot use thier enchanted item
                        print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You cannot use your{CEND}', end = '')
                        print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n') 
            
            #break out of big while loop
            break

    ending_embelishment('anansi')   #add embelishments!
    sleep(1)    #add suspense w/ delay

    #prints intro to the encounter in the Anansi arc
    while True:     #nested under a true loop for neatness
        for n in range(len(anansi_arc_storyline_list)): 
            temp = 26   #the constant that controls indentation
            temp_2 = 0  #the variable that controls indentation

            #adjusts indentation of strings
            if n < 16 and n > 10:   #limits it to index: 11-14
                temp_2 = -16
            elif n == 16:           #limits it to index 14
                temp_2 = 26     #indents the question 

            x = (temp + (temp_2))   #the equation that adjusts indentation

            #modifies time it will print and prints the lines
            if n < 16 and n > 10:   #limits to index: 11-15 
                print(' ' * x + f'{anansi_arc_storyline_list[n]}')
            elif n == 16:           #limits to index 16
                sleep(1)        #add delay for suspense
                print(' ' * x + f'{anansi_arc_storyline_list[n]}')
                sleep(1)        #add delay for suspense
        
        #break out of loop
        break   

    #the 'encounter' portion of the Anansi Arc
    while True:     #contents are under while loop for neatness 
        #prints the encounter choices
        for k in range(len(anansi_arc_storyline_list)): 
            #adjust indentation of strings
                temp = 26   #the constant that controls indentation
                temp_2 = 0  #the variable that controls indentation

                #customises the indentation
                temp_2 = -26

                x = (temp + (temp_2))    #the equation that adjusts the inentation of str's
                
                #prints the lines
                if k < 20 and k > 16 :    #limits it to the questions
                    print(' ' * x + anansi_arc_storyline_list[k])
                    sleep(0.5)  #add delay for suspense

        #lets the user make their choice
        anansi_choice_encounter = input_system_ingame(3, 1)      

        #acts on what the user choice
        if anansi_choice_encounter == '1':    #If their choice was 1 
            #the first part of option 1
            while proceed_2:        #acts on the user's choice 
                #checks if they would like to use their enchanted item and if they CAN use it 
                enchanteditem_checker_argument = ask_activate_enchanteditem('Ethos')

                #updates the points, etc.
                if enchanteditem_checker_argument == '0':         #if user does NOT want to use their item
                    #update the player's points
                    points_tally('Ethos', 8) 

                    #print message to user
                    print('\n' + ' ' * 26 + f'You have spent {CBOLD}{CITALIC}{CYELLOW}8{CEND} ', end = '')
                    print(f'{CBOLD}{CYELLOW}Ethos points{CEND}!')   
                    
                    #break out of mini while loop
                    proceed_2 = False   
                elif enchanteditem_checker_argument == 'incompatible':                                           #if user wants to use their item 
                    if enchanteditem_checker_argument == '1':
                        if enchanteditem_checker_argument == 'True': #checks if user can use enchanted item
                            #saves the new points
                            anansi_newpoints = enchanted_item_activated(8, Id_enchanteditem)
                            
                            #update points 
                            points_tally('Ethos', anansi_newpoints)
                            
                            #print message to user
                            print(' ' * 26 + f'You have spent ', end = '')
                            print(f'{CBOLD}{CITALIC}{CYELLOW}{anansi_newpoints} ', end = '')
                            print(f'{CBOLD}{CYELLOW}Ethos points{CEND}!')
                            
                            #break out of mini while loop
                            proceed_2 = False
                        else:
                            #print message to player that their chances are maxxed out
                            print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You exceeded uses for the{CEND}', end = '')
                            print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n')
                    else:       #in other words, if the enchanted item is incompatible
                        #print out message that they cannot use thier enchanted item
                        print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You cannot use your{CEND}', end = '')
                        print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n') 

            #add embelishments and suspense (adjust time)
            sleep(1)
            ending_embelishment('anansi')
            sleep(1)

            #in-between story portion for option 1
            for u in range(len(anansi_arc_storyline_list)): 
                #adjust indentation of strings
                temp = 26   #the constant that controls indentation
                temp_2 = 0  #the variable that controls indentation

                #customises the indentation
                temp_2 = -16

                x = (temp + (temp_2))    #the equation that adjusts the inentation of str's
                
                #prints the lines
                if u == 23:     #limits index to: 23 
                    print(' ' * x + anansi_arc_storyline_list[u])
                elif u == 24:   #limits index to: 24 
                    print(' ' * x + anansi_arc_storyline_list[u])
                    sleep(1)        #add delay for suspense

            #the second part of option 1
            while proceed_2A:     #code is under a while loop for neatness and repeatability 
                #prints choice(s)
                print(anansi_arc_storyline_list[20])    
                sleep(1)        #add timer for suspense
            
                #lets player 'choose' 
                anansi_choice_encounter_subcategory = input_system_ingame(1, 1)
                
                #updates the points, etc.
                if anansi_choice_encounter_subcategory == '1': 
                    #checks if they would like to use their enchanted item and if they CAN use it 
                    enchanteditem_checker_argument = ask_activate_enchanteditem('Pathos')
                    
                    #does what the user said^^
                    if enchanteditem_checker_argument == '0':         #if user does NOT want to use their item
                        #update the player's points
                        points_tally('Pathos', 5) 

                        #print message to user
                        print('\n' + ' ' * 26 + f'You have spent {CBOLD}{CITALIC}{CRED}5{CEND} ', end = '')
                        print(f'{CBOLD}{CRED}Pathos points{CEND}!')  
                        
                        #break out of mini while loop
                        proceed_2A = False       
                    else:                 #if user wants to use their item 
                        if enchanteditem_checker_argument == '1':
                            if test_the_enchanteditemlimit() == 'True': #checks if user can use enchanted item
                                #saves the new points
                                anansi_newpoints = enchanted_item_activated(8, Id_enchanteditem)
                                
                                #update points 
                                points_tally('Pathos', anansi_newpoints)

                                #print message to user
                                print(' ' * 26 + f'You have spent ', end = '')
                                print(f'{CBOLD}{CITALIC}{CRED}{anansi_newpoints} ', end = '')
                                print(f'{CBOLD}{CRED}Pathos points{CEND}!')
                                
                                #break out of mini while loop
                                proceed_2A = False
                            else:
                                #print message to player that their chances are maxxed out
                                print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You exceeded uses for the{CEND}', end = '')
                                print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n')
                        elif enchanteditem_checker_argument == 'incompatible':       #in other words, if the enchanted item is incompatible
                            #print out message that they cannot use thier enchanted item
                            print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You cannot use your{CEND}', end = '')
                            print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n') 

            #break out of the big while loop
            break 
        elif anansi_choice_encounter == '2':  #If their choice was 2 
            #acts on the user's choice
            while proceed_2:        #use while loop and sentinel to access profile and side quests
                #checks if they would like to use their enchanted item and if they CAN use it 
                enchanteditem_checker_argument = ask_activate_enchanteditem('Pathos')

                #updates the points, etc.
                if enchanteditem_checker_argument == '0':       #if user does not want to use their item 
                    #update the player's points
                    points_tally('Pathos', 10) 

                    #print message to user
                    print('\n' + ' ' * 26 + f'You have spent {CBOLD}{CITALIC}{CRED}10{CEND} ', end = '')
                    print(f'{CBOLD}{CRED}Pathos points{CEND}!')

                    #break out of mini-loop 
                    proceed_2 = False
                else:                                       #if user want to use their item
                    if enchanteditem_checker_argument == '1':
                        if test_the_enchanteditemlimit() == 'True': #checks if user can use enchanted item 
                            #saves the new points
                            anansi_newpoints = enchanted_item_activated(8, Id_enchanteditem)
                            
                            #update points 
                            points_tally('Pathos', anansi_newpoints)

                            #print message to user
                            print(' ' * 26 + f'You have spent ', end = '')
                            print(f'{CBOLD}{CITALIC}{CRED}{anansi_newpoints} ', end = '')
                            print(f'{CBOLD}{CRED}Pathos points{CEND}!')

                            #break out of mini-loop 
                            proceed_2 = False
                        else:
                            #print message to player that their chances are maxxed out
                            print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You exceeded uses for the{CEND}', end = '')
                            print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n')
                    elif enchanteditem_checker_argument == 'incompatible': #enchanted item = incompatible
                        #print out message that they cannot use thier enchanted item
                        print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You cannot use your{CEND}', end = '')
                        print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n') 

            #break out of the big big while loop
            break      
        elif anansi_choice_encounter == '3':      #If their choice was 3 
            #the first part of option 3
            while proceed_2:     #nested under a true loop for neatness 
                #checks if they would like to use their enchanted item and if they CAN use it 
                enchanteditem_checker_argument = ask_activate_enchanteditem('Logos')

                #updates the points, etc.
                if enchanteditem_checker_argument == '0':         #if user does NOT want to use their item
                    #update the player's points
                    points_tally('Logos', 8) 

                    #print message to user
                    print('\n' + ' ' * 26 + f'You have spent {CBOLD}{CITALIC}{CBLUE}8{CEND} ', end = '')
                    print(f'{CBOLD}{CBLUE}Logos points{CEND}!')  
                    
                    #break out of mini while loop
                    proceed_2 = False        
                else:                                           #if user wants to use their item 
                    if enchanteditem_checker_argument == '1':
                        if test_the_enchanteditemlimit() == 'True': #checks if user can use enchanted item
                            #saves the new points
                            anansi_newpoints = enchanted_item_activated(8, Id_enchanteditem)
                            
                            #update points 
                            points_tally('Logos', anansi_newpoints)

                            #print message to user
                            print(' ' * 26 + f'You have spent ', end = '')
                            print(f'{CBOLD}{CITALIC}{CBLUE}{anansi_newpoints} ', end = '')
                            print(f'{CBOLD}{CBLUE}Logos points{CEND}!')
                            
                            #break out of mini while loop
                            proceed_2 = False
                        else:
                            #print message to player that their chances are maxxed out
                            print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You exceeded uses for the{CEND}', end = '')
                            print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n')
                    elif enchanteditem_checker_argument == 'incompatible': #enchanted item = incompatible
                        #print out message that they cannot use thier enchanted item
                        print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You cannot use your{CEND}', end = '')
                        print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n') 

            #add embelishments and suspense (adjuSt time)
            sleep(1)
            ending_embelishment('anansi')
            sleep(1)

            #in-between story portion for option 1
            for o in range(len(anansi_arc_storyline_list)): 
                #adjust indentation of strings
                temp = 26   #the constant that controls indentation
                temp_2 = 0  #the variable that controls indentation

                #customises the indentation
                temp_2 = -16

                x = (temp + (temp_2))    #the equation that adjusts the inentation of str's
                
                #prints the lines
                if o > 24 and o < 27 :    #limits it to index: 25-26 
                    print(' ' * x + anansi_arc_storyline_list[o])
                elif o == 27:               #limits index to 27 
                    print(' ' * x + anansi_arc_storyline_list[o])
                    sleep(1)    #delay time to add suspense

            #the second part of option 3
            while proceed_2A:     #code is under a while loop for neatness and repeatability 
                #prints choice(s)
                print(anansi_arc_storyline_list[21])
                print(anansi_arc_storyline_list[22])
                sleep(1)        #add timer for suspense

                #lets player 'choose' 
                anansi_choice_encounter_subcategory = input_system_ingame(1, 1)
                
                #updates the points, etc.
                if anansi_choice_encounter_subcategory == '1': 
                    #checks if they would like to use their enchanted item and if they CAN use it 
                    enchanteditem_checker_argument = ask_activate_enchanteditem('Pathos')

                    #asks user if they want to use their enchanted item
                    if enchanteditem_checker_argument == '0':         #if user does NOT want to use their item
                        #update the player's points
                        points_tally('Pathos', 5) 

                        #print message to user
                        print('\n' + ' ' * 26 + f'You have spent {CBOLD}{CITALIC}{CRED}5{CEND} ', end = '')
                        print(f'{CBOLD}{CRED}Pathos points{CEND}!')  

                        #break out of mini while loop
                        proceed_2A = False       
                    else:                                             #if user wants to use their item 
                        if enchanteditem_checker_argument == '1':
                            if test_the_enchanteditemlimit() == 'True': #checks if user can use enchanted item
                                #saves the new points
                                anansi_newpoints = enchanted_item_activated(8, Id_enchanteditem)

                                #update points 
                                points_tally('Pathos', anansi_newpoints)

                                #print message to user
                                print(' ' * 26 + f'You have spent ', end = '')
                                print(f'{CBOLD}{CITALIC}{CRED}{anansi_newpoints} ', end = '')
                                print(f'{CBOLD}{CRED}Ethos points{CEND}!')
                                
                                #break out of mini while loop
                                proceed_2A = False 
                            else:
                                #print message to player that their chances are maxxed out
                                print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You exceeded uses for the{CEND}', end = '')
                                print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n')
                        elif enchanteditem_checker_argument == 'incompatible': #enchanted item = incompatible
                            #print out message that they cannot use thier enchanted item
                            print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You cannot use your{CEND}', end = '')
                            print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n') 

            #break out of the big big while loop
            break
            
    #the 'ending' portion of the anansi arc
    while True:     #contents are under while loop for neatness 
        #add embelishments: newline for neatness and timer for suspense
        print('\n')
        sleep(1)

        #print the final portion of the Anansi Arc 
        for p in range(len(anansi_arc_storyline_list)): 
            #adjust indentation of strings
            temp = 26   #the constant that controls indentation
            temp_2 = 0  #the variable that controls indentation

            #adjusts indentation
            if p < 31 and p > 27:   #limits index to: 28-30 
                temp_2 = -16
            elif p == 31:           #limits index to: 31 
                temp_2 = -10

            x = (temp + (temp_2))   #the equation that controls indentation
            
            #modifies the time and prints the strings
            if p < 31 and p > 27:   #limits index to: 28-30 
                print(' ' * x + f'{anansi_arc_storyline_list[p]}')
            elif p == 31:           #limits index to: 31 
                sleep(1)
                print(' ' * x + f'{anansi_arc_storyline_list[p]}')
                sleep(1)
        
        #break out of while loop
        break

    ending_embelishment('anansi')   #add embelishments!
    sleep(1)    #add suspense w/ delay

    #the summary and rewarads of the anansi arc
    while True:     #contents are under while loop for neatness 
        #prints the rewards and summary
        for title, rewards in anansi_arc_ending_dictionary.items():     #display the body w/ format 
            print(' ' * 5 + title)     #name = key, goes thorugh the dictionary one by one
            sleep(0.5)  #delays printing of title
            for reward in rewards:    #description = values in list, goes thorugh each value in list
                print(' ' * 10 + reward)     #adds indent and description
                sleep(0.5)  #delays printing of each body of text

        #acts on the rewards: updates users attributes and inventory
        the_inventory(4)
        points_tally('Pathos', -(Players_attributes['Pathos'] * 3))     #increases player's points

        #break out of while loop
        break

    #output
    ending_embelishment('anansi')

def junajpu_ixbalanke_arc():                                    #the junajpu & ixb'alanke arc 
    """ 
    Contains all the action in the Junajpu and Ixb'alanke Arc aka. The Hero Twins arc. 
    Junajpu and Ixb'alanke are a pair of twins from Mayan folklore.
    
    args:
        none
    returns:
        none
    """
    #initialise lists and dictionaries
    herotwins_arc_storyline_list = [    #the list that has all the prints in this arc 
            #pre (index: 0-2)
            f'To avoid any troublesome encounters you decide to journey into a secret underground ' 
            f'tunnel system.',
            f'You come across a courtyard reminiscent of {CBEIGE}Maya Ballgame{CEND} court.',
            f'{CBOLD}{CITALIC}{CWHITE2}What do you do?{CEND}\n',

            #twins_pre_questions (index: 3-6)
            f'{CBOLD}1:{CEND} Curious seeing the ancient ball court, you recite old facts that you ' 
            f'know as you walk around as if ',
            f'\tto prove that; {CITALIC}{CWHITE}‘Yes, I know a thing or two!’{CEND}. ' 
            f'[{CYELLOW}ETHOS {CITALIC}(-8){CEND}]',
            f'{CBOLD}2:{CEND} Overcome with sentiment, you practice a few of your own moves with ' 
            f'the ball lying on the court. [{CRED}PATHOS {CITALIC}(-8){CEND}]',
            f'{CBOLD}3:{CEND} Walk right past it, you don’t want to anger anyone. '
            f'[{CBLUE}LOGOS {CITALIC}(-8){CEND}]\n',

            #encounter_1 (index: 7-15)
            f'Before you can blink a loud rumbling echoes through the court.',
            f'Two figures approach you.',
            f'They recognize you as the infamous unbeatable mortal.',
            f'After exchanging greetings, {CBEIGEBG}the twins{CEND} say,',
            f'{CBEIGE2}“We would like to see if you live up to your reputation, ',
            f'play one round with us and we’ll get you out of the tunnels.”{CEND}',
            f'The protection of two of the {CBOLD}most crafty gods{CEND} is invaluable.',
            f'However, as friendly as they are, you have no idea what they’ll do should you ' 
            f'lose in a {CBOLD}ball game{CEND}.',
            f'{CBOLD}{CITALIC}{CWHITE2}What do you say?{CEND}\n',

            #twins_encounter_1_choices (index: 16-18)
            f'{CBOLD}1:{CEND} {CWHITE}“Instead of playing, I can help you redecorate the court.”{CEND} ' 
            f'[{CYELLOW}ETHOS {CITALIC}(-8){CEND}]',
            f'{CBOLD}2:{CEND} {CWHITE}"Instead of playing, how about teaching a thing or two to me?"{CEND} ' 
            f'[{CRED}PATHOS {CITALIC}(-5){CEND}]',
            f'{CBOLD}3:{CEND} ' 
            f'{CWHITE}"Sorry, I need to go home. I will play with you some other time!"{CEND} '
            f'[{CBLUE}LOGOS {CITALIC}(-10){CEND}]\n',

            #enounter_2 (index: 19-23)
            f'The {CBEIGEBG}the twins{CEND} decide to go along with your suggestion but as you are ' 
            f'about to exit the courtyard, ',
            f'the statues surrounding you start to come to life!',
            f'The {CGREYBG}malicious gods{CEND} of the underworld have come to irritate ' 
            f'{CBEIGEBG}the twins{CEND} after another loss in a game of ball.',
            f'As the {CBEIGEBG}the twins{CEND} are preoccupied with fighting the gods off,',
            f'{CBOLD}{CITALIC}{CWHITE2}What do you do?{CEND}\n',

            #twins_encounter_2_choices (index: 24 & 25)
            f'{CBOLD}1:{CEND} Help them out! [{CBLUE}LOGOS {CITALIC}(-5){CEND}]',
            f'{CBOLD}2:{CEND} Run towards the unguarded exit! [{CBLUE}LOGOS {CITALIC}(-2){CEND}]\n',
            # (index: 26)
            f'{CBOLD}1:{CEND} {CWHITE}Yell for help!{CEND} [{CBLUE}LOGOS {CITALIC}(-5){CEND}]\n',

            #encounter_2_LP-5 (index: 27 & 28)
            f'{CBLUE2}Junajpu{CEND} looks back and grins as you slither your way through the '
            f'{CGREYBG}massive gods{CEND}. ',
            f'{CBEIGE2}Ixb’alanke{CEND} throws you a club and together the three of you subdue '
            f'the {CGREYBG}butthurt gods{CEND}.\n',
            
            #encounter_2_LP-2 (index: 29-32)
            f'An {CGREYBG}enormous fist{CEND} snatches you just before you reach the exit! ',
            f'{CGREYBG}The god{CEND} considers you like one would consider a mosquito before it is killed. ',
            f'{CITALIC}{CGREYBG}“Pesky coward…”{CEND} It hisses. ',
            f'You feel it’s crushing grip around your chest and body, you…',
            #(index: 33-35)
            f'Hearing your scream, {CBEIGEBG}the twins{CEND} slay the god and bring you back to your senses.',
            f'{CBLUE2}Junajpu{CEND} and {CBEIGE2}Ixb’alanke{CEND} look at you with not ' 
            f'little amounts of disappointment. ',
            f'Your pride is halved.',

            #twins ending (index: 36-39)
            f'As you breathe in the warm wind and feel the moonlight on your skin, ' 
            f'you look back to see {CBLUE2}Junajpu{CEND} and {CBEIGE2}Ixb’alanke{CEND} at the '
            f'mouth of the tunnels. ',
            f'{CBEIGEBG}The twins{CEND} send you identical looks and give you a wave before ' 
            f'returning to defeat more gods in a game of ball.',
            f'You look at your path ahead and trudge on.',
            f'The journey home is a long one yet is nevertheless one that is worth every suffering.'
        ]
    herotwins_arc_ending_dictionary = { #the dictionary (and list) that has the ending description 
    f'{CITALIC}You gained:{CEND}' : [
        f'{CBEIGE}{CBOLD}Mosquito Jar{CEND} {CSELECTED}{CITALIC}(+ Inventory){CEND}',
        f'x3 {CBLUE}{CBOLD}Logos Points{CEND} {CSELECTED}{CITALIC}(+ Points){CEND}'
        ]
        }

    #initiate variables
    proceed_1 = True        #sentinel for the 'pre' poriton's option's
    proceed_11 = True       #sentinel for 'encounter' part 1
    proceed_2 = True        #sentinel for the 'encounter' portion's every 1st 
                            # while loop
    proceed_2A = True       #sentinel for the 'encounter' portion's every 
                            # nested encounter OR 2nd while loop
    twins_newpoints = 0    #the new value being subtracted from the player's
                            #attributes after altered by their enchanted item 

    #no input

    #process
    #prints the title card of this arc
    while True:    #nested under a true loop to keep it clean 
        #title of page
        title_profile = CBOLD + CSELECTED + f'{CBLUE2}𖤓 {CEND} {CBOLD}THE HERO TWINS ARC{CEND}' + f' {CBLUE2}☾{CEND}' + '\n' 
        
        #put empty space on the same line
        print(f' ' * 46, end = '')     

        #code that mimics a type-writer: from stackoverflow!
        for l in title_profile:     
            sys.stdout.write(l)
            sys.stdout.flush()
            time.sleep(0.1)
        
        print('\n') #add space

        #break out of loop
        break

    #prints the intro to the Hero Twins arc
    while True:   #contents are under while loop for neatness 
        for ii in range(len(herotwins_arc_storyline_list)):
            #adjust indentation of strings
            temp = 26   #the constant that controls indentation
            temp_2 = 0  #the variable that controls indentation
            
            if ii == 0 or ii == 1:        #limits index to 0 and 1
                temp_2 =-16
            elif ii == 2:                #limits index to 2 (the question)
                temp_2 = 26

            x = (temp + (temp_2))   #the equation that controls indentation
            
            #modifies time it will print and prints the lines
            if ii == 2:            #limits to the question
                sleep(1)        #add delay for suspense
                print(' ' * x + f'{herotwins_arc_storyline_list[ii]}')
                sleep(1)        #add delay for suspense
            elif ii == 0 or ii == 1:  #limits to description 
                print(' ' * x + f'{herotwins_arc_storyline_list[ii]}')
        break     #break out of loop
    
    #the 'pre' portion of the Hero Twins arc
    while True:   #contents are under while loop for neatness 
        #prints the pre choices
        for jj in range(len(herotwins_arc_storyline_list)): 
            #adjust indentation of strings
            temp = 26   #the constant that controls indentation
            temp_2 = 0  #the variable that controls indentation

            #customises the indentation
            temp_2 = -26

            x = (temp + (temp_2))    #the equation that adjusts the inentation of str's
            
            #prints the lines w/ timer
            if jj > 2 and jj < 7:     #limits index to 3-6
                print(' ' * x + herotwins_arc_storyline_list[jj])
                sleep(0.5)          #add timer for suspense
        
        #lets user make their choice
        twins_choice_pre = input_system_ingame(3, 1)

        #acts on what the user chose
        if twins_choice_pre == '1':    #user chooses option 1 
            #acts on the user's choice
            while proceed_1: 
                #checks if they would like to use their enchanted item and if they CAN use it 
                enchanteditem_checker_argument = ask_activate_enchanteditem('Ethos')

                #updates the points, etc.
                if enchanteditem_checker_argument == '0':       #if user does not want to use their item
                    #update the player's points
                    points_tally('Ethos', 8) 

                    #print message to user
                    print('\n' + ' ' * 26 + f'You have spent {CBOLD}{CITALIC}{CYELLOW}8{CEND} ', end = '')
                    print(f'{CBOLD}{CYELLOW}Ethos points{CEND}!')

                    #break out of mini-loop
                    proceed_1 = False
                else:       #if the user wants to use their enchanted item
                    if enchanteditem_checker_argument == '1':     
                        if test_the_enchanteditemlimit() == 'True': #checks if user can use enchanted item
                            #saves the new points
                            twins_newpoints = enchanted_item_activated(8, Id_enchanteditem)
                            
                            #update points 
                            points_tally('Ethos', twins_newpoints)
                            
                            #print message to user
                            print(' ' * 26 + f'You have spent ', end = '')
                            print(f'{CBOLD}{CITALIC}{CYELLOW}{twins_newpoints} ', end = '')
                            print(f'{CBOLD}{CYELLOW}Ethos points{CEND}!')

                            #break out of mini-loop
                            proceed_1 = False
                        else:
                            #print message to player that their chances are maxxed out
                            print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You exceeded uses for the{CEND}', end = '')
                            print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n')
                    elif enchanteditem_checker_argument == 'incompatible': #enchanted item = incompatible
                        #print out message that they cannot use thier enchanted item
                        print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You cannot use your{CEND}', end = '')
                        print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n') 
            
            #break out of big while loop
            break
        elif twins_choice_pre == '2':  #user chooses option 2 
            #acts on the user's choice
            while proceed_1: 
                #checks if they would like to use their enchanted item and if they CAN use it 
                enchanteditem_checker_argument = ask_activate_enchanteditem('Pathos')
                
                #updates the points, etc.
                if enchanteditem_checker_argument == '0':       #if user does not want to use their item
                    #update the player's points
                    points_tally('Pathos', 8) 

                    #print message to user
                    print('\n' + ' ' * 26 + f'You have spent {CBOLD}{CITALIC}{CRED}8{CEND} ', end = '')
                    print(f'{CBOLD}{CRED}Pathos points{CEND}!')

                    #break out of mini-loop        
                    proceed_1 = False
                else:                                       #if user want to use their item
                    if enchanteditem_checker_argument == '1': 
                        if test_the_enchanteditemlimit() == 'True': #checks if user can use enchanted item 
                            #saves the new points
                            twins_newpoints = enchanted_item_activated(8, Id_enchanteditem)
                            
                            #update points 
                            points_tally('Pathos', twins_newpoints)

                            #print message to user
                            print(' ' * 26 + f'You have spent ', end = '')
                            print(f'{CBOLD}{CITALIC}{CRED}{twins_newpoints} ', end = '')
                            print(f'{CBOLD}{CRED}Pathos points{CEND}!')

                            #break out of loop 
                            proceed_1 = False
                        else:
                            #print message to player that their chances are maxxed out
                            print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You exceeded uses for the{CEND}', end = '')
                            print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n')            
                    elif enchanteditem_checker_argument == 'incompatible': #enchanted item = incompatible
                        #print out message that they cannot use thier enchanted item
                        print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You cannot use your{CEND}', end = '')
                        print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n') 
        
            #break out of big while loop
            break
        elif twins_choice_pre == '3':  #user chooses option 3 
            #acts on the user's choice
            while proceed_1: 
                #checks if they would like to use their enchanted item and if they CAN use it 
                enchanteditem_checker_argument = ask_activate_enchanteditem('Logos')

                #updates the points, etc.
                if enchanteditem_checker_argument == '0':       #if user does not want to use their item
                    #update the player's points
                    points_tally('Logos', 8) 

                    #print message to user
                    print('\n' + ' ' * 26 + f'You have spent {CBOLD}{CITALIC}{CBLUE}8{CEND} ', end = '')
                    print(f'{CBOLD}{CBLUE}Logos points{CEND}!')

                    #break out of mini-loop        
                    proceed_1 = False
                else:                                       #if user wants to use their item 
                    if enchanteditem_checker_argument == '1':
                        if test_the_enchanteditemlimit() == 'True': #checks if user can use enchanted item 
                            #saves the new points
                            twins_newpoints = enchanted_item_activated(8, Id_enchanteditem)
                            
                            #update points 
                            points_tally('Logos', twins_newpoints)
                            
                            #print message to user
                            print(' ' * 26 + f'You have spent ', end = '')
                            print(f'{CBOLD}{CITALIC}{CBLUE}{twins_newpoints} ', end = '')
                            print(f'{CBOLD}{CBLUE}Logos points{CEND}!')

                            #break out of mini-loop 
                            proceed_1 = False
                        else: 
                            #print message to player that their chances are maxxed out
                            print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You exceeded uses for the{CEND}', end = '')
                            print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n')            
                    elif enchanteditem_checker_argument == 'incompatible': #enchanted item = incompatible
                        #print out message that they cannot use thier enchanted item
                        print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You cannot use your{CEND}', end = '')
                        print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n') 
            
            #break out of big while loop
            break

    ending_embelishment('twins')   #add embelishments!
    sleep(1)    #add suspense w/ delay

    #prints intro to the 1st encounter in the Hero Twins Arc
    while True:     #contents are under while loop for neatness 
        #prints intro to the 1st encounter
        for nn in range(len(herotwins_arc_storyline_list)):
            #adjust indentation of strings
            temp = 26   #the constant that controls indentation
            temp_2 = 0  #the variable that controls indentation

            #customises the indentation
            if nn > 6 and nn < 11:
                temp_2 = -16
            elif nn == 11 or nn == 12:
                temp_2 = 16
            elif nn > 12 and nn < 15:
                temp_2 = -16
            elif nn == 15:
                temp_2 = 26

            x = (temp + (temp_2))    #the equation that adjusts the inentation of str's
            
            #prints the lines w/ timer
            if (nn > 6 and nn < 11) or (nn > 12 and nn < 15):
                print(' ' * x + herotwins_arc_storyline_list[nn])
            elif nn == 11 or nn == 12 or nn == 15:
                sleep(0.5)        #add delay for suspense
                print(' ' * x + f'{herotwins_arc_storyline_list[nn]}')
                sleep(0.5)        #add delay for suspense

        #break out of the loop
        break

    #the 'encounter 1' portion of the Hero Twins Arc
    while True:     #contents are under while loop for neatness 
        #prints the encounter choices
        for k in range(len(herotwins_arc_storyline_list)): 
            #adjust indentation of strings
                temp = 26   #the constant that controls indentation
                temp_2 = 0  #the variable that controls indentation

                #customises the indentation
                temp_2 = -26

                x = (temp + (temp_2))    #the equation that adjusts the inentation of str's
                
                #prints the lines
                if k > 15 and k < 19 :    #limits it to the questions
                    print(' ' * x + herotwins_arc_storyline_list[k])
                    sleep(0.5)  #add delay for suspense

        #lets the user make their choice
        twins_choice_encounter_1 = input_system_ingame(3, 1)      

        # #acts on the user's choice        
        if twins_choice_encounter_1 == '1':    #If their choice was 1 
            while proceed_11:        #acts on the user's choice 
                #checks if they would like to use their enchanted item and if they CAN use it 
                enchanteditem_checker_argument = ask_activate_enchanteditem('Ethos')

                #updates the points, etc.
                if enchanteditem_checker_argument == '0':         #if user does NOT want to use their item
                    #update the player's points
                    points_tally('Ethos', 8) 

                    #print message to user
                    print('\n' + ' ' * 26 + f'You have spent {CBOLD}{CITALIC}{CYELLOW}8{CEND} ', end = '')
                    print(f'{CBOLD}{CYELLOW}Ethos points{CEND}!')   
                    
                    #break out of mini while loop
                    proceed_11 = False   
                else:                                           #if user wants to use their item 
                    if enchanteditem_checker_argument == '1':
                        if test_the_enchanteditemlimit == 'True': #checks if user can use enchanted item
                            #saves the new points
                            twins_newpoints = enchanted_item_activated(8, Id_enchanteditem)
                            
                            #update points 
                            points_tally('Ethos', twins_newpoints)
                            
                            #print message to user
                            print(' ' * 26 + f'You have spent ', end = '')
                            print(f'{CBOLD}{CITALIC}{CYELLOW}{twins_newpoints} ', end = '')
                            print(f'{CBOLD}{CYELLOW}Ethos points{CEND}!')
                            
                            #break out of mini while loop
                            proceed_11 = False
                        else:
                            #print message to player that their chances are maxxed out
                            print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You exceeded uses for the{CEND}', end = '')
                            print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n')
                    elif enchanteditem_checker_argument == 'incompatible': #enchanted item = incompatible
                        #print out message that they cannot use thier enchanted item
                        print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You cannot use your{CEND}', end = '')
                        print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n') 

            #break out of the big while loop
            break 
        elif twins_choice_encounter_1 == '2':  #If their choice was 2 
            while proceed_11:        #acts on the user's choice 
                #checks if they would like to use their enchanted item and if they CAN use it 
                enchanteditem_checker_argument = ask_activate_enchanteditem('Pathos')

                #updates the points, etc.
                if enchanteditem_checker_argument == '0':         #if user does NOT want to use their item
                    #update the player's points
                    points_tally('Pathos', 5) 

                    #print message to user
                    print('\n' + ' ' * 26 + f'You have spent {CBOLD}{CITALIC}{CRED}5{CEND} ', end = '')
                    print(f'{CBOLD}{CRED}Pathos points{CEND}!')   
                    
                    #break out of mini while loop
                    proceed_11 = False   
                else:                                           #if user wants to use their item 
                    if enchanteditem_checker_argument == '1':
                        if test_the_enchanteditemlimit == 'True': #checks if user can use enchanted item
                            #saves the new points
                            twins_newpoints = enchanted_item_activated(5, Id_enchanteditem)
                            
                            #update points 
                            points_tally('Pathos', twins_newpoints)
                            
                            #print message to user
                            print(' ' * 26 + f'You have spent ', end = '')
                            print(f'{CBOLD}{CITALIC}{CRED}{twins_newpoints} ', end = '')
                            print(f'{CBOLD}{CRED}Pathos points{CEND}!')
                            
                            #break out of mini while loop
                            proceed_11 = False
                        else:
                            #print message to player that their chances are maxxed out
                            print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You exceeded uses for the{CEND}', end = '')
                            print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n')
                    elif enchanteditem_checker_argument == 'incompatible': #enchanted item = incompatible
                        #print out message that they cannot use thier enchanted item
                        print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You cannot use your{CEND}', end = '')
                        print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n') 

            #break out of the big while loop
            break       
        elif twins_choice_encounter_1 == '3':      #If their choice was 3 
            while proceed_11:        #acts on the user's choice 
                #checks if they would like to use their enchanted item and if they CAN use it 
                enchanteditem_checker_argument = ask_activate_enchanteditem('Logos')

                #updates the points, etc.
                if enchanteditem_checker_argument == '0':         #if user does NOT want to use their item
                    #update the player's points
                    points_tally('Logos', 10) 

                    #print message to user
                    print('\n' + ' ' * 26 + f'You have spent {CBOLD}{CITALIC}{CBLUE}10{CEND} ', end = '')
                    print(f'{CBOLD}{CBLUE}Logos points{CEND}!')   
                    
                    #break out of mini while loop
                    proceed_11 = False   
                else:                                           #if user wants to use their item 
                    if enchanteditem_checker_argument == '1':
                        if enchanteditem_checker_argument == 'True': #checks if user can use enchanted item
                            #saves the new points
                            twins_newpoints = enchanted_item_activated(10, Id_enchanteditem)
                            
                            #update points 
                            points_tally('Logos', twins_newpoints)
                            
                            #print message to user
                            print(' ' * 26 + f'You have spent ', end = '')
                            print(f'{CBOLD}{CITALIC}{CBLUE}{twins_newpoints} ', end = '')
                            print(f'{CBOLD}{CBLUE}Logos points{CEND}!')
                            
                            #break out of mini while loop
                            proceed_11 = False
                        else:
                            #print message to player that their chances are maxxed out
                            print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You exceeded uses for the{CEND}', end = '')
                            print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n')
                    elif enchanteditem_checker_argument == 'incompatible': #enchanted item = incompatible
                        #print out message that they cannot use thier enchanted item
                        print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You cannot use your{CEND}', end = '')
                        print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n') 

            #break out of the big big while loop
            break
   
    ending_embelishment('twins')   #add embelishments!
    sleep(1)    #add suspense w/ delay

    # prints the intro to the 2nd encounter in the Hero TWins Arc
    while True: 
        #prints intro to the 2nd encounter
        for m in range(len(herotwins_arc_storyline_list)):
            #adjust indentation of strings
            temp = 26   #the constant that controls indentation
            temp_2 = 0  #the variable that controls indentation

            #customises the indentation
            if m == 23:
                temp_2 = 26
            elif m > 18 and m < 23:
                temp_2 = -16 

            x = (temp + (temp_2))    #the equation that adjusts the inentation of str's
            
            #prints the lines w/ timer
            if m > 18 and m < 23:
                print(' ' * x + herotwins_arc_storyline_list[m])
            elif m == 23:
                sleep(0.5)        #add delay for suspense
                print(' ' * x + f'{herotwins_arc_storyline_list[m]}')
                sleep(0.5)        #add delay for suspense

        #break out of the loop
        break
            
    #the 'encounter 2' portion of the Hero Twins arc
    while True: 
        #prints the 'encounter 2' questions
        for mm in range(len(herotwins_arc_storyline_list)):
            #adjust indentation of strings
            temp = 26   #the constant that controls indentation
            temp_2 = 0  #the variable that controls indentation

            #customises the indentation
            if mm == 24 or mm == 25:
                temp_2 = -26

            x = (temp + (temp_2))    #the equation that adjusts the inentation of str's
            
            #prints the lines w/ timer
            if mm == 24 or mm == 25:
                print(' ' * x + f'{herotwins_arc_storyline_list[mm]}')
                sleep(0.5)        #add delay for suspense
        
        #lets the user make their choice
        twins_choice_encounter_2 = input_system_ingame(2, 1)

        #acts on the player's choice
        if twins_choice_encounter_2 == '1': #If their choice was 1 
            #acts on the user's choice
            while proceed_2:        #use while loop and sentinel to access profile and side quests
                #checks if they would like to use their enchanted item and if they CAN use it 
                enchanteditem_checker_argument = ask_activate_enchanteditem('Logos')

                #updates the points, etc.
                if enchanteditem_checker_argument == '0':       #if user does not want to use their item 
                    #update the player's points
                    points_tally('Logos', 5) 

                    #print message to user
                    print('\n' + ' ' * 26 + f'You have spent {CBOLD}{CITALIC}{CBLUE}5{CEND} ', end = '')
                    print(f'{CBOLD}{CBLUE}Logos points{CEND}!')

                    #break out of mini-loop 
                    proceed_2 = False
                else:                                       #if user want to use their item
                    if enchanteditem_checker_argument == '1':
                        if test_the_enchanteditemlimit() == 'True': #checks if user can use enchanted item 
                            #saves the new points
                            twins_newpoints = enchanted_item_activated(5, Id_enchanteditem)
                            
                            #update points 
                            points_tally('Logos', twins_newpoints)

                            #print message to user
                            print(' ' * 26 + f'You have spent ', end = '')
                            print(f'{CBOLD}{CITALIC}{CBLUE}{twins_newpoints} ', end = '')
                            print(f'{CBOLD}{CBLUE}Logos points{CEND}!')

                            #break out of mini-loop 
                            proceed_2 = False
                        else:
                            #print message to player that their chances are maxxed out
                            print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You exceeded uses for the{CEND}', end = '')
                            print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n')
                    elif enchanteditem_checker_argument == 'incompatible': #enchanted item = incompatible
                        #print out message that they cannot use thier enchanted item
                        print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You cannot use your{CEND}', end = '')
                        print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n') 

            #add space for neatness
            print('\n')
            sleep(1)    #add suspense

            #prints the finale of 'encounter 2'
            for q in range(len(herotwins_arc_storyline_list)): 
                #adjust indentation of strings
                temp = 26   #the constant that controls indentation
                temp_2 = 0  #the variable that controls indentation

                #customises the indentation
                if q == 27 or q == 28:
                    temp_2 = -16

                x = (temp + (temp_2))    #the equation that adjusts the inentation of str's
                
                #prints the lines w/ timer
                if q == 27 or q == 28:
                    print(' ' * x + f'{herotwins_arc_storyline_list[q]}')
                    sleep(0.5)        #add delay for suspense

            #break out of the big big while loop
            break      
        elif twins_choice_encounter_2 == '2': #If their choice was 2 
            #the first part of option 2
            while proceed_2:     #nested under a true loop for neatness 
                #checks if they would like to use their enchanted item and if they CAN use it 
                enchanteditem_checker_argument = ask_activate_enchanteditem('Logos')

                #updates the points, etc.
                if enchanteditem_checker_argument == '0':         #if user does NOT want to use their item
                    #update the player's points
                    points_tally('Logos', 2) 

                    #print message to user
                    print('\n' + ' ' * 26 + f'You have spent {CBOLD}{CITALIC}{CBLUE}2{CEND} ', end = '')
                    print(f'{CBOLD}{CBLUE}Logos points{CEND}!\n')  
                    
                    #break out of mini while loop
                    proceed_2 = False        
                else:                                           #if user wants to use their item 
                    if enchanteditem_checker_argument == '1':
                        if test_the_enchanteditemlimit() == 'True': #checks if user can use enchanted item
                            #saves the new points
                            twins_newpoints = enchanted_item_activated(2, Id_enchanteditem)
                            
                            #update points 
                            points_tally('Logos', twins_newpoints)

                            #print message to user
                            print(' ' * 26 + f'You have spent ', end = '')
                            print(f'{CBOLD}{CITALIC}{CBLUE}{twins_newpoints} ', end = '')
                            print(f'{CBOLD}{CBLUE}Logos points{CEND}!')
                            
                            #break out of mini while loop
                            proceed_2 = False
                        else:
                            #print message to player that their chances are maxxed out
                            print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You exceeded uses for the{CEND}', end = '')
                            print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n')
                    elif enchanteditem_checker_argument == 'incompatible': #enchanted item = incompatible
                        #print out message that they cannot use thier enchanted item
                        print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You cannot use your{CEND}', end = '')
                        print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n') 

            #in-between story portion for option 1
            for oo in range(len(herotwins_arc_storyline_list)): 
                #adjust indentation of strings
                temp = 26   #the constant that controls indentation
                temp_2 = 0  #the variable that controls indentation

                #customises the indentation
                if oo == 29 or oo == 30 or oo == 32:
                    temp_2 = -16
                elif oo == 31:
                    temp_2 = 16

                x = (temp + (temp_2))    #the equation that adjusts the inentation of str's
                
                #prints the lines and adjusts the timing
                if oo == 29:    #the first line
                    sleep(0.5)  #add suspense
                    print(' ' * x + herotwins_arc_storyline_list[oo])
                elif oo == 30:  #the middle lines
                    print(' ' * x + herotwins_arc_storyline_list[oo])
                elif oo == 31:  #the middle lines 
                    print(' ' * x + herotwins_arc_storyline_list[oo])
                    sleep(0.5)    #add suspense
                elif oo == 32:  #the last line
                    print(' ' * x + herotwins_arc_storyline_list[oo])
                    print(' ')  #add space
                    sleep(1)    #add suspense

            #the second part of option 2
            while proceed_2A:     #code is under a while loop for neatness and repeatability 
                #prints choice(s)
                print(herotwins_arc_storyline_list[26])
                sleep(1)        #add timer for suspense

                #lets player 'choose' 
                twins_choice_encounter_subcategory = input_system_ingame(1, 1)
                
                #updates the points, etc.
                if twins_choice_encounter_subcategory == '1': 
                    #checks if they would like to use their enchanted item and if they CAN use it 
                    enchanteditem_checker_argument = ask_activate_enchanteditem('Logos')

                    #asks user if they want to use their enchanted item
                    if enchanteditem_checker_argument == '0':         #if user does NOT want to use their item
                        #update the player's points
                        points_tally('Logos', 5) 

                        #print message to user
                        print('\n' + ' ' * 26 + f'You have spent {CBOLD}{CITALIC}{CBLUE}5{CEND} ', end = '')
                        print(f'{CBOLD}{CBLUE}Logos points{CEND}!')  

                        #break out of mini while loop
                        proceed_2A = False       
                    else:                                           #if user wants to use their item 
                        if enchanteditem_checker_argument == '1':
                            if test_the_enchanteditemlimit() == 'True': #checks if user can use enchanted item
                                #saves the new points
                                twins_newpoints = enchanted_item_activated(5, Id_enchanteditem)

                                #update points 
                                points_tally('Logos', twins_newpoints)

                                #print message to user
                                print(' ' * 26 + f'You have spent ', end = '')
                                print(f'{CBOLD}{CITALIC}{CBLUE}{twins_newpoints} ', end = '')
                                print(f'{CBOLD}{CBLUE}Logos points{CEND}!\n')
                                
                                #break out of mini while loop
                                proceed_2A = False 
                            else:
                                #print message to player that their chances are maxxed out
                                print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You exceeded uses for the{CEND}', end = '')
                                print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n')
                        elif enchanteditem_checker_argument == 'incompatible': #enchanted item = incompatible
                            #print out message that they cannot use thier enchanted item
                            print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You cannot use your{CEND}', end = '')
                            print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n') 

            #prints the outro to choice '1'
            for w in range(len(herotwins_arc_storyline_list)): 
                #adjust indentation of strings
                temp = 26   #the constant that controls indentation
                temp_2 = 0  #the variable that controls indentation

                #customises the indentation
                if w > 32 and w < 36:
                    temp_2 = -16
                
                x = (temp + (temp_2))    #the equation that adjusts the inentation of str's
                
                #prints the lines
                if w > 33 and w < 36:
                    print(' ' * x + herotwins_arc_storyline_list[w])
                elif w == 33:       #the first line of the outro
                    print(' ')  #add space for neateness
                    sleep(0.5)    #add suspense
                    print(' ' * x + herotwins_arc_storyline_list[w])
                    
            #break out of the big big while loop
            break

    #add embelishments and suspense (adjuSt time)
    sleep(1)
    ending_embelishment('twins')
    sleep(1)

    #the 'ending' portion of the Hero Twins arc
    while True:     #contents are under while loop for neatness 
        #print the final portion of the Anansi Arc 
        for ww in range(len(herotwins_arc_storyline_list)): 
            #adjust indentation of strings
            temp = 26   #the constant that controls indentation
            temp_2 = 0  #the variable that controls indentation

            #adjusts indentation
            if ww > 35 and ww < 40:
                temp_2 = -16            

            x = (temp + (temp_2))   #the equation that controls indentation
            
            #modifies the time and prints the strings
            if ww > 35 and ww < 39:   #limits index to: 36-39
                print(' ' * x + herotwins_arc_storyline_list[ww])
            elif ww == 39:
                sleep(0.5)  #add timer for suspense
                print(' ' * x + herotwins_arc_storyline_list[ww])
                sleep(1)    #add timer for suspense

        #break out of while loop
        break

    ending_embelishment('twins')   #add embelishments!
    sleep(1)    #add suspense w/ delay

    #prints the summary and rewards of the Hero twins arc  
    while True:     #contents are under while loop for neatness 
        #prints the rewards and summary
        for title, rewards in herotwins_arc_ending_dictionary.items():     #display the body w/ format 
            print(' ' * 5 + title)     #name = key, goes thorugh the dictionary one by one
            sleep(0.5)  #delays printing of title
            for reward in rewards:    #description = values in list, goes thorugh each value in list
                print(' ' * 10 + reward)     #adds indent and description
                sleep(0.5)  #delays printing of each body of text

        #acts on the rewards: updates users attributes and inventory
        the_inventory(5)
        points_tally('Logos', -(Players_attributes['Logos'] * 3))   #increases player's points

        #break out of while loop
        break 
                
    #output
    ending_embelishment('twins')   #add embelishments!
    sleep(1)    #add suspense w/ delay 

def sun_wukong_arc():                                           #the sunwukong arc 
    """ 
    Contains all the action in the Sun Wukong arc. Sun Wukong is a mythical
    being from Chinese mythology, specifically in the novel 'Journey to the West'.
    
    args:
        none
    returns:
        none
    """
    #initialise lists and dictionaries
    sunwukong_arc_storyline_list = [    #the list that has all the prints in this arc
        #pre (index: 0-5)
        f'As you continue your journey you stumble upon a pile of bamboo haphazardly stacked in the '
            f'entrance of the bridge to cross the river.',
        f'You hear a pained yowl and as you look into the pile you see an injured… {CVIOLETBG}Pig?{CEND}',
        f'It certainly isn’t any ordinary animal.',
        f'You feel an aura of power illuminating from under '
            f'its skin.',
        f'Curiosity and concern intertwine as the {CVIOLETBG}pig{CEND} stirs and mumbles.',
        f'{CBOLD}{CITALIC}{CWHITE2}What do you do?{CEND}\n',

        #sunwukong_pre_questions (index: 6-8 )
        f'{CBOLD}1:{CEND} You look around for clues as to what happened and try to coax the '
            f'{CVIOLETBG}pig{CEND} to open its eyes. [{CYELLOW}ETHOS {CITALIC}(-10){CEND}]',
        f'{CBOLD}2:{CEND} You quickly approach the {CVIOLETBG}pig{CEND} to help it. '
            f'[{CRED}PATHOS {CITALIC}(-10){CEND}]',
        f'{CBOLD}3:{CEND} You leave ointments on the ground but do not check on the {CVIOLETBG}pig{CEND} '
            f'and find another way to cross the river. [{CBLUE}LOGOS {CITALIC}(-10){CEND}]\n',
        
        #encounter (index: 9-19)
        f'Before you can do anything meaningful, a loud thud comes from behind you.', 
        f'Standing on a staff too tall, too decorated, too powerful not to be from a mythical being.',
        f'Its figure is clad in armour, its hairy, monkey body is a yellow colour, '
            f'and atop its head is a crown on a face that looks absolutely furious.', 
        f'{CYELLOW2}“You dare hurt one of my brothers.”{CEND} {CYELLOWBG2}Sun Wukong’s{CEND}{CYELLOW2} voice booms.',
        f'{CYELLOW2}“For this you will pay, however, I recognise you, {CDOUBLEURL}{Player_name}{CEND}{CYELLOW2}." ',
        f'{CYELLOW2}"Your battles against the celestial court have been..."{CEND}',
        f'{CYELLOW2}"Great entertainment and for that I’ll give you mercy.”{CEND}',
        f'Any hope you have is quickly crushed by his next words.', 
        f'A feral grin appears on the god’s face,', 
        f'{CYELLOW2}“Any last words?”{CEND}',
        f'{CBOLD}{CITALIC}{CWHITE2}What do you say?{CEND}\n',

        #sunwukong_encounter_choices (index: 20-22)
        f'{CBOLD}1:{CEND} {CWHITE}"I would never hurt your friend! I do not pick fights and my '
            f'reputation speaks for itself."{CEND} [{CYELLOW}ETHOS {CITALIC}(-12){CEND}]',
        f'{CBOLD}2:{CEND} {CWHITE}"I understand your anger but it was not me who hurt your '
            f'friend."{CEND} [{CRED}PATHOS {CITALIC}(-10){CEND}]',
        f'{CBOLD}3:{CEND} {CWHITE}"I could not have hurt your monkey! I left them ointments don’t '
            f'you see?"{CEND} [{CBLUE}LOGOS {CITALIC}(-7){CEND}]\n',
        # (index: 23)
        f'{CBOLD}1:{CEND} {CWHITE}"I would never hurt your friend! I do not pick fights and '
            f'my reputation speaks for itself."{CEND} [{CYELLOW}ETHOS {CITALIC}(-12){CEND}]\n',

        #encounter_PP (index: 24-26)
        f'{CYELLOWBG2}Sun Wukong{CEND} snorts and jumps down from his Ruyi Jingu Bang.',
        f'{CYELLOW2}“Are those your final words, Mortal? Disappointing!”{CEND}',
        f'Sensing an incoming fight you will most definitely lose, you act quickly.\n',

        #encounter_LP (index: 27-29)
        f'{CYELLOW2}“Oh oh, I see! I completely believe you–not! I know a trickster when I see one.”{CEND}', 
        f'He laughs, shrill and mischievous.',
        f'Sensing a fight where you are at a disadvantage you act quickly.\n', 

        #sunwukong ending (index: 30-34)
        f'After clearing the misunderstanding and healing {CYELLOWBG2}Sun Wukong’s{CEND} friend, '
            f'who you learned is named ',
        f'{CVIOLETBG}Zhu Bajie{CEND}, the trio of you remove the clutter blocking the mouth of the bridge.', 
        f'You share laughs across the bridge as you share stories with '
            f'{CYELLOWBG2}Sun Wukong{CEND} and {CVIOLETBG}Zhu Bajie{CEND}.', 
        f'They bid you goodbye as they journey deeper into the forests.', 
        f'You walk away happy with more new acquaintances than you started and continue your journey home.'
    ]
    sunwukong_arc_ending_dictionary = { #the dictionary (and list) that has the ending description 
        f'{CITALIC}You gained:{CEND}' : [
            f'{CYELLOWBG2}{CBOLD}Mini Magic Staff{CEND} {CSELECTED}{CITALIC}(+ Inventory){CEND}',
            f'x3 {CYELLOW}{CBOLD}Ethos Points{CEND} {CSELECTED}{CITALIC}(+ Points){CEND}\n'
        ]
    }

    #initiate variables
    proceed_1 = True        #sentinel for the 'pre' poriton's option's
    proceed_2 = True        #sentinel for the 'encounter' portion's every 1st 
                            # while loop
    proceed_2A = True       #sentinel for the 'encounter' portion's every 
                            # nested encounter OR 2nd while loop
    sunwukong_newpoints = 0 #the new value being subtracted from the player's
                            #attributes after altered by their enchanted item 

    #no input

    #process
    #prints title card of this arc
    while True:     #nested under a true loop to keep it clean 
        #title of page
        title_profile = CBOLD + f'{CYELLOW2}˗ˏˋ{CEND}  {CBOLD}{CSELECTED}THE VICTORIOUS FIGHTING BUDDHA ARC{CEND}' + f' {CYELLOW2}ˎˊ˗{CEND}' + '\n' 
        
        #put empty space on the same line
        print(f' ' * 46, end = '')     

        #code that mimics a type-writer: from stackoverflow!
        for l in title_profile:     
            sys.stdout.write(l)
            sys.stdout.flush()
            time.sleep(0.1)

        print('\n') #add space

        #break out of loop
        break

    #prints the intro to the Sun Wukong arc
    while True:     #contents are under while loop for neatness 
        for ii in range(len(sunwukong_arc_storyline_list)):
            #adjust indentation of strings
            temp = 26   #the constant that controls indentation
            temp_2 = 0  #the variable that controls indentation
            
            if ii >= 0 and ii < 5:        #limits index to 0-3
                temp_2 = -16
            elif ii == 5:                #limits index to 4 (the question)
                temp_2 = 26

            x = (temp + (temp_2))   #the equation that controls indentation
            
            #modifies time it will print and prints the lines
            if ii == 5:            #limits to the question
                sleep(1)        #add delay for suspense
                print(' ' * x + f'{sunwukong_arc_storyline_list[ii]}')
                sleep(1)        #add delay for suspense
            elif ii >= 0 and ii < 5:  #limits to description 
                print(' ' * x + f'{sunwukong_arc_storyline_list[ii]}')
        break     #break out of loop

    #the 'pre' portion of the Sun Wukong arc
    while True:     #contents are under while loop for neatness 
        #prints the pre choices
        for jj in range(len(sunwukong_arc_storyline_list)): 
            #adjust indentation of strings
            temp = 26   #the constant that controls indentation
            temp_2 = 0  #the variable that controls indentation

            #customises the indentation
            temp_2 = -26

            x = (temp + (temp_2))    #the equation that adjusts the inentation of str's
            
            #prints the lines w/ timer
            if jj > 5 and jj < 9:     #limits index to 3-6
                print(' ' * x + sunwukong_arc_storyline_list[jj])
                sleep(0.5)          #add timer for suspense
        
        #lets user make their choice
        sunwukong_choice_pre = input_system_ingame(3, 1)

        #acts on what the user chose
        if sunwukong_choice_pre == '1':    #user chooses option 1 
            #acts on the user's choice
            while proceed_1: 
                #checks if they would like to use their enchanted item and if they CAN use it 
                enchanteditem_checker_argument = ask_activate_enchanteditem('Ethos')

                #updates the points, etc.
                if enchanteditem_checker_argument == '0':       #if user does not want to use their item
                    #update the player's points
                    points_tally('Ethos', 10) 

                    #print message to user
                    print('\n' + ' ' * 26 + f'You have spent {CBOLD}{CITALIC}{CYELLOW}10{CEND} ', end = '')
                    print(f'{CBOLD}{CYELLOW}Ethos points{CEND}!\n')

                    #break out of mini-loop
                    proceed_1 = False
                else:       #if the user wants to use their enchanted item
                    if enchanteditem_checker_argument == '1':     
                        if test_the_enchanteditemlimit() == 'True': #checks if user can use enchanted item
                            #saves the new points
                            sunwukong_newpoints = enchanted_item_activated(10, Id_enchanteditem)
                            
                            #update points 
                            points_tally('Ethos', sunwukong_newpoints)
                            
                            #print message to user
                            print(' ' * 26 + f'You have spent ', end = '')
                            print(f'{CBOLD}{CITALIC}{CYELLOW}{sunwukong_newpoints} ', end = '')
                            print(f'{CBOLD}{CYELLOW}Ethos points{CEND}!\n')

                            #break out of mini-loop
                            proceed_1 = False
                        else:
                            #print message to player that their chances are maxxed out
                            print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You exceeded uses for the{CEND}', end = '')
                            print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n')
                    elif enchanteditem_checker_argument == 'incompatible':       #in other words, if the enchanted item is incompatible
                        #print out message that they cannot use thier enchanted item
                        print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You cannot use your{CEND}', end = '')
                        print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n') 
            
            #break out of big while loop
            break
        elif sunwukong_choice_pre == '2':  #user chooses option 2 
            #acts on the user's choice
            while proceed_1: 
                #checks if they would like to use their enchanted item and if they CAN use it 
                enchanteditem_checker_argument = ask_activate_enchanteditem('Pathos')
                
                #updates the points, etc.
                if enchanteditem_checker_argument == '0':       #if user does not want to use their item
                    #update the player's points
                    points_tally('Pathos', 10) 

                    #print message to user
                    print('\n' + ' ' * 26 + f'You have spent {CBOLD}{CITALIC}{CRED}10{CEND} ', end = '')
                    print(f'{CBOLD}{CRED}Pathos points{CEND}!\n')

                    #break out of mini-loop        
                    proceed_1 = False
                else:                                       #if user want to use their item
                    if enchanteditem_checker_argument == '1': 
                        if test_the_enchanteditemlimit() == 'True': #checks if user can use enchanted item 
                            #saves the new points
                            sunwukong_newpoints = enchanted_item_activated(10, Id_enchanteditem)
                            
                            #update points 
                            points_tally('Pathos', sunwukong_newpoints)

                            #print message to user
                            print(' ' * 26 + f'You have spent ', end = '')
                            print(f'{CBOLD}{CITALIC}{CRED}{sunwukong_newpoints} ', end = '')
                            print(f'{CBOLD}{CRED}Pathos points{CEND}!\n')

                            #break out of loop 
                            proceed_1 = False
                        else:
                            #print message to player that their chances are maxxed out
                            print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You exceeded uses for the{CEND}', end = '')
                            print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n')            
                    elif enchanteditem_checker_argument == 'incompatible': #enchanted item = incompatible
                        #print out message that they cannot use thier enchanted item
                        print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You cannot use your{CEND}', end = '')
                        print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n') 
        
            #break out of big while loop
            break
        elif sunwukong_choice_pre == '3':  #user chooses option 3 
            #acts on the user's choice
            while proceed_1: 
                #checks if they would like to use their enchanted item and if they CAN use it 
                enchanteditem_checker_argument = ask_activate_enchanteditem('Logos')

                #updates the points, etc.
                if enchanteditem_checker_argument == '0':       #if user does not want to use their item
                    #update the player's points
                    points_tally('Logos', 10) 

                    #print message to user
                    print('\n' + ' ' * 26 + f'You have spent {CBOLD}{CITALIC}{CBLUE}10{CEND} ', end = '')
                    print(f'{CBOLD}{CBLUE}Logos points{CEND}!\n')

                    #break out of mini-loop        
                    proceed_1 = False
                else:                                       #if user wants to use their item 
                    if enchanteditem_checker_argument == '1':
                        if test_the_enchanteditemlimit() == 'True': #checks if user can use enchanted item 
                            #saves the new points
                            sunwukong_newpoints = enchanted_item_activated(10, Id_enchanteditem)
                            
                            #update points 
                            points_tally('Logos', sunwukong_newpoints)
                            
                            #print message to user
                            print(' ' * 26 + f'You have spent ', end = '')
                            print(f'{CBOLD}{CITALIC}{CBLUE}{sunwukong_newpoints} ', end = '')
                            print(f'{CBOLD}{CBLUE}Logos points{CEND}!\n')

                            #break out of mini-loop 
                            proceed_1 = False
                        else: 
                            #print message to player that their chances are maxxed out
                            print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You exceeded uses for the{CEND}', end = '')
                            print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n')            
                    elif enchanteditem_checker_argument == 'incompatible': #enchanted item = incompatible
                        #print out message that they cannot use thier enchanted item
                        print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You cannot use your{CEND}', end = '')
                        print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n') 
            
            #break out of big while loop
            break

    ending_embelishment('sunwukong')   #add embelishments!
    sleep(1)    #add suspense w/ delay
    
    #prints the intro to encounter
    while True:     #contents are under while loop for neatness 
        #prints intro to the 1st encounter
        for nn in range(len(sunwukong_arc_storyline_list)):
            #adjust indentation of strings
            temp = 26   #the constant that controls indentation
            temp_2 = 0  #the variable that controls indentation

            #customises the indentation 
            if (nn > 11 and nn < 16) or nn == 18: #the quotes 
                temp_2 = 16
            elif (nn > 8 and nn < 12) or nn == 16 or nn == 17:  #the descriptions
                temp_2 = -16
            elif nn == 19:  #the question
                temp_2 = 26

            x = (temp + (temp_2))    #the equation that adjusts the inentation of str's
            
            #prints the lines w/ timer
            if (nn > 8 and nn < 12) or nn == 16 or nn == 17: #prints the description
                print(' ' * x + sunwukong_arc_storyline_list[nn])
            elif (nn > 11 and nn < 16) or nn == 18 or nn == 19:  #prints the quotes
                sleep(0.5)        #add delay for suspense
                print(' ' * x + f'{sunwukong_arc_storyline_list[nn]}')
                sleep(0.5)        #add delay for suspense

        #break out of the loop
        break

    #the 'encounter' portion of the Sun Wukong arc
    while True:     #contents are under while loop for neatness 
        #prints the 'encounter 2' questions
        for mm in range(len(sunwukong_arc_storyline_list)): 
            #adjust indentation of strings
            temp = 26   #the constant that controls indentation
            temp_2 = 0  #the variable that controls indentation

            #customises the indentation
            if mm > 19 and mm < 23:
                temp_2 = -26

            x = (temp + (temp_2))    #the equation that adjusts the inentation of str's
            
            #prints the lines w/ timer
            if mm > 19 and mm < 23:
                print(' ' * x + f'{sunwukong_arc_storyline_list[mm]}')
                sleep(0.5)        #add delay for suspense
        
        #lets the user make their choice
        sunwukong_choice_encounter = input_system_ingame(3, 1)

        #acts on the player's choice
        if sunwukong_choice_encounter == '1': #If their choice was 1 
            #the first part of option 3
            while proceed_2:     #nested under a true loop for neatness 
                #checks if they would like to use their enchanted item and if they CAN use it 
                enchanteditem_checker_argument = ask_activate_enchanteditem('Ethos')

                #updates the points, etc.
                if enchanteditem_checker_argument == '0':         #if user does NOT want to use their item
                    #update the player's points
                    points_tally('Ethos', 12) 

                    #print message to user
                    print('\n' + ' ' * 26 + f'You have spent {CBOLD}{CITALIC}{CYELLOW}12{CEND} ', end = '')
                    print(f'{CBOLD}{CYELLOW}Ethos points{CEND}!\n')  
                    
                    #break out of mini while loop
                    proceed_2 = False        
                else:                                           #if user wants to use their item 
                    if enchanteditem_checker_argument == '1':
                        if test_the_enchanteditemlimit() == 'True': #checks if user can use enchanted item
                            #saves the new points
                            sunwukong_newpoints = enchanted_item_activated(12, Id_enchanteditem)
                            
                            #update points 
                            points_tally('Ethos', sunwukong_newpoints)

                            #print message to user
                            print(' ' * 26 + f'You have spent ', end = '')
                            print(f'{CBOLD}{CITALIC}{CYELLOW}{sunwukong_newpoints} ', end = '')
                            print(f'{CBOLD}{CYELLOW}Ethos points{CEND}!')
                            
                            #break out of mini while loop
                            proceed_2 = False
                        else:
                            #print message to player that their chances are maxxed out
                            print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You exceeded uses for the{CEND}', end = '')
                            print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n')
                    elif enchanteditem_checker_argument == 'incompatible': #enchanted item = incompatible
                        #print out message that they cannot use thier enchanted item
                        print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You cannot use your{CEND}', end = '')
                        print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n') 
                   
            #break out of the big big while loop
            break
        elif sunwukong_choice_encounter == '2': #If their choice was 2 
            #first part of option 2
            while proceed_2:        #use while loop and sentinel to access profile and side quests
                #checks if they would like to use their enchanted item and if they CAN use it 
                enchanteditem_checker_argument = ask_activate_enchanteditem('Pathos')

                #updates the points, etc.
                if enchanteditem_checker_argument == '0':       #if user does not want to use their item 
                    #update the player's points
                    points_tally('Pathos', 10) 

                    #print message to user
                    print('\n' + ' ' * 26 + f'You have spent {CBOLD}{CITALIC}{CRED}10{CEND} ', end = '')
                    print(f'{CBOLD}{CRED}Pathos points{CEND}!')

                    #break out of mini-loop 
                    proceed_2 = False
                else:                                       #if user want to use their item
                    if enchanteditem_checker_argument == '1':
                        if test_the_enchanteditemlimit() == 'True': #checks if user can use enchanted item 
                            #saves the new points
                            sunwukong_newpoints = enchanted_item_activated(10, Id_enchanteditem)
                            
                            #update points 
                            points_tally('Pathos', sunwukong_newpoints)

                            #print message to user
                            print(' ' * 26 + f'You have spent ', end = '')
                            print(f'{CBOLD}{CITALIC}{CRED}{sunwukong_newpoints} ', end = '')
                            print(f'{CBOLD}{CRED}Pathos points{CEND}!')

                            #break out of mini-loop 
                            proceed_2 = False
                        else:
                            #print message to player that their chances are maxxed out
                            print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You exceeded uses for the{CEND}', end = '')
                            print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n')
                    elif enchanteditem_checker_argument == 'incompatible': #f the enchanted item is incompatible
                        #print out message that they cannot use thier enchanted item
                        print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You cannot use your{CEND}', end = '')
                        print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n') 

                        #in-between story portion for option 1
            
            print('\n') #add space
            sleep(1)    #add suspense

            #prints in-between story
            for oo in range(len(sunwukong_arc_storyline_list)): 
                #adjust indentation of strings
                temp = 26   #the constant that controls indentation
                temp_2 = 0  #the variable that controls indentation

                #customises the indentation
                if oo == 24 or oo == 26:
                    temp_2 = -16
                elif oo == 25:
                    temp_2 = 16

                x = (temp + (temp_2))    #the equation that adjusts the inentation of str's
                
                #prints the lines and adjusts the timing
                if oo == 24 or oo == 26:
                    print(' ' * x + sunwukong_arc_storyline_list[oo])
                elif oo == 25:
                    sleep(0.5)  #add suspense
                    print(' ' * x + sunwukong_arc_storyline_list[oo])
                    sleep(0.5)  #add suspense
                
            #the second part of option 2
            while proceed_2A:     #code is under a while loop for neatness and repeatability 
                #prints choice(s)
                print(sunwukong_arc_storyline_list[23])
                sleep(1)        #add timer for suspense

                #lets player 'choose' 
                sunwukong_choice_encounter_subcategory = input_system_ingame(1, 1)
                
                #updates the points, etc.
                if sunwukong_choice_encounter_subcategory == '1': 
                    #checks if they would like to use their enchanted item and if they CAN use it 
                    enchanteditem_checker_argument = ask_activate_enchanteditem('Ethos')

                    #asks user if they want to use their enchanted item
                    if enchanteditem_checker_argument == '0':         #if user does NOT want to use their item
                        #update the player's points
                        points_tally('Ethos', 12) 

                        #print message to user
                        print('\n' + ' ' * 26 + f'You have spent {CBOLD}{CITALIC}{CYELLOW}12{CEND} ', end = '')
                        print(f'{CBOLD}{CYELLOW}Ethos points{CEND}!')  

                        #break out of mini while loop
                        proceed_2A = False       
                    else:                                           #if user wants to use their item 
                        if enchanteditem_checker_argument == '1':
                            if test_the_enchanteditemlimit() == 'True': #checks if user can use enchanted item
                                #saves the new points
                                sunwukong_newpoints = enchanted_item_activated(12, Id_enchanteditem)

                                #update points 
                                points_tally('Ethos', sunwukong_newpoints)

                                #print message to user
                                print(' ' * 26 + f'You have spent ', end = '')
                                print(f'{CBOLD}{CITALIC}{CYELLOW}{sunwukong_newpoints} ', end = '')
                                print(f'{CBOLD}{CYELLOW}Ethos points{CEND}!')
                                
                                #break out of mini while loop
                                proceed_2A = False 
                            else:
                                #print message to player that their chances are maxxed out
                                print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You exceeded uses for the{CEND}', end = '')
                                print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n')
                        elif enchanteditem_checker_argument == 'incompatible': #enchanted item = incompatible
                            #print out message that they cannot use thier enchanted item
                            print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You cannot use your{CEND}', end = '')
                            print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n') 

            #add space for neatness
            print('\n')

            #break out of the big big while loop
            break      
        elif sunwukong_choice_encounter == '3': #If their choice was 3 
            #the first part of option 3
            while proceed_2:     #nested under a true loop for neatness 
                #checks if they would like to use their enchanted item and if they CAN use it 
                enchanteditem_checker_argument = ask_activate_enchanteditem('Logos')

                #updates the points, etc.
                if enchanteditem_checker_argument == '0':         #if user does NOT want to use their item
                    #update the player's points
                    points_tally('Logos', 7) 

                    #print message to user
                    print('\n' + ' ' * 26 + f'You have spent {CBOLD}{CITALIC}{CBLUE}7{CEND} ', end = '')
                    print(f'{CBOLD}{CBLUE}Logos points{CEND}!\n')  
                    
                    #break out of mini while loop
                    proceed_2 = False        
                else:                                           #if user wants to use their item 
                    if enchanteditem_checker_argument == '1':
                        if test_the_enchanteditemlimit() == 'True': #checks if user can use enchanted item
                            #saves the new points
                            sunwukong_newpoints = enchanted_item_activated(7, Id_enchanteditem)
                            
                            #update points 
                            points_tally('Logos', sunwukong_newpoints)

                            #print message to user
                            print(' ' * 26 + f'You have spent ', end = '')
                            print(f'{CBOLD}{CITALIC}{CBLUE}{sunwukong_newpoints} ', end = '')
                            print(f'{CBOLD}{CBLUE}Logos points{CEND}!\n')
                            
                            #break out of mini while loop
                            proceed_2 = False
                        else:
                            #print message to player that their chances are maxxed out
                            print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You exceeded uses for the{CEND}', end = '')
                            print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n')
                    elif enchanteditem_checker_argument == 'incompatible': #enchanted item = incompatible
                        #print out message that they cannot use thier enchanted item
                        print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You cannot use your{CEND}', end = '')
                        print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n') 

            sleep(1)    #add suspense

            #in-between story portion for option 3
            for uu in range(len(sunwukong_arc_storyline_list)): 
                #adjust indentation of strings
                temp = 26   #the constant that controls indentation
                temp_2 = 0  #the variable that controls indentation

                #customises the indentation
                if uu == 27 or uu == 29:
                    temp_2 = -16
                elif uu == 28:
                    temp_2 = 16

                x = (temp + (temp_2))    #the equation that adjusts the inentation of str's
                
                #prints the lines and adjusts the timing
                if uu == 27 or uu == 29:    #description
                    print(' ' * x + sunwukong_arc_storyline_list[uu])
                elif uu == 28:
                    sleep(0.5)  #add suspense
                    print(' ' * x + sunwukong_arc_storyline_list[uu])
                    sleep(0.5)  #add suspense

            #the second part of option 3
            while proceed_2A:     #code is under a while loop for neatness and repeatability 
                #prints choice(s)
                print(sunwukong_arc_storyline_list[23])
                sleep(1)        #add timer for suspense

                #lets player 'choose' (pentaly for picking the worng choice)
                sunwukong_choice_encounter_subcategory = input_system_ingame(1, 1)
                
                #updates the points, etc.
                if sunwukong_choice_encounter_subcategory == '1': 
                    #checks if they would like to use their enchanted item and if they CAN use it 
                    enchanteditem_checker_argument = ask_activate_enchanteditem('Ethos')

                    #asks user if they want to use their enchanted item
                    if enchanteditem_checker_argument == '0':         #if user does NOT want to use their item
                        #update the player's points
                        points_tally('Ethos', 12) 

                        #print message to user
                        print('\n' + ' ' * 26 + f'You have spent {CBOLD}{CITALIC}{CYELLOW}12{CEND} ', end = '')
                        print(f'{CBOLD}{CYELLOW}Ethos points{CEND}!')  

                        #break out of mini while loop
                        proceed_2A = False       
                    else:                                           #if user wants to use their item 
                        if enchanteditem_checker_argument == '1':
                            if test_the_enchanteditemlimit() == 'True': #checks if user can use enchanted item
                                #saves the new points
                                sunwukong_newpoints = enchanted_item_activated(12, Id_enchanteditem)

                                #update points 
                                points_tally('Ethos', sunwukong_newpoints)

                                #print message to user
                                print(' ' * 26 + f'You have spent ', end = '')
                                print(f'{CBOLD}{CITALIC}{CYELLOW}{sunwukong_newpoints} ', end = '')
                                print(f'{CBOLD}{CYELLOW}Ethos points{CEND}!')
                                
                                #break out of mini while loop
                                proceed_2A = False 
                            else:
                                #print message to player that their chances are maxxed out
                                print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You exceeded uses for the{CEND}', end = '')
                                print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n')
                        elif enchanteditem_checker_argument == 'incompatible': #enchanted item = incompatible
                            #print out message that they cannot use thier enchanted item
                            print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You cannot use your{CEND}', end = '')
                            print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n') 
  
            #break out of the big big while loop
            break

    sleep(1)    #add suspense w/ delay
    ending_embelishment('sunwukong')   #add embelishments!
    sleep(1)    #add suspense w/ delay

    #the 'ending' portion of the Sun Wukong arc
    while True:     #contents are under while loop for neatness 
        #add embelishments: newline for neatness and timer for suspense
        print('\n')
        sleep(1)

        #print the final portion of the Anansi Arc 
        for p in range(len(sunwukong_arc_storyline_list)): 
            #adjust indentation of strings
            temp = 26   #the constant that controls indentation
            temp_2 = 0  #the variable that controls indentation

            #adjusts indentation
            if p > 29 and p < 34:   #limits index to: 28-30 
                temp_2 = -16
            elif p == 35:
                temp_2 = -10

            x = (temp + (temp_2))   #the equation that controls indentation
            
            #modifies the time and prints the strings
            if p > 29 and p < 34:   #limits index to: 28-30 
                print(' ' * x + f'{sunwukong_arc_storyline_list[p]}')
            elif p == 35:           #limits index to: 31 
                sleep(0.5)
                print(' ' * x + f'{sunwukong_arc_storyline_list[p]}')
                sleep(0.5)
        
        #break out of while loop
        break

    ending_embelishment('sunwukong')   #add embelishments!
    sleep(1)    #add suspense w/ delay 

    #prints the summary and rewards of the Sun Wukong arc
    while True:     #contents are under while loop for neatness 
        #prints the rewards and summary
        for title, rewards in sunwukong_arc_ending_dictionary.items():     #display the body w/ format 
            print(' ' * 5 + title)     #name = key, goes thorugh the dictionary one by one
            sleep(0.5)  #delays printing of title
            for reward in rewards:    #description = values in list, goes thorugh each value in list
                print(' ' * 10 + reward)     #adds indent and description
                sleep(0.5)  #delays printing of each body of text

        #acts on the rewards: updates users attributes and inventory
        the_inventory(3)
        points_tally('Ethos', -(Players_attributes['Ethos'] * 3))     #increases player's points

        #break out of while loop
        break

    #output
    ending_embelishment('sunwukong')   #add embelishments!
    sleep(1)    #add suspense w/ delay 

def loki_arc():                                                 #the loki arc 
    """ 
    Contains all the action in the Loki Arc. Loki is a trickter god from Norse mythology.
    Args:
        none
    Returns:
        none
    """
    #initialise lists and dictionaries
    loki_arc_storyline_list = [     #the list with all the str's in the story 
        #round_1_intro (index: 0)
        f'A smile blooms on your face as you catch a glimpse of home atop a misty mountain top.\n',

        #round_1_pre_intro (index: 1-5)
        f'You swing your bag over your shoulder with a swing in your step. ',
        f'But before you can take a step forward a {CGREENBG}green mist{CEND} descends upon you.',
        f'An ancient, godly magic you are more than familiar with blurs your vision.',
        f'Another god seems to have caught you.', 
        f'{CBOLD}{CITALIC}{CWHITE2}What do you do?{CEND}\n',

        #round_1_pre_choices (index:6-8 )
        f'{CBOLD}1:{CEND} Bluff! [{CYELLOW}ETHOS {CITALIC}(-13){CEND}]',
        f'{CBOLD}2:{CEND} Brandish a sword! [{CRED}PATHOS {CITALIC}(-13){CEND}]',
        f'{CBOLD}3:{CEND} Bring out a sheild! [{CBLUE}LOGOS {CITALIC}(-13){CEND}]\n',

        #round_1_encounter_intro (index: 9-13)
        f'A cackle comes from behind you.',
        f'An {CGREENBG}elderly woman{CEND} dressed in black hobbles toward you.',
        f'Her staff— whenever it strikes the ground a certain power reverberates from it.',
        f'A ball of {CGREENBG}green energy{CEND} vibrates at the top of her staff and in a '
            f'second it flies off—towards you!',
        f'{CBOLD}{CITALIC}{CWHITE2}What do you do?{CEND}\n',

        #round_1_encounter_choices (index: 14-16)
        f'{CBOLD}1:{CEND} Dodge the blast! [{CYELLOW}ETHOS {CITALIC}(-20){CEND}]',
        f'{CBOLD}2:{CEND} Slash through the blast! [{CRED}PATHOS {CITALIC}(-20){CEND}]',
        f'{CBOLD}3:{CEND} Use your sheild! [{CBLUE}LOGOS {CITALIC}(-20){CEND}]\n',

        #encounter_EP (index: 17-19)
        f'You grit your teeth as you land a foot away from the scorched ground.',
        f'Annoyed and exasperated you shout at the cloaked grandma:\n',
        f'{CBOLD}1:{CEND} {CWHITE}"You don’t want to get in my way, not now!"{CEND} '
            f'[{CYELLOW}ETHOS {CITALIC}(-10){CEND}]\n',
        #encounter_PP (index: 20-23)
        f'Wind blows against your face and you ready your sword again.',
        f'A surge of power and irritation pulsates throughout your body.',
        f'You seethe at the grinning grandma:\n',
        f'{CBOLD}1:{CEND} {CWHITE}"What do you want from me?"{CEND} [{CRED}PATHOS {CITALIC}(-10){CEND}]\n',
        #encounter_LP (index: 24-27)
        f'You raise your head after tanking the burst. ',
        f'You catch a glimpse of grandma’s face—scarred and mischievous—and realization dawns upon you.',
        f'You snarl:\n',
        f'{CBOLD}1:{CEND} {CWHITE}"I know who you are, you fiend!"{CEND} '
            f'[{CBLUE}LOGOS {CITALIC}(-10){CEND}]\n',        
        
        #round_2_pre_intro (index: 28-34)
        f'The cloaked grandma flashes a wild, mischievous grin at you.',
        f'Its cloak melts away along with her features.',
        f'Her body reshapes, their black hair turns into a shiny strawberry blonde.',
        f'Their face shifts, it stays scarred but takes on youthful features.', 
        f'Beady black eyes taunt you, saying: ',
        f'{CGREEN}“Hello again little champion! Seeing as you have time to spare, '
            f'how about you lend me a hand?”{CEND}',
        f'{CBOLD}{CITALIC}{CWHITE2}What do you say?{CEND}\n',

        #round_2_pre_choices (index: 35-37)
        f'{CBOLD}1:{CEND} {CWHITE}"No. Don’t have time for you."{CEND} '
            f'[{CYELLOW}ETHOS {CITALIC}(-15){CEND}]',
        f'{CBOLD}2:{CEND} {CWHITE}"No thanks, bastard."{CEND} [{CRED}PATHOS {CITALIC}(-15){CEND}]',
        f'{CBOLD}3:{CEND} {CWHITE}"No I’m not getting roped into this again."{CEND} '
            f'[{CBLUE}LOGOS {CITALIC}(-15){CEND}]\n',

        #pre_EP (index: 38-43)
        f'{CGREENBG}Loki{CEND} rolls her eyes at you.',
        f'{CGREEN}“I wasn’t asking, little champion. For your insolence, I ought to kill you."',
        f'"Unfortunately you are the only one who can get what I want."',
        f'"I will be extra gracious and if you help me, I swear to send you right home."',
        f'"How about that?”{CEND}\n',
        f'{CBOLD}1:{CEND} {CWHITE}"Fine."{CEND}\n', #NO POINTS SPENT!
        #pre_PP (index: 44-49)
        f'A flicker of green burns your sword hand.',
        f'The sword clatters to the ground and you glare at the goddess responsible. ',
        f'{CGREEN}“What impertinence!”{CEND} {CGREENBG}Loki{CEND} chortles, ',
        f'{CGREEN}“While I would like to smite you on the spot as a show of my mercy..."',
        f'"I swear I will let you return home if you retrieve what I want!"{CEND}\n',
        f'{CBOLD}1:{CEND} {CWHITE}"Okay. But your oath will be fulfilled right as I get it, '
            f'{CGREENBG}Loki{CEND}{CWHITE}."{CEND}\n',    #NO POINTS SPENT
        #pre_LP (index: 50-54)
        f'A throaty laugh emanates from the goddess.',
        f'{CGREEN}“Your other adventures were much more… tedious than what I ask of you now. ',
        f'"As a show of mercy to your show of rudeness..."',
        f'"I swear to bring your sorry self to your home after you do what I want.”{CEND}\n',
        f'{CBOLD}1:{CEND} {CWHITE}"Alright. But I will no longer be involved in your schemes, '
            f'{CGREENBG}Loki{CEND}{CWHITE}."{CEND}\n',
    
        #round_2_encounter_intro (index: 55-65)
        f'The temptation to an uninterrupted arrival home was too much to refuse '
            f'{CGREENBG}Loki’s{CEND} very obvious schemes.',
        f'In the middle of an unknown sea you were tasked to search for '
            f'{CGREENBG}Loki’s{CEND} child Jörmungandr.',
        f'You are heal it with your ‘champion-powers’ and bring them to {CGREENBG}Loki{CEND}.',
        f'{CWHITE}“You bastard…”{CEND} you seethe.',
        f'{CWHITE}“I’m not so stupid as to be your aide in commencing ragnarok.”{CEND}',
        f'{CGREEN}“You are not as gullible as the other gods, I’ll give you that."',
        f'"Now what shall I do with you?”{CEND} {CGREENBG}Loki’s{CEND} flash green.',
        f'You are not brainless.',
        f'You have no chance against a god who just tried to trigger Ragnarok for fun."',
        f'But what you do have in spades is desperation.',  
        f'{CBOLD}{CITALIC}{CWHITE2}What do you do?{CEND}\n',

        #round_2_encounter_choices (index: 66-68)
        f'{CBOLD}1:{CEND} Pick up the sword and attack! [{CYELLOW}ETHOS {CITALIC}(-30){CEND}]',
        f'{CBOLD}2:{CEND} Kick sand into her eyes! [{CRED}PATHOS {CITALIC}(-30){CEND}]',
        f'{CBOLD}3:{CEND} Throw your sheild at her! [{CBLUE}LOGOS {CITALIC}(-30){CEND}]\n',

        #

        #encounter__EP (index: 69-75)
        f'With a roar you lift your sword over your head.',
        f'Naturally it is deflected and you are tossed to the side.',
        f'Landing on your two feet you check your pocket—your ticket home is still there.',
        f'With reason to hope you continue your admittedly reckless plan.',
        f'As you continue your game of attack and deflect with the '
            f'{CGREENBG}trickster goddess{CEND} you see an opening.',
        f'You reach into your backpack and bring out the gift from {CREDBG2}Anansi{CEND}!',
        f'A spindle of webs not even the strongest of gods could escape from without a fight.\n\n',
        #choice (index: 76) 
        f'{CBOLD}1:{CEND} Throw the webs at {CGREENBG}Loki{CEND}! [{CRED}PATHOS {CITALIC}(-25){CEND}]\n',
        #story (index: 77-88)
        f'Clearly underestimating your attack she knocks it to the side.',
        f'{CGREEN}“What was that some sort of yarn?”',
        f'“Is this your final act of desperation, little champion?”{CEND}',
        f'{CWHITE} “Underestimating me is your first mistake,”{CEND}',
        f'Clutching your wounded side, you look the deity in the eye.',
        f'{CWHITE}“Your second one is underestimating Anansi.”{CEND}',
        f'The webs come shooting out.',
        f'They wrap around the goddess until all but her face is wrapped by silver spindles.',
        f'For the first time the goddess is no longer having fun at your expense.',
        f'{CGREEN}“You think this will hold me down?"{CEND}',
        f'{CGREEN}"Once these flimsy webs are destroyed I’ll make you regret your disobedience–”{CEND}',
        f'{CWHITE}“That’s your third mistake.”{CEND} you let your smugness show.\n\n',
        #choice (index: 89)
        f'{CBOLD}1:{CEND} Reach into your bag and use your ticket home! '
            f'[{CBLUE}LOGOS {CITALIC}(-20){CEND}]\n',
        #story (index: 90-100)
        f'You throw a shiny green scale at the base of the webbed goddess.',
        f'{CWHITE}“Your oath was to send me home once I retrieved Jörmungandr and I have."',
        f'"A piece of him that is.”{CWHITE}',
        f'{CGREEN}“That was not our deal!”{CEND} she bellows.',
        f'{CWHITE}“But you never specified how much of your son I had to retrieve.”',
        f'“So send me home before the consequences of breaking your oath befall on you.”{CEND}',
        f'She sneers at you.',
        f'{CGREEN}“You may have caught me off guard, little champion.”{CEND}',
        f'A green fog surrounds you but this time you aren’t scared.',
        f'{CGREEN}“Hear me when I say that this will be your last time escaping me.”{CEND}',
        f'The vision of a {CGREENBG}webbed-up goddess{CEND}, cold seas, '
            f'and black sand fades as you feel the spell overtake your senses.\n\n',

        #encounter_PP (index: 101-123)
        f'You race to the columns of basalt nearby and start climbing like a madman.',
        f'{CGREEN}“You can try and run, little champion but it won’t work.”{CEND}',
        f'The looming voice of {CGREENBG}mischief{CEND} calls to you.',
        f'It won’t matter if she catches you now or later, you already have a plan.',
        f'You reach for your ear as you run.',
        f'Tucked behind your ear, like an engineer would their pencil, is a thin tooth-picked sized rod.',
        f'A mimic of {CYELLOW2}Ruyi Jingu Bang{CEND}.',
        f'A gift from a {CYELLOWBG2}trickster{CEND} to use on a {CGREENBG}trickster{CEND}.',
        f'You run to a basalt formation flat and sizable enough for your plan.',
        f'Right on time {CGREENBG}Loki{CEND} appears in a plume of green.',
        f'{CGREEN}“I’ve given you enough time, little champion."',
        f'"I thought you were fiercer than to run away!”{CEND}',
        f'Blasts of green energy surround you in every direction and you decide it is time.',
        f'You reach from behind your ear and summon your ace in the hole.',
        f'In your hands is a {CYELLOW2}staff{CEND}, taller than you by humming with untapped power.',
        f'Using its might, you knock back several of {CGREENBG}Loki’s{CEND} minions.',
        f'{CGREEN}“Oh, ooh! What a surprise!”{CEND}',
        f'A peal of laughter comes from {CGREENBG}Loki{CEND}.',
        f'{CGREEN}“But you are stupider than I thought."',
        f'"That tame imitation won’t hurt me.”{CEND}',
        f'You bite back a grin.',
        f'{CWHITE}“Again not thinking through, {CGREENBG}Loki{CEND}{CWHITE}."',
        f'"I thought you would learn from your experiences.”{CEND}\n\n',
        #choice (index: 124)
        f'{CBOLD}1:{CEND} Commence Transformation! [{CBLUE}LOGOS {CITALIC}(-25){CEND}]\n',
        #story (index: 125-133)
        f'In a moment of faith, you toss your staff into the sky!',
        f'{CGREEN}“Hah, an even greater show of idiocy! You are no '
            f'{CYELLOWBG2}Sun Wukong—{CEND}{CGREEN}”{CEND}',
        f'A boom echoes through the destroyed basalt columns and wind rushes to you and '
            f'{CGREENBG}Loki{CEND}.',
        f'When the dust settles what beholds you is an enormous snake.',
        f'Brown and black scales twist and turn through the basalt formations effectively '
            f'blocking any and all exits.',
        f'Two beady eyes larger than you stare down {CGREENBG}Loki{CEND}.',
        f'{CWHITE}“The staff does more than you think,”',
        f'“Vipers aren’t a good memory, no?”{CEND}',
        f'{CYELLOWBG2}Sun Wukong’s{CEND} gift was a staff that could aid you in casting illusions.\n\n',
        #choice (index: 134)
        f'{CBOLD}1:{CEND} Use your staff/snake to hold down the goddess! '
            f'[{CYELLOW}ETHOS {CITALIC}(-20){CEND}]\n',
        #story (index: 135-153)
        f'Using the second where {CGREENBG}Loki’s{CEND} attention slipped you command the '
            f'staff/snake to wrap around them.',
        f'With {CGREENBG}Loki{CEND} restrained and stunned you enact the next part of your plan.',
        f'With a raise of your hand you have the snake’s mouth atop {CGREENBG}Loki’s{CEND} head.',
        f'It unhinges its jaws and its white fangs glisten with venom.',
        f'The viscous liquid coats its mouth and fangs.',
        f'An exaggerated version of a snake but it works how you intend.', 
        f'Rage but mostly fear is directed at you from {CGREENBG}Loki{CEND}.',
        f'{CGREEN}“Have your snake unhand me this instance or I’ll smite you where I stand!”{CEND}',
        f'Loki gasps, the staff/snake constricting tighter around her midsection.',
        f'{CGREEN}“I command you–”{CEND}',
        f'{CWHITE}“You don’t get to ‘command’ me here, little god.”{CEND}',
        f'From behind the illusion sweat beads down your face.',
        f'You need to end this soon.',
        f'{CWHITE}“Send me home or I’ll have the snake venom scar your face again.”{CEND}',
        f'{CGREENBG}Loki{CEND} doesn’t reply.',
        f'You have the snake dip its lead closer to the goddess’ face.',
        f'{CWHITE}“Send me home.”{CEND} you say with more force.',
        f'Anger and promise seeps into your voice and that seems to convenience Loki that you will '
            f'no longer hesitate.',
        f'Green fog surrounds you and the last glimpse you get before the spell '
            f'overtakes your senses are {CGREENBG}green eyes{CEND} promising vengeance.\n\n',        

        #encounter_LP (index: 154-168)
        f'{CGREENBG}Loki{CEND} deflects the shield, it embeds itself on a nearby stone pillar by the sea.',
        f'{CGREEN}“Is that the best you can come up with?”{CEND}',
        f'You pull out your sword and {CGREENBG}Loki{CEND} summons monsters from her green mist.',
        f'You strike down countless numbers of trolls and dragurs as you make your way to a cave.',
        f'Luring all of your enemies in like a reel.',
        f'You have a plan and it is absurd.',
        f'As you enter the mouth of the cave, its cool and damp air fill your lungs.',
        f'In a moment of hastiness, you jump back from your opponents and raise your sword.',
        f'A bright blaze illuminates the cave as your sword glows bright blue flames.',
        f'{CGREEN}“What a curious machination, little champion.”{CEND}',
        f'Loki hums from behind her horde of minions,',
        f'{CGREEN}“But you are just a mortal. Sooner or later you will succumb to your weaknesses!”{CEND}',
        f'{CGREENBG}Loki{CEND} smiles madly as she summons another wave of monsters. ',
        f'It is true, you are getting tired.',
        f'Your breathing is awry and your vision starts to haze.\n\n',
        #choice (index: 169)
        f'{CBOLD}1:{CEND} Seal the cave! [{CYELLOW}ETHOS {CITALIC}(-25){CEND}]\n',
        #story (index: 170-181)
        f'Seeing how everything falls into place.',
        f'You waste no time and barrage your way through the ocean of enemies.',
        f'With a roar you turn the sword and strike the rocks above the entrance of the cave.',
        f'Dust and rocks billow through the whole save and for a moment it seems like everyone '
            f'stops to see what has just happened.',
        f'{CGREEN}“You brainless ingrate!”{CEND} {CGREENBG}Loki{CEND} sneers at you.',
        f'{CGREEN}“Selling the cave will be your ruin!"{CEND}',
        f'{CGREEN}"You have no air to breathe and–”',
        f'“You’re stuck with me.”{CEND}',
        f'You wipe the blood from the corner of your mouth,',
        f'{CWHITE}“It won’t matter that the cave is closed."',
        f'"You will send me home!”{CEND}',
        f'You grab your backpack, which has stayed with you through your maneuvering efforts, '
            f'and open it to reveal—\n\n',
        #choice (index: 182)
        f'{CBOLD}1:{CEND} Unleash the mosquitoes! [{CRED}PATHOS {CITALIC}(-20){CEND}]\n',
        #story (index: 183-197)
        f'You hold your secret weapon up high–a jar with one single mosquito.',
        f'The sound of glass breaking prompts {CGREENBG}Loki{CEND},',
        f'{CGREEN}“Is that it?”',
        f'“How can a gift from the hero twins be so underwhelming?”{CEND}',
        f'{CGREENBG}Loki{CEND} flicks her finger and the horde continues to attack you.',
        f'At that moment you laugh, as you fight you keep your eyes on the singular mosquito '
            f'that becomes mosquitoes.',
        f'Screams echo through the cave as your horde of enchanted mosquitoes suck the life '
            f'out of the monsters.',
        f'Once the horde is reduced to rotting carcases you raise your hand and point to '
            f'{CGREENBG}Loki{CEND}.',
        f'{CWHITE}“You underestimated me and I thank you for that!”{CEND}',
        f'The horde swarms {CGREENBG}Loki{CEND} and she tries to blast all of them, however when '
            f'one dies more than a dozen quickly replace it.',
        f'Loki shrieks as moe of the mosquitoes latch onto {CGREENBG}Loki’{CEND} godly skin and '
            f'absorb the immortality out of the goddess.',
        f'{CWHITE}“But what I cannot forgive is your disrespect to the hero twins and their magic—”{CEND}',
        f'You approach her writhing body,',
        f'{CWHITE}“So before your immortality is drained, send me home and I’ll call the horde off.”{CEND}',
        f'You catch a glimpse of {CGREENBG}green eyes{CEND} promising death before the '
            f'{CGREENBG}green fog{CEND} envelopes you.\n\n',

        #loki_ending (index: 198-204)
        f'Your previous bravado fades and you fall to the ground.',
        f'That was a tough fight, you think to yourself.',
        f'{CGREENBG}Loki{CEND} still played you.',
        f'The green mist threw you down at the outskirts of your hometown.',
        f'Wounded and exhausted you begin to accept the sweet release of sleep.',
        f'But before you can begin to close your eyes–',
        f'A hand appears in front of you.\n'
        ]
    loki_arc_ending_dictionary = {  #the dictionary (and list) that  has the ending descrition 
        f'{CITALIC}You gained:{CEND}' : [
        f'{CSELECTED}{CITALIC}Being able to go home.{CEND}\n'
        ]
        }
    
    #initiate variables 
    global True_ending_confirmation
    proceed_r1_1 = True     #sentinel for the round 1 'pre' poriton's option's
    proceed_r1_2 = True     #sentinel for the round 1 'encounter' portion's  
                            # every 1st while loop
    proceed_r1A_1 = True    #sentinel for the round 1 'encounter' portion's  
                            # every nested encounter OR 2nd while loop
    proceed_r2_1 = True     #sentinel for the round 2 first portion of 'pre'
    proceed_r2_11 = True    #sentinel for the round 2 second portion of 'pre' 
    proceed_r2_2 = True     #sentinel for round 2 'encounter' - first part 
    proceed_r2A_2 = True    #sentinel for round 2 'encounter - second part
    proceed_r2A_3 = True    #sentinelf or round 2 'encounter' - third part
    loki_newpoints = 0      #the new value being subtracted from the player's
                            #attributes after altered by their enchanted item

    #input

    #process
    #prints title card of the arc
    while True:     #nested under a true loop to keep it clean 
        #title of page
        title_profile = f'{CBOLD}{CGREEN}𓆚{CEND}  {CBOLD}{CSELECTED}THE MALEVOLENT TRICKSTER ARC{CEND} {CGREEN}𓆚{CEND}\n' 
        
        #put empty space on the same line
        print(f' ' * 46, end = '')     

        #code that mimics a type-writer: from stackoverflow!
        for l in title_profile:     
            sys.stdout.write(l)
            sys.stdout.flush()
            time.sleep(0.1)

        print('\n') #add space

        #break out of loop
        break

    #prints intro to the arc
    while True:     #contents are under while loop for neatness 
        #prints the line
        for i in range(len(loki_arc_storyline_list)):
            #modifies time it will print and prints the line
            if i == 0:            #limits to the question
                #the intro to the loki arc
                sleep(1)        #add delay for suspense
                print(' ' * 10 + f'{loki_arc_storyline_list[i]}')
                sleep(1)        #add delay for suspense

                #the start of round 1
                print(CBOLD + CSELECTED + CGREEN2 + ' ' * 50 + 'ROUND 1 ' + CEND)
                sleep(1)        #add delay for suspense
            
        break     #break out of loop

    #round 1 | prints intro to round 1 of the Loki arc
    while True:     #contents are under while loop for neatness 
        for ii in range(len(loki_arc_storyline_list)):
            #adjust indentation of strings
            temp = 26   #the constant that controls indentation
            temp_2 = 0  #the variable that controls indentation
            
            if ii > 0 and ii < 5:       #limits index to 0-3
                temp_2 = -16
            elif ii == 5:                #limits index to 4 (the question)
                temp_2 = 26

            x = (temp + (temp_2))   #the equation that controls indentation
            
            #modifies time it will print and prints the lines
            if ii == 5:                 #limits to the question
                sleep(1)        #add delay for suspense
                print(' ' * x + f'{loki_arc_storyline_list[ii]}')
                sleep(1)        #add delay for suspense
            elif ii > 0 and ii < 5:     #limits to description 
                print(' ' * x + f'{loki_arc_storyline_list[ii]}')
        
        #break out of loop
        break     

    #round 1 | 'pre' portion of the Loki arc
    while True:     #contents are under while loop for neatness 
        #prints the pre choices
        for jj in range(len(loki_arc_storyline_list)): 
            #adjust indentation of strings
            temp = 26   #the constant that controls indentation
            temp_2 = 0  #the variable that controls indentation

            #customises the indentation
            temp_2 = -26

            x = (temp + (temp_2))    #the equation that adjusts the inentation of str's
            
            #prints the lines w/ timer
            if jj > 5 and jj < 9:     #limits index to 3-6
                print(' ' * x + loki_arc_storyline_list[jj])
                sleep(0.5)          #add timer for suspense
        
        #lets user make their choice
        loki_choice_pre = input_system_ingame(3, 1)
        
        #acts on what the user chose
        if loki_choice_pre == '1':    #user chooses option 1 
            #acts on the user's choice
            while proceed_r1_1: 
                #checks if they would like to use their enchanted item and if they CAN use it 
                enchanteditem_checker_argument = ask_activate_enchanteditem('Ethos')

                #updates the points, etc.
                if enchanteditem_checker_argument == '0':       #if user does not want to use their item
                    #update the player's points
                    points_tally('Ethos', 13) 

                    #print message to user
                    print('\n' + ' ' * 26 + f'You have spent {CBOLD}{CITALIC}{CYELLOW}13{CEND} ', end = '')
                    print(f'{CBOLD}{CYELLOW}Ethos points{CEND}!\n')

                    #break out of mini-loop
                    proceed_r1_1 = False
                else:       #if the user wants to use their enchanted item
                    if enchanteditem_checker_argument == '1':     
                        if test_the_enchanteditemlimit() == 'True': #checks if user can use enchanted item
                            #saves the new points
                            loki_newpoints = enchanted_item_activated(13, Id_enchanteditem)
                            
                            #update points 
                            points_tally('Ethos', loki_newpoints)
                            
                            #print message to user
                            print(' ' * 26 + f'You have spent ', end = '')
                            print(f'{CBOLD}{CITALIC}{CYELLOW}{loki_newpoints} ', end = '')
                            print(f'{CBOLD}{CYELLOW}Ethos points{CEND}!\n')

                            #break out of mini-loop
                            proceed_r1_1 = False
                        else:
                            #print message to player that their chances are maxxed out
                            print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You exceeded uses for the{CEND}', end = '')
                            print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n')
                    elif enchanteditem_checker_argument == 'incompatible': #enchanted item = incompatible
                        #print out message that they cannot use thier enchanted item
                        print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You cannot use your{CEND}', end = '')
                        print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n') 
            
            #break out of big while loop
            break
        elif loki_choice_pre == '2':  #user chooses option 2 
            #acts on the user's choice
            while proceed_r1_1: 
                #checks if they would like to use their enchanted item and if they CAN use it 
                enchanteditem_checker_argument = ask_activate_enchanteditem('Pathos')
                
                #updates the points, etc.
                if enchanteditem_checker_argument == '0':       #if user does not want to use their item
                    #update the player's points
                    points_tally('Pathos', 13) 

                    #print message to user
                    print('\n' + ' ' * 26 + f'You have spent {CBOLD}{CITALIC}{CRED}13{CEND} ', end = '')
                    print(f'{CBOLD}{CRED}Pathos points{CEND}!\n')

                    #break out of mini-loop        
                    proceed_r1_1 = False
                else:                                       #if user want to use their item
                    if enchanteditem_checker_argument == '1': 
                        if test_the_enchanteditemlimit() == 'True': #checks if user can use enchanted item 
                            #saves the new points
                            loki_newpoints = enchanted_item_activated(13, Id_enchanteditem)
                            
                            #update points 
                            points_tally('Pathos', loki_newpoints)

                            #print message to user
                            print(' ' * 26 + f'You have spent ', end = '')
                            print(f'{CBOLD}{CITALIC}{CRED}{loki_newpoints} ', end = '')
                            print(f'{CBOLD}{CRED}Pathos points{CEND}!\n')

                            #break out of loop 
                            proceed_r1_1 = False
                        else:
                            #print message to player that their chances are maxxed out
                            print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You exceeded uses for the{CEND}', end = '')
                            print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n')            
                    elif enchanteditem_checker_argument == 'incompatible': #enchanted item = incompatible
                        #print out message that they cannot use thier enchanted item
                        print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You cannot use your{CEND}', end = '')
                        print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n') 
        
            #break out of big while loop
            break
        elif loki_choice_pre == '3':  #user chooses option 3 
            #acts on the user's choice
            while proceed_r1_1: 
                #checks if they would like to use their enchanted item and if they CAN use it 
                enchanteditem_checker_argument = ask_activate_enchanteditem('Logos')

                #updates the points, etc.
                if enchanteditem_checker_argument == '0':       #if user does not want to use their item
                    #update the player's points
                    points_tally('Logos', 13) 

                    #print message to user
                    print('\n' + ' ' * 26 + f'You have spent {CBOLD}{CITALIC}{CBLUE}13{CEND} ', end = '')
                    print(f'{CBOLD}{CBLUE}Logos points{CEND}!\n')

                    #break out of mini-loop        
                    proceed_r1_1 = False
                else:                                       #if user wants to use their item 
                    if enchanteditem_checker_argument == '1':
                        if test_the_enchanteditemlimit() == 'True': #checks if user can use enchanted item 
                            #saves the new points
                            loki_newpoints = enchanted_item_activated(13, Id_enchanteditem)
                            
                            #update points 
                            points_tally('Logos', loki_newpoints)
                            
                            #print message to user
                            print(' ' * 26 + f'You have spent ', end = '')
                            print(f'{CBOLD}{CITALIC}{CBLUE}{loki_newpoints} ', end = '')
                            print(f'{CBOLD}{CBLUE}Logos points{CEND}!\n')

                            #break out of mini-loop 
                            proceed_r1_1 = False
                        else: 
                            #print message to player that their chances are maxxed out
                            print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You exceeded uses for the{CEND}', end = '')
                            print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n')            
                    elif enchanteditem_checker_argument == 'incompatible': #enchanted item = incompatible
                        #print out message that they cannot use thier enchanted item
                        print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You cannot use your{CEND}', end = '')
                        print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n') 
            
            #break out of big while loop
            break

    ending_embelishment('loki')
    sleep(1)

    #round 1 | prints intro to 'encounter'
    while True:     #contents are under while loop for neatness 
        #prints intro to the 1st encounter
        for nn in range(len(loki_arc_storyline_list)):
            #adjust indentation of strings
            temp = 26   #the constant that controls indentation
            temp_2 = 0  #the variable that controls indentation

            #customises the indentation 
            if nn > 8 and nn < 13: #the quotes 
                temp_2 = -16
            elif nn == 13:  #the question
                temp_2 = 26

            x = (temp + (temp_2))    #the equation that adjusts the inentation of str's
            
            #prints the lines w/ timer
            if nn > 8 and nn < 13: #prints the description
                print(' ' * x + loki_arc_storyline_list[nn])
            elif nn == 13:  #prints the quotes
                sleep(0.5)        #add delay for suspense
                print(' ' * x + f'{loki_arc_storyline_list[nn]}')
                sleep(0.5)        #add delay for suspense

        #break out of the loop
        break

    #round 1 | the 'encounter' portion of the Loki arc
    while True:     #contents are under while loop for neatness 
        #prints the 'encounter' questions
        for mm in range(len(loki_arc_storyline_list)): 
            #adjust indentation of strings
            temp = 26   #the constant that controls indentation
            temp_2 = 0  #the variable that controls indentation

            #customises the indentation
            if mm > 13 or mm < 17: 
                temp_2 = -26

            x = (temp + (temp_2))    #the equation that adjusts the inentation of str's
            
            #prints the lines w/ timer
            if mm > 13 and mm < 17:
                print(' ' * x + f'{loki_arc_storyline_list[mm]}')
                sleep(0.5)        #add delay for suspense
        
        #lets the user make their choice
        loki_choice_encounter = input_system_ingame(3, 1)

        # acts on the player's choice
        if loki_choice_encounter == '1': #If their choice was 1 
            #the first part of option 1
            while proceed_r1_2:     #nested under a true loop for neatness 
                #checks if they would like to use their enchanted item and if they CAN use it 
                enchanteditem_checker_argument = ask_activate_enchanteditem('Ethos')

                #updates the points, etc.
                if enchanteditem_checker_argument == '0':         #if user does NOT want to use their item
                    #update the player's points
                    points_tally('Ethos', 20) 

                    #print message to user
                    print('\n' + ' ' * 26 + f'You have spent {CBOLD}{CITALIC}{CYELLOW}20{CEND} ', end = '')
                    print(f'{CBOLD}{CYELLOW}Ethos points{CEND}!\n')  
                    
                    #break out of mini while loop
                    proceed_r1_2 = False        
                else:                                           #if user wants to use their item 
                    if enchanteditem_checker_argument == '1':
                        if test_the_enchanteditemlimit() == 'True': #checks if user can use enchanted item
                            #saves the new points
                            loki_newpoints = enchanted_item_activated(20, Id_enchanteditem)
                            
                            #update points 
                            points_tally('Ethos', loki_newpoints)

                            #print message to user
                            print(' ' * 26 + f'You have spent ', end = '')
                            print(f'{CBOLD}{CITALIC}{CYELLOW}{loki_newpoints} ', end = '')
                            print(f'{CBOLD}{CYELLOW}Ethos points{CEND}!\n')
                            
                            #break out of mini while loop
                            proceed_r1_2 = False
                        else:
                            #print message to player that their chances are maxxed out
                            print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You exceeded uses for the{CEND}', end = '')
                            print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n')
                    elif enchanteditem_checker_argument == 'incompatible': #enchanted item = incompatible
                        #print out message that they cannot use thier enchanted item
                        print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You cannot use your{CEND}', end = '')
                        print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n') 
            
            sleep(1)    #add suspense

            #in-between story portion for option 1
            for uu in range(len(loki_arc_storyline_list)): 
                #adjust indentation of strings
                temp = 26   #the constant that controls indentation
                temp_2 = 0  #the variable that controls indentation

                #customises the indentation
                temp_2 = -16

                x = (temp + (temp_2))    #the equation that adjusts the inentation of str's
                
                #prints the lines and adjusts the timing
                if uu == 17 or uu == 18:  
                    print(' ' * x + loki_arc_storyline_list[uu])
                    sleep(0.5)  #add suspense

            #the second part of option 1
            while proceed_r1A_1:     #code is under a while loop for neatness and repeatability 
                #prints choice(s)
                print(loki_arc_storyline_list[19])
                sleep(1)        #add timer for suspense

                #lets player 'choose' (this is pentaly for picking the worng choice)
                loki_choice_encounter_subcategory = input_system_ingame(1, 1)
                
                #updates the points, etc.
                if loki_choice_encounter_subcategory == '1': 
                    #checks if they would like to use their enchanted item and if they CAN use it 
                    enchanteditem_checker_argument = ask_activate_enchanteditem('Ethos')

                    if enchanteditem_checker_argument == '0':         #if user does NOT want to use their item
                        #update the player's points
                        points_tally('Ethos', 10) 

                        #print message to user
                        print('\n' + ' ' * 26 + f'You have spent {CBOLD}{CITALIC}{CYELLOW}10{CEND} ', end = '')
                        print(f'{CBOLD}{CYELLOW}Ethos points{CEND}!\n')  

                        #break out of mini while loop
                        proceed_r1A_1 = False       
                    else:                                           #if user wants to use their item 
                        if enchanteditem_checker_argument == '1': 
                            if test_the_enchanteditemlimit() == 'True': #checks if user can use enchanted item
                                #saves the new points
                                loki_newpoints = enchanted_item_activated(10, Id_enchanteditem)

                                #update points 
                                points_tally('Ethos', loki_newpoints)

                                #print message to user
                                print(' ' * 26 + f'You have spent ', end = '')
                                print(f'{CBOLD}{CITALIC}{CYELLOW}{loki_newpoints} ', end = '')
                                print(f'{CBOLD}{CYELLOW}Ethos points{CEND}!\n')
                                
                                #break out of mini while loop
                                proceed_r1A_1 = False 
                            else:
                                #print message to player that their chances are maxxed out
                                print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You exceeded uses for the{CEND}', end = '')
                                print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n')
                        elif enchanteditem_checker_argument == 'incompatible': #enchanted item = incompatible
                            #print out message that they cannot use thier enchanted item
                            print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You cannot use your{CEND}', end = '')
                            print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n')  
            #break out of the big big while loop
            break
        elif loki_choice_encounter == '2': #If their choice was 2 
            #first part of option 2
            while proceed_r1_2:     #nested under a true loop for neatness 
                #checks if they would like to use their enchanted item and if they CAN use it 
                enchanteditem_checker_argument = ask_activate_enchanteditem('Pathos')

                #updates the points, etc.
                if enchanteditem_checker_argument == '0':         #if user does NOT want to use their item
                    #update the player's points
                    points_tally('Pathos', 20) 

                    #print message to user
                    print('\n' + ' ' * 26 + f'You have spent {CBOLD}{CITALIC}{CRED}20{CEND} ', end = '')
                    print(f'{CBOLD}{CRED}Pathos points{CEND}!\n')  
                    
                    #break out of mini while loop
                    proceed_r1_2 = False        
                else:                                           #if user wants to use their item 
                    if enchanteditem_checker_argument == '1':
                        if test_the_enchanteditemlimit() == 'True': #checks if user can use enchanted item
                            #saves the new points
                            loki_newpoints = enchanted_item_activated(20, Id_enchanteditem)
                            
                            #update points 
                            points_tally('Pathos', loki_newpoints)

                            #print message to user
                            print(' ' * 26 + f'You have spent ', end = '')
                            print(f'{CBOLD}{CITALIC}{CRED}{loki_newpoints} ', end = '')
                            print(f'{CBOLD}{CRED}Pathos points{CEND}!\n')
                            
                            #break out of mini while loop
                            proceed_r1_2 = False
                        else:
                            #print message to player that their chances are maxxed out
                            print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You exceeded uses for the{CEND}', end = '')
                            print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n')
                    elif enchanteditem_checker_argument == 'incompatible': #f the enchanted item is incompatible
                        #print out message that they cannot use thier enchanted item
                        print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You cannot use your{CEND}', end = '')
                        print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n') 
            
            sleep(1)    #add suspense

            #in-between story portion for option 2
            for uu in range(len(loki_arc_storyline_list)): 
                #adjust indentation of strings
                temp = 26   #the constant that controls indentation
                temp_2 = 0  #the variable that controls indentation

                #customises the indentation
                temp_2 = -16

                x = (temp + (temp_2))    #the equation that adjusts the inentation of str's
                
                #prints the lines and adjusts the timing
                if uu == 21 or uu == 22:  
                    print(' ' * x + loki_arc_storyline_list[uu])
                    sleep(0.5)  #add suspense

            #the second part of option 2
            while proceed_r1A_1:     #code is under a while loop for neatness and repeatability 
                #prints choice(s)
                print(loki_arc_storyline_list[23])
                sleep(1)        #add timer for suspense

                #lets player 'choose' (this is pentaly for picking the worng choice)
                loki_choice_encounter_subcategory = input_system_ingame(1, 1)
                
                #updates the points, etc.
                if loki_choice_encounter_subcategory == '1': 
                    #checks if they would like to use their enchanted item and if they CAN use it 
                    enchanteditem_checker_argument = ask_activate_enchanteditem('Pathos')

                    if enchanteditem_checker_argument == '0':         #if user does NOT want to use their item
                        #update the player's points
                        points_tally('Pathos', 10) 

                        #print message to user
                        print('\n' + ' ' * 26 + f'You have spent {CBOLD}{CITALIC}{CRED}10{CEND} ', end = '')
                        print(f'{CBOLD}{CRED}Pathos points{CEND}!\n')  

                        #break out of mini while loop
                        proceed_r1A_1 = False       
                    else:                                           #if user wants to use their item 
                        if enchanteditem_checker_argument == '1':
                            if test_the_enchanteditemlimit() == 'True': #checks if user can use enchanted item
                                #saves the new points
                                loki_newpoints = enchanted_item_activated(10, Id_enchanteditem)

                                #update points 
                                points_tally('Pathos', loki_newpoints)

                                #print message to user
                                print(' ' * 26 + f'You have spent ', end = '')
                                print(f'{CBOLD}{CITALIC}{CRED}{loki_newpoints} ', end = '')
                                print(f'{CBOLD}{CRED}Pathos points{CEND}!\n')
                                
                                #break out of mini while loop
                                proceed_r1A_1 = False 
                            else:
                                #print message to player that their chances are maxxed out
                                print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You exceeded uses for the{CEND}', end = '')
                                print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n')
                        elif enchanteditem_checker_argument == 'incompatible': #enchanted item = incompatible
                            #print out message that they cannot use thier enchanted item
                            print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You cannot use your{CEND}', end = '')
                            print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n') 
  
            #break out of the big big while loop
            break     
        elif loki_choice_encounter == '3': #If their choice was 3 
            #the first part of option 3
            while proceed_r1_2:     #nested under a true loop for neatness 
                #checks if they would like to use their enchanted item and if they CAN use it 
                enchanteditem_checker_argument = ask_activate_enchanteditem('Logos')

                #updates the points, etc.
                if enchanteditem_checker_argument == '0':         #if user does NOT want to use their item
                    #update the player's points
                    points_tally('Logos', 10) 

                    #print message to user
                    print('\n' + ' ' * 26 + f'You have spent {CBOLD}{CITALIC}{CBLUE}10{CEND} ', end = '')
                    print(f'{CBOLD}{CBLUE}Logos points{CEND}!\n')  
                    
                    #break out of mini while loop
                    proceed_r1_2 = False        
                else:                                           #if user wants to use their item 
                    if enchanteditem_checker_argument == '1':
                        if test_the_enchanteditemlimit() == 'True': #checks if user can use enchanted item
                            #saves the new points
                            loki_newpoints = enchanted_item_activated(10, Id_enchanteditem)
                            
                            #update points 
                            points_tally('Logos', loki_newpoints)

                            #print message to user
                            print(' ' * 26 + f'You have spent ', end = '')
                            print(f'{CBOLD}{CITALIC}{CBLUE}{loki_newpoints} ', end = '')
                            print(f'{CBOLD}{CBLUE}Logos points{CEND}!\n')
                            
                            #break out of mini while loop
                            proceed_r1_2 = False
                        else:
                            #print message to player that their chances are maxxed out
                            print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You exceeded uses for the{CEND}', end = '')
                            print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n')
                    elif enchanteditem_checker_argument == 'incompatible': #enchanted item = incompatible
                        #print out message that they cannot use thier enchanted item
                        print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You cannot use your{CEND}', end = '')
                        print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n') 

            sleep(1)    #add suspense

            #in-between story portion for option 3
            for uu in range(len(loki_arc_storyline_list)): 
                #adjust indentation of strings
                temp = 26   #the constant that controls indentation
                temp_2 = 0  #the variable that controls indentation

                #customises the indentation
                if uu > 23 and uu < 27:
                    temp_2 = -16

                x = (temp + (temp_2))    #the equation that adjusts the inentation of str's
                
                #prints the lines and adjusts the timing
                if uu > 23 and uu < 27:    #description
                    print(' ' * x + loki_arc_storyline_list[uu])

            #the second part of option 3
            while proceed_r1A_1:     #code is under a while loop for neatness and repeatability 
                #prints choice(s)
                print(loki_arc_storyline_list[27])
                sleep(1)        #add timer for suspense

                #lets player 'choose' (pentaly for picking the worng choice)
                loki_choice_encounter_subcategory = input_system_ingame(1, 1)
                
                #updates the points, etc.
                if loki_choice_encounter_subcategory == '1': 
                    #checks if they would like to use their enchanted item and if they CAN use it 
                    enchanteditem_checker_argument = ask_activate_enchanteditem('Logos')

                    #asks user if they want to use their enchanted item
                    if enchanteditem_checker_argument == '0':         #if user does NOT want to use their item
                        #update the player's points
                        points_tally('Logos', 10) 

                        #print message to user
                        print('\n' + ' ' * 26 + f'You have spent {CBOLD}{CITALIC}{CBLUE}10{CEND} ', end = '')
                        print(f'{CBOLD}{CBLUE}Logos points{CEND}!')  

                        #break out of mini while loop
                        proceed_r1A_1 = False       
                    else:                                           #if user wants to use their item 
                        if enchanteditem_checker_argument == '1':
                            if test_the_enchanteditemlimit() == 'True': #checks if user can use enchanted item
                                #saves the new points
                                loki_newpoints = enchanted_item_activated(10, Id_enchanteditem)

                                #update points 
                                points_tally('Logos', loki_newpoints)

                                #print message to user
                                print(' ' * 26 + f'You have spent ', end = '')
                                print(f'{CBOLD}{CITALIC}{CBLUE}{loki_newpoints} ', end = '')
                                print(f'{CBOLD}{CBLUE}Logos points{CEND}!')
                                
                                #break out of mini while loop
                                proceed_r1A_1 = False 
                            else:
                                #print message to player that their chances are maxxed out
                                print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You exceeded uses for the{CEND}', end = '')
                                print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n')
                        elif enchanteditem_checker_argument == 'incompatible': #enchanted item = incompatible
                            #print out message that they cannot use thier enchanted item
                            print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You cannot use your{CEND}', end = '')
                            print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n') 
  
            #break out of the big big while loop
            break

    ending_embelishment('loki')
    sleep(1)

    #round 2 | prints intro to 'pre' round 2 of Loki arc
    while True:     #contents are under while loop for neatness 
        #intro to the round
        print('\n' + CBOLD + CSELECTED + CGREEN2 + ' ' * 50 + 'ROUND 2 ' + CEND)
        sleep(1)        #add delay for suspense
        
        #the story-portion
        for jj in range(len(loki_arc_storyline_list)): 
            #adjust indentation of strings
            temp = 26   #the constant that controls indentation
            temp_2 = 0  #the variable that controls indentation
            
            #customises the indentation
            if jj > 27 and jj < 32:
                temp_2 = -16
            elif jj == 33:
                temp_2 = 16
            elif jj == 34:
                temp_2 = 26

            x = (temp + (temp_2))   #the equation that controls indentation
            
            #modifies time it will print and prints the lines
            if jj > 27 and jj < 32:     #prints the description
                print(' ' * x + loki_arc_storyline_list[jj])
            elif jj == 33 or jj == 34:  #prints the dialouge and question
                sleep(0.5)
                print(' ' * x + loki_arc_storyline_list[jj])
                sleep(0.5)
            
        #break out of loop
        break     

    #round 2 | 'pre' portion of the Loki Arc
    while True:     #contents are under while loop for neatness 
        #prints the pre choices
        for e in range(len(loki_arc_storyline_list)): 
            #adjust indentation of strings
            temp = 26   #the constant that controls indentation
            temp_2 = 0  #the variable that controls indentation

            #customises the indentation
            temp_2 = -26

            x = (temp + (temp_2))    #the equation that adjusts the inentation of str's
            
            #prints the lines w/ timer
            if e > 34 and e < 38:        #add timer for suspense
                print(' ' * x + loki_arc_storyline_list[e])
                sleep(0.5)
        
        #lets user make their choice
        loki_choice_pre = input_system_ingame(3, 1)
        
        #acts on what the user chose
        if loki_choice_pre == '1':    #user chooses option 1 
            #acts on the user's choice
            while proceed_r2_1: 
                #checks if they would like to use their enchanted item and if they CAN use it 
                enchanteditem_checker_argument = ask_activate_enchanteditem('Ethos')

                #updates the points, etc.
                if enchanteditem_checker_argument == '0':       #if user does not want to use their item
                    #update the player's points
                    points_tally('Ethos', 15) 

                    #print message to user
                    print('\n' + ' ' * 26 + f'You have spent {CBOLD}{CITALIC}{CYELLOW}15{CEND} ', end = '')
                    print(f'{CBOLD}{CYELLOW}Ethos points{CEND}!\n')

                    #break out of mini-loop
                    proceed_r2_1 = False
                else:       #if the user wants to use their enchanted item
                    if enchanteditem_checker_argument == '1':     
                        if test_the_enchanteditemlimit() == 'True': #checks if user can use enchanted item
                            #saves the new points
                            loki_newpoints = enchanted_item_activated(15, Id_enchanteditem)
                            
                            #update points 
                            points_tally('Ethos', loki_newpoints)
                            
                            #print message to user
                            print(' ' * 26 + f'You have spent ', end = '')
                            print(f'{CBOLD}{CITALIC}{CYELLOW}{loki_newpoints} ', end = '')
                            print(f'{CBOLD}{CYELLOW}Ethos points{CEND}!\n')

                            #break out of mini-loop
                            proceed_r2_1 = False
                        else:
                            #print message to player that their chances are maxxed out
                            print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You exceeded uses for the{CEND}', end = '')
                            print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n')
                    elif enchanteditem_checker_argument == 'incompatible': #enchanted item = incompatible
                        #print out message that they cannot use thier enchanted item
                        print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You cannot use your{CEND}', end = '')
                        print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n') 
            
            sleep(1)    #add suspense

            #in-between story portion for option 1
            for q in range(len(loki_arc_storyline_list)): 
                #adjust indentation of strings
                temp = 26   #the constant that controls indentation
                temp_2 = 0  #the variable that controls indentation

                #customises the indentation
                if q == 38:
                    temp_2 = -16
                elif q > 38 and q < 43:
                    temp_2 = 16

                x = (temp + (temp_2))    #the equation that adjusts the inentation of str's
                
                #prints the lines and adjusts the timing
                if q == 38:
                    print(' ' * x + loki_arc_storyline_list[q])
                elif q > 38 and q < 43:  #prints the quotes
                    sleep(0.5)
                    print(' ' * x + loki_arc_storyline_list[q])
                    sleep(0.5)  #add suspense

            #the second part of option 1
            while proceed_r2_11:     #code is under a while loop for neatness and repeatability 
                #prints choice(s)
                print(loki_arc_storyline_list[43])
                sleep(1)        #add timer for suspense

                #lets player 'choose' (this is pentaly for picking the worng choice)
                not_needed_varible_r2 = input_system_ingame(1, 1)
                
                if not_needed_varible_r2 == '1':
                    #break out of mini-loop
                    proceed_r2_11 = False
                
            #break out of big while loop
            break
        elif loki_choice_pre == '2':  #user chooses option 2 
            #acts on the user's choice
            while proceed_r2_1: 
                #checks if they would like to use their enchanted item and if they CAN use it 
                enchanteditem_checker_argument = ask_activate_enchanteditem('Pathos')

                #updates the points, etc.
                if enchanteditem_checker_argument == '0':       #if user does not want to use their item
                    #update the player's points
                    points_tally('Pathos', 15) 

                    #print message to user
                    print('\n' + ' ' * 26 + f'You have spent {CBOLD}{CITALIC}{CRED}15{CEND} ', end = '')
                    print(f'{CBOLD}{CRED}Pathos points{CEND}!\n')

                    #break out of mini-loop
                    proceed_r2_1 = False
                else:       #if the user wants to use their enchanted item
                    if enchanteditem_checker_argument == '1':     
                        if test_the_enchanteditemlimit() == 'True': #checks if user can use enchanted item
                            #saves the new points
                            loki_newpoints = enchanted_item_activated(15, Id_enchanteditem)
                            
                            #update points 
                            points_tally('Pathos', loki_newpoints)
                            
                            #print message to user
                            print(' ' * 26 + f'You have spent ', end = '')
                            print(f'{CBOLD}{CITALIC}{CRED}{loki_newpoints} ', end = '')
                            print(f'{CBOLD}{CRED}Pathos points{CEND}!\n')

                            #break out of mini-loop
                            proceed_r2_1 = False
                        else:
                            #print message to player that their chances are maxxed out
                            print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You exceeded uses for the{CEND}', end = '')
                            print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n')
                    elif enchanteditem_checker_argument == 'incompatible': #enchanted item = incompatible
                        #print out message that they cannot use thier enchanted item
                        print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You cannot use your{CEND}', end = '')
                        print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n') 

            sleep(1)    #add suspense

            #in-between story portion for option 2
            for q in range(len(loki_arc_storyline_list)): 
                #adjust indentation of strings
                temp = 26   #the constant that controls indentation
                temp_2 = 0  #the variable that controls indentation

                #customises the indentation
                if q > 43 and q < 46:
                    temp_2 = -16
                elif q > 45 and q < 49:
                    temp_2 = 16

                x = (temp + (temp_2))    #the equation that adjusts the inentation of str's
                
                #prints the lines and adjusts the timing
                if q > 43 and q < 46:
                    print(' ' * x + loki_arc_storyline_list[q])
                elif q > 45 and q < 49:  #prints the quotes
                    sleep(0.5)
                    print(' ' * x + loki_arc_storyline_list[q])
                    sleep(0.5)  #add suspense

            #the second part of option 2
            while proceed_r2_11:     #code is under a while loop for neatness and repeatability 
                #prints choice(s)
                print(loki_arc_storyline_list[49])
                sleep(1)        #add timer for suspense

                #lets player 'choose' (this is pentaly for picking the worng choice)
                not_needed_varible_r2 = input_system_ingame(1, 1)

                if not_needed_varible_r2 == '1':
                    #break out of mini-loop
                    proceed_r2_11 = False
                
            #break out of big while loop
            break
        elif loki_choice_pre == '3':  #user chooses option 3 
            #acts on the user's choice
            while proceed_r2_1: 
                #checks if they would like to use their enchanted item and if they CAN use it 
                enchanteditem_checker_argument = ask_activate_enchanteditem('Logos')

                #updates the points, etc.
                if enchanteditem_checker_argument == '0':       #if user does not want to use their item
                    #update the player's points
                    points_tally('Logos', 15) 

                    #print message to user
                    print('\n' + ' ' * 26 + f'You have spent {CBOLD}{CITALIC}{CBLUE}15{CEND} ', end = '')
                    print(f'{CBOLD}{CBLUE}Logos points{CEND}!\n')

                    #break out of mini-loop
                    proceed_r2_1 = False
                else:       #if the user wants to use their enchanted item
                    if enchanteditem_checker_argument == '1':     
                        if test_the_enchanteditemlimit() == 'True': #checks if user can use enchanted item
                            #saves the new points
                            loki_newpoints = enchanted_item_activated(15, Id_enchanteditem)
                            
                            #update points 
                            points_tally('Logos', loki_newpoints)
                            
                            #print message to user
                            print(' ' * 26 + f'You have spent ', end = '')
                            print(f'{CBOLD}{CITALIC}{CBLUE}{loki_newpoints} ', end = '')
                            print(f'{CBOLD}{CBLUE}Logos points{CEND}!\n')

                            #break out of mini-loop
                            proceed_r2_1 = False
                        else:
                            #print message to player that their chances are maxxed out
                            print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You exceeded uses for the{CEND}', end = '')
                            print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n')
                    elif enchanteditem_checker_argument == 'incompatible': #enchanted item = incompatible
                        #print out message that they cannot use thier enchanted item
                        print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You cannot use your{CEND}', end = '')
                        print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n') 

            sleep(1)    #add suspense

            #in-between story portion for option 3
            for q in range(len(loki_arc_storyline_list)): 
                #adjust indentation of strings
                temp = 26   #the constant that controls indentation
                temp_2 = 0  #the variable that controls indentation

                #customises the indentation
                if q == 50:
                    temp_2 = -16
                elif q > 50 and q < 54:
                    temp_2 = 16

                x = (temp + (temp_2))    #the equation that adjusts the inentation of str's
                
                #prints the lines and adjusts the timing
                if q == 50:                 #prints the description
                    print(' ' * x + loki_arc_storyline_list[q])
                elif q > 50 and q < 54:     #prints the quotes
                    sleep(0.5)
                    print(' ' * x + loki_arc_storyline_list[q])
                    sleep(0.5)  #add suspense

            #the second part of option 3
            while proceed_r2_11:     #code is under a while loop for neatness and repeatability 
                #prints choice(s)
                print(loki_arc_storyline_list[54])
                sleep(1)        #add timer for suspense

                #lets player 'choose' (this is pentaly for picking the worng choice)
                not_needed_varible_r2 = input_system_ingame(1, 1)

                #acts on the user's choice
                if not_needed_varible_r2 == '1':
                    #break out of mini-loop
                    proceed_r2_11 = False
                
            #break out of big while loop
            break

    #round 2 | prints intro to 'encounter'
    while True:     #contents are under while loop for neatness 
        print('\n') #add double space for clarity

        #prints intro to the 1st encounter
        for n in range(len(loki_arc_storyline_list)): 
            #adjust indentation of strings
            temp = 26   #the constant that controls indentation
            temp_2 = 0  #the variable that controls indentation

            #customises the indentation 
            if (n > 54 and n < 58) or (n > 61 and n < 65): #the description
                temp_2 = -16
            elif n > 57 and n < 60:     #the quotes (by MC)
                temp_2 = -10
            elif n > 59 and n < 62:     #the quotes (by Loki)
                temp_2 = 16
            elif n == 65:
                temp_2 = 26

            x = (temp + (temp_2))    #the equation that adjusts the inentation of str's
            
            #prints the lines w/ timer
            if (n > 54 and n < 58) or (n > 61 and n < 65): #prints the description
                print(' ' * x + loki_arc_storyline_list[n])
            elif (n > 57 and n < 62) or (n == 65):  #prints the quotes + question
                sleep(0.5)        #add delay for suspense
                print(' ' * x + loki_arc_storyline_list[n])
                sleep(0.5)        #add delay for suspense

        #break out of the loop
        break

    #round 2 | the 'encounter' portion of the Loki Arc
    while True:     #contents are under while loop for neatness 
        #prints the 'encounter' questions
        for m in range(len(loki_arc_storyline_list)): 
            #adjust indentation of strings
            temp = 26   #the constant that controls indentation
            temp_2 = 0  #the variable that controls indentation

            #customises the indentation
            if m > 65 and m < 69: 
                temp_2 = -26

            x = (temp + (temp_2))    #the equation that adjusts the inentation of str's
            
            #prints the lines w/ timer
            if m > 65 and m < 69:
                print(' ' * x + loki_arc_storyline_list[m])
                sleep(0.5)        #add delay for suspense
        
        #lets the user make their choice
        loki_choice_encounter = input_system_ingame(3, 1)

        # acts on the player's choice
        if loki_choice_encounter == '1': #If their choice was 1 
            #the first part of option 1
            while proceed_r2_2:     #nested under a true loop for neatness 
                #checks if they would like to use their enchanted item and if they CAN use it 
                enchanteditem_checker_argument = ask_activate_enchanteditem('Ethos')

                #updates the points, etc.
                if enchanteditem_checker_argument == '0':         #if user does NOT want to use their item
                    #update the player's points
                    points_tally('Ethos', 30) 

                    #print message to user
                    print('\n' + ' ' * 26 + f'You have spent {CBOLD}{CITALIC}{CYELLOW}30{CEND} ', end = '')
                    print(f'{CBOLD}{CYELLOW}Ethos points{CEND}!\n')  
                    
                    #break out of mini while loop
                    proceed_r2_2 = False        
                else:                                           #if user wants to use their item 
                    if enchanteditem_checker_argument == '1':
                        if test_the_enchanteditemlimit() == 'True': #checks if user can use enchanted item
                            #signals that the TRUE ENDING will be met
                            True_ending_confirmation = 1
                            
                            #saves the new points
                            loki_newpoints = enchanted_item_activated(30, Id_enchanteditem)
                            
                            #update points 
                            points_tally('Ethos', loki_newpoints)

                            #print message to user
                            print(' ' * 26 + f'You have spent ', end = '')
                            print(f'{CBOLD}{CITALIC}{CYELLOW}{loki_newpoints} ', end = '')
                            print(f'{CBOLD}{CYELLOW}Ethos points{CEND}!\n')
                            
                            #break out of mini while loop
                            proceed_r2_2 = False
                        else:
                            #print message to player that their chances are maxxed out
                            print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You exceeded uses for the{CEND}', end = '')
                            print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n')
                    elif enchanteditem_checker_argument == 'incompatible': #enchanted item = incompatible
                        #print out message that they cannot use thier enchanted item
                        print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You cannot use your{CEND}', end = '')
                        print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n') 
            
            sleep(1)    #add suspense

            #1st in-between story portion for option 1
            for a in range(len(loki_arc_storyline_list)): 
                #adjust indentation of strings
                temp = 26   #the constant that controls indentation
                temp_2 = 0  #the variable that controls indentation

                #customises the indentation
                temp_2 = -16

                x = (temp + (temp_2))    #the equation that adjusts the inentation of str's
                
                #prints the lines and adjusts the timing
                if a > 68 and a < 74:  
                    print(' ' * x + loki_arc_storyline_list[a])
                elif a == 75:
                    print(' ' * x + loki_arc_storyline_list[a])
                    sleep(0.5)  #add suspense

            #the second part of option 1
            while proceed_r2A_2:     #code is under a while loop for neatness and repeatability 
                #prints choice(s)
                print(loki_arc_storyline_list[76])
                sleep(1)        #add timer for suspense

                #lets player 'choose' (this is pentaly for picking the worng choice)
                loki_choice_encounter_subcategory_1 = input_system_ingame(1, 1)
                
                #updates the points, etc.
                if loki_choice_encounter_subcategory_1 == '1': 
                    #checks if they would like to use their enchanted item and if they CAN use it 
                    enchanteditem_checker_argument = ask_activate_enchanteditem('Pathos')

                    if enchanteditem_checker_argument == '0':         #if user does NOT want to use their item
                        #update the player's points
                        points_tally('Pathos', 25) 

                        #print message to user
                        print('\n' + ' ' * 26 + f'You have spent {CBOLD}{CITALIC}{CRED}25{CEND} ', end = '')
                        print(f'{CBOLD}{CRED}Pathos points{CEND}!\n')  

                        #break out of mini while loop
                        proceed_r2A_2 = False       
                    else:                                           #if user wants to use their item 
                        if enchanteditem_checker_argument == '1': 
                            if test_the_enchanteditemlimit() == 'True': #checks if user can use enchanted item
                                #saves the new points
                                loki_newpoints = enchanted_item_activated(25, Id_enchanteditem)

                                #update points 
                                points_tally('Pathos', loki_newpoints)

                                #print message to user
                                print(' ' * 26 + f'You have spent ', end = '')
                                print(f'{CBOLD}{CITALIC}{CRED}{loki_newpoints} ', end = '')
                                print(f'{CBOLD}{CRED}Ethos points{CEND}!\n')
                                
                                #break out of mini while loop
                                proceed_r2A_2 = False 
                            else:
                                #print message to player that their chances are maxxed out
                                print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You exceeded uses for the{CEND}', end = '')
                                print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n')
                        elif enchanteditem_checker_argument == 'incompatible': #enchanted item = incompatible
                            #print out message that they cannot use thier enchanted item
                            print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You cannot use your{CEND}', end = '')
                            print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n') 
            
            sleep(1)    #add suspense

            #2nd in-between story portion for option 1
            for aa in range(len(loki_arc_storyline_list)): 
                #adjust indentation of strings
                temp = 26   #the constant that controls indentation
                temp_2 = 0  #the variable that controls indentation

                #customises the indentation
                if aa == 77 or aa == 81 or (aa > 82 and aa < 86): #the description
                    temp_2 = -16
                elif aa == 80 or aa == 82 or aa == 88:   #the quotes (by MC)
                    temp_2 = -10 
                elif (aa > 77 and a < 80) or (aa > 85 and aa < 88):   #quotes by Loki
                    temp_2 = 16

                x = (temp + (temp_2))    #the equation that adjusts the inentation of str's
                
                #prints the lines and adjusts the timing
                if (aa > 77 and a < 80) or (aa > 85 and aa < 88):  #prints quotes
                    sleep(0.5)  #add suspense
                    print(' ' * x + loki_arc_storyline_list[aa])
                    sleep(0.5)  #add suspense
                elif aa == 80 or aa == 82 or aa == 88:   #prints quotes pt. 2 
                                                        #to not make the argument longer^^
                    sleep(0.5)  #add suspense
                    print(' ' * x + loki_arc_storyline_list[aa])
                    sleep(0.5)  #add suspense
                elif aa == 77 or aa == 81 or (aa > 82 and aa < 86):
                    print(' ' * x + loki_arc_storyline_list[aa])
            
            #the third part of option 1
            while proceed_r2A_3:     #code is under a while loop for neatness and repeatability 
                #prints choice(s)
                print(loki_arc_storyline_list[89])
                sleep(1)        #add timer for suspense

                #lets player 'choose' (this is pentaly for picking the worng choice)
                loki_choice_encounter_subcategory_2 = input_system_ingame(1, 1)
                
                #updates the points, etc.
                if loki_choice_encounter_subcategory_2 == '1': 
                    #checks if they would like to use their enchanted item and if they CAN use it 
                    enchanteditem_checker_argument = ask_activate_enchanteditem('Logos')

                    if enchanteditem_checker_argument == '0':         #if user does NOT want to use their item
                        #update the player's points
                        points_tally('Logos', 20) 

                        #print message to user
                        print('\n' + ' ' * 26 + f'You have spent {CBOLD}{CITALIC}{CBLUE}20{CEND} ', end = '')
                        print(f'{CBOLD}{CBLUE}Logos points{CEND}!\n')  

                        #break out of mini while loop
                        proceed_r2A_3 = False       
                    else:                                           #if user wants to use their item 
                        if enchanteditem_checker_argument == '1': 
                            if test_the_enchanteditemlimit() == 'True': #checks if user can use enchanted item
                                #saves the new points
                                loki_newpoints = enchanted_item_activated(20, Id_enchanteditem)

                                #update points 
                                points_tally('Logos', loki_newpoints)

                                #print message to user
                                print(' ' * 26 + f'You have spent ', end = '')
                                print(f'{CBOLD}{CITALIC}{CBLUE}{loki_newpoints} ', end = '')
                                print(f'{CBOLD}{CBLUE}Logos points{CEND}!\n')
                                
                                #break out of mini while loop
                                proceed_r2A_3 = False 
                            else:
                                #print message to player that their chances are maxxed out
                                print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You exceeded uses for the{CEND}', end = '')
                                print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n')
                        elif enchanteditem_checker_argument == 'incompatible': #enchanted item = incompatible
                            #print out message that they cannot use thier enchanted item
                            print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You cannot use your{CEND}', end = '')
                            print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n') 

            sleep(1)    #add suspense

            #3rd in-between story portion for option 1
            for aaa in range(len(loki_arc_storyline_list)): 
                #adjust indentation of strings
                temp = 26   #the constant that controls indentation
                temp_2 = 0  #the variable that controls indentation

                #customises the indentation
                if aaa == 90 or aaa == 96 or aaa == 98 or aaa == 100:   #the description
                    temp_2 = -16
                elif (aaa > 90 and aaa < 93) or (aaa > 93 and aaa < 96):   #the quotes (by MC)
                    temp_2 = -10 
                elif aaa == 93 or aaa == 97 or aaa == 99:   #quotes by Loki
                    temp_2 = 16

                x = (temp + (temp_2))    #the equation that adjusts the inentation of str's
                
                #prints the lines and adjusts the timing
                if (aaa > 90 and aaa < 93) or (aaa > 93 and aaa < 96):  #prints quotes
                    sleep(0.5)  #add suspense
                    print(' ' * x + loki_arc_storyline_list[aaa])
                    sleep(0.5)  #add suspense
                elif aaa == 93 or aaa == 97 or aaa == 99:   #prints quotes pt. 2 
                    #I seperatead the "quotes" to not make the argument longer^^
                    sleep(0.5)  #add suspense
                    print(' ' * x + loki_arc_storyline_list[aaa])
                    sleep(0.5)  #add suspense
                elif aaa == 90 or aaa == 96 or aaa == 98 or aaa == 100: #prints description
                    print(' ' * x + loki_arc_storyline_list[aaa])

            #break out of the big big while loop
            break
        elif loki_choice_encounter == '2': #If their choice was 2 
            #the first part of option 2
            while proceed_r2_2:     #nested under a true loop for neatness 
                #checks if they would like to use their enchanted item and if they CAN use it 
                enchanteditem_checker_argument = ask_activate_enchanteditem('Pathos')

                #updates the points, etc.
                if enchanteditem_checker_argument == '0':         #if user does NOT want to use their item
                    #update the player's points
                    points_tally('Pathos', 30) 

                    #print message to user
                    print('\n' + ' ' * 26 + f'You have spent {CBOLD}{CITALIC}{CRED}30{CEND} ', end = '')
                    print(f'{CBOLD}{CRED}Pathos points{CEND}!\n')  
                    
                    #break out of mini while loop
                    proceed_r2_2 = False        
                else:                                           #if user wants to use their item 
                    if enchanteditem_checker_argument == '1':
                        if test_the_enchanteditemlimit() == 'True': #checks if user can use enchanted item
                            #signals that the TRUE ENDING will be met
                            True_ending_confirmation = 1
                            
                            #saves the new points
                            loki_newpoints = enchanted_item_activated(30, Id_enchanteditem)
                            
                            #update points 
                            points_tally('Pathos', loki_newpoints)

                            #print message to user
                            print(' ' * 26 + f'You have spent ', end = '')
                            print(f'{CBOLD}{CITALIC}{CRED}{loki_newpoints} ', end = '')
                            print(f'{CBOLD}{CRED}Pathos points{CEND}!\n')
                            
                            #break out of mini while loop
                            proceed_r2_2 = False
                        else:
                            #print message to player that their chances are maxxed out
                            print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You exceeded uses for the{CEND}', end = '')
                            print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n')
                    elif enchanteditem_checker_argument == 'incompatible': #enchanted item = incompatible
                        #print out message that they cannot use thier enchanted item
                        print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You cannot use your{CEND}', end = '')
                        print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n') 
            
            sleep(1)    #add suspense

            #1st in-between story portion for option 2
            for a in range(len(loki_arc_storyline_list)): 
                #adjust indentation of strings
                temp = 26   #the constant that controls indentation
                temp_2 = 0  #the variable that controls indentation

                #customises the indentation
                if (a > 102 and a < 111) or (a > 112 and a < 117): #description
                    temp_2 = -16
                elif a == 101 or a == 118 or a == 121: #description pt. 2
                    temp_2 = -16
                elif a == 102 or a == 111 or a == 112 or a == 116 or a == 117:  #quotes (LOKI)
                    temp_2 = 16
                elif a > 117 and a < 121: #quotes (LOKI) pt.2
                    temp_2 = 16
                elif a > 121 and a < 124:   #quotes (MC)
                    temp_2 = -10

                x = (temp + (temp_2))    #the equation that adjusts the inentation of str's
                
                #prints the lines and adjusts the timing
                if (a > 102 and a < 111) or (a > 112 and a < 117):  #description
                    print(' ' * x + loki_arc_storyline_list[a])
                elif a == 101 or a == 118 or a == 121:  #description pt. 2
                    print(' ' * x + loki_arc_storyline_list[a])
                elif a == 102 or a == 111 or a == 112 or a == 116 or a == 117:  #quotes 
                    sleep(0.5)  #add suspense
                    print(' ' * x + loki_arc_storyline_list[a])
                    sleep(0.5)  #add suspense
                elif (a > 117 and a < 121) or (a > 117 and a < 121) or (a > 121 and a < 124):
                    #^^quotes pt. 2
                    sleep(0.5)  #add suspense
                    print(' ' * x + loki_arc_storyline_list[a])
                    sleep(0.5)  #add suspense

            #the second part of option 2
            while proceed_r2A_2:     #code is under a while loop for neatness and repeatability 
                #prints choice(s)
                print(loki_arc_storyline_list[124])
                sleep(1)        #add timer for suspense

                #lets player 'choose' (this is pentaly for picking the worng choice)
                loki_choice_encounter_subcategory_1 = input_system_ingame(1, 1)
                
                #updates the points, etc.
                if loki_choice_encounter_subcategory_1 == '1': 
                    #checks if they would like to use their enchanted item and if they CAN use it 
                    enchanteditem_checker_argument = ask_activate_enchanteditem('Logos')

                    if enchanteditem_checker_argument == '0':         #if user does NOT want to use their item
                        #update the player's points
                        points_tally('Logos', 25) 

                        #print message to user
                        print('\n' + ' ' * 26 + f'You have spent {CBOLD}{CITALIC}{CBLUE}25{CEND} ', end = '')
                        print(f'{CBOLD}{CBLUE}Logos points{CEND}!\n')  

                        #break out of mini while loop
                        proceed_r2A_2 = False       
                    else:                                           #if user wants to use their item 
                        if enchanteditem_checker_argument == '1': 
                            if test_the_enchanteditemlimit() == 'True': #checks if user can use enchanted item
                                #saves the new points
                                loki_newpoints = enchanted_item_activated(25, Id_enchanteditem)

                                #update points 
                                points_tally('Logos', loki_newpoints)

                                #print message to user
                                print(' ' * 26 + f'You have spent ', end = '')
                                print(f'{CBOLD}{CITALIC}{CBLUE}{loki_newpoints} ', end = '')
                                print(f'{CBOLD}{CBLUE}Logos points{CEND}!\n')
                                
                                #break out of mini while loop
                                proceed_r2A_2 = False 
                            else:
                                #print message to player that their chances are maxxed out
                                print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You exceeded uses for the{CEND}', end = '')
                                print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n')
                        elif enchanteditem_checker_argument == 'incompatible': #enchanted item = incompatible
                            #print out message that they cannot use thier enchanted item
                            print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You cannot use your{CEND}', end = '')
                            print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n') 
            
            sleep(1)    #add suspense

            #2nd in-between story portion for option 2
            for aa in range(len(loki_arc_storyline_list)): 
                #adjust indentation of strings
                temp = 26   #the constant that controls indentation
                temp_2 = 0  #the variable that controls indentation

                #customises the indentation
                if aa == 125 or aa == 133 or (aa > 126 and aa < 130): #the description
                    temp_2 = -16
                elif aa > 130 and aa < 133:   #the quotes (by MC)
                    temp_2 = -10
                elif aa == 126:   #quotes by Loki
                    temp_2 = 16

                x = (temp + (temp_2))    #the equation that adjusts the inentation of str's
                
                #prints the lines and adjusts the timing
                if (aa > 130 and aa < 133) or aa == 126:  #prints quotes
                    sleep(0.5)  #add suspense
                    print(' ' * x + loki_arc_storyline_list[aa])
                    sleep(0.5)  #add suspense
                elif aa == 125 or aa == 133 or (aa > 126 and aa < 130): #description
                    print(' ' * x + loki_arc_storyline_list[aa])
            
            #the third part of option 2
            while proceed_r2A_3:     #code is under a while loop for neatness and repeatability 
                #prints choice(s)
                print(loki_arc_storyline_list[134])
                sleep(1)        #add timer for suspense

                #lets player 'choose' (this is pentaly for picking the worng choice)
                loki_choice_encounter_subcategory_2 = input_system_ingame(1, 1)
                
                #updates the points, etc.
                if loki_choice_encounter_subcategory_2 == '1': 
                    #checks if they would like to use their enchanted item and if they CAN use it 
                    enchanteditem_checker_argument = ask_activate_enchanteditem('Ethos')

                    if enchanteditem_checker_argument == '0':         #if user does NOT want to use their item
                        #update the player's points
                        points_tally('Ethos', 20) 

                        #print message to user
                        print('\n' + ' ' * 26 + f'You have spent {CBOLD}{CITALIC}{CYELLOW}20{CEND} ', end = '')
                        print(f'{CBOLD}{CYELLOW}Ethos points{CEND}!\n')  

                        #break out of mini while loop
                        proceed_r2A_3 = False       
                    else:                                           #if user wants to use their item 
                        if enchanteditem_checker_argument == '1': 
                            if test_the_enchanteditemlimit() == 'True': #checks if user can use enchanted item
                                #saves the new points
                                loki_newpoints = enchanted_item_activated(20, Id_enchanteditem)

                                #update points 
                                points_tally('Ethos', loki_newpoints)

                                #print message to user
                                print(' ' * 26 + f'You have spent ', end = '')
                                print(f'{CBOLD}{CITALIC}{CYELLOW}{loki_newpoints} ', end = '')
                                print(f'{CBOLD}{CYELLOW}Ethos points{CEND}!\n')
                                
                                #break out of mini while loop
                                proceed_r2A_3 = False 
                            else:
                                #print message to player that their chances are maxxed out
                                print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You exceeded uses for the{CEND}', end = '')
                                print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n')
                        elif enchanteditem_checker_argument == 'incompatible': #enchanted item = incompatible
                            #print out message that they cannot use thier enchanted item
                            print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You cannot use your{CEND}', end = '')
                            print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n') 

            sleep(1)    #add suspense

            #3rd in-between story portion for option 2
            for aaa in range(len(loki_arc_storyline_list)): 
                #adjust indentation of strings
                temp = 26   #the constant that controls indentation
                temp_2 = 0  #the variable that controls indentation

                #customises the indentation
                if (aaa > 145 and aaa < 148) or (aaa > 134 and aaa < 142):   #the description
                    temp_2 = -16
                elif aaa == 143 or (aaa > 148 and aaa < 151) or (aaa > 151 and aaa < 154):
                    #^^description pt. 2 - to be neater
                    temp_2 = -16
                elif aaa == 148 or aaa == 145 or aaa == 151:   #the quotes (by MC)
                    temp_2 = -10 
                elif aaa == 142 or aaa == 143:   #quotes by Loki
                    temp_2 = 16
                
                x = (temp + (temp_2))    #the equation that adjusts the inentation of str's
                
                #prints the lines and adjusts the timing
                if aaa == 142 or (aaa > 143 and aaa < 146):  #prints quotes
                    sleep(0.5)  #add suspense
                    print(' ' * x + loki_arc_storyline_list[aaa])
                    sleep(0.5)  #add suspense
                elif aaa == 148 or aaa == 151:   #prints quotes pt. 2 
                    #I seperatead the "quotes" to not make the argument longer^^
                    sleep(0.5)  #add suspense
                    print(' ' * x + loki_arc_storyline_list[aaa])
                    sleep(0.5)  #add suspense
                elif aaa == 143 or (aaa > 148 and aaa < 151) or (aaa > 151 and aaa < 154): 
                    #^^#prints description
                    print(' ' * x + loki_arc_storyline_list[aaa])
                elif (aaa > 145 and aaa < 148) or (aaa > 134 and aaa < 142): #prints description
                    print(' ' * x + loki_arc_storyline_list[aaa])

            #break out of the big big while loop
            break   
        elif loki_choice_encounter == '3': #If their choice was 3 
            while proceed_r2_2:     #nested under a true loop for neatness 
                #checks if they would like to use their enchanted item and if they CAN use it 
                enchanteditem_checker_argument = ask_activate_enchanteditem('Logos')

                #updates the points, etc.
                if enchanteditem_checker_argument == '0':         #if user does NOT want to use their item
                    #update the player's points
                    points_tally('Logos', 30) 

                    #print message to user
                    print('\n' + ' ' * 26 + f'You have spent {CBOLD}{CITALIC}{CBLUE}30{CEND} ', end = '')
                    print(f'{CBOLD}{CBLUE}Logos points{CEND}!\n')  
                    
                    #break out of mini while loop
                    proceed_r2_2 = False        
                else:                                           #if user wants to use their item 
                    if enchanteditem_checker_argument == '1':
                        if test_the_enchanteditemlimit() == 'True': #checks if user can use enchanted item
                            #signals that the TRUE ENDING will be met
                            True_ending_confirmation = 1
                            
                            #saves the new points
                            loki_newpoints = enchanted_item_activated(30, Id_enchanteditem)
                            
                            #update points 
                            points_tally('Logos', loki_newpoints)

                            #print message to user
                            print(' ' * 26 + f'You have spent ', end = '')
                            print(f'{CBOLD}{CITALIC}{CBLUE}{loki_newpoints} ', end = '')
                            print(f'{CBOLD}{CBLUE}Logos points{CEND}!\n')
                            
                            #break out of mini while loop
                            proceed_r2_2 = False
                        else:
                            #print message to player that their chances are maxxed out
                            print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You exceeded uses for the{CEND}', end = '')
                            print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n')
                    elif enchanteditem_checker_argument == 'incompatible': #enchanted item = incompatible
                        #print out message that they cannot use thier enchanted item
                        print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You cannot use your{CEND}', end = '')
                        print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n') 
            
            sleep(1)    #add suspense

            #1st in-between story portion for option 3
            for a in range(len(loki_arc_storyline_list)): 
                #adjust indentation of strings
                temp = 26   #the constant that controls indentation
                temp_2 = 0  #the variable that controls indentation

                #customises the indentation
                if a == 154 or a == 164 or (a > 155 and a < 163) or (a > 165 and a < 169): 
                    #description^^
                    temp_2 = -16
                elif a == 155 or a == 163 or a == 165: #quotes (LOKI) pt.2
                    temp_2 = 16

                x = (temp + (temp_2))    #the equation that adjusts the inentation of str's
                
                #prints the lines and adjusts the timing
                if a == 154 or a == 164 or (a > 155 and a < 163) or (a > 165 and a < 169):  
                    #description^^
                    print(' ' * x + loki_arc_storyline_list[a])
                elif a == 155 or a == 163 or a == 165:  #^^quotes 
                    sleep(0.5)  #add suspense
                    print(' ' * x + loki_arc_storyline_list[a])
                    sleep(0.5)  #add suspense

            #the second part of option 3
            while proceed_r2A_2:     #code is under a while loop for neatness and repeatability 
                #prints choice(s)
                print(loki_arc_storyline_list[169])
                sleep(1)        #add timer for suspense

                #lets player 'choose' (this is pentaly for picking the worng choice)
                loki_choice_encounter_subcategory_1 = input_system_ingame(1, 1)
                
                #updates the points, etc.
                if loki_choice_encounter_subcategory_1 == '1': 
                    #checks if they would like to use their enchanted item and if they CAN use it 
                    enchanteditem_checker_argument = ask_activate_enchanteditem('Ethos')

                    if enchanteditem_checker_argument == '0':         #if user does NOT want to use their item
                        #update the player's points
                        points_tally('Ethos', 25) 

                        #print message to user
                        print('\n' + ' ' * 26 + f'You have spent {CBOLD}{CITALIC}{CYELLOW}25{CEND} ', end = '')
                        print(f'{CBOLD}{CYELLOW}Ethos points{CEND}!\n')  

                        #break out of mini while loop
                        proceed_r2A_2 = False       
                    else:                                           #if user wants to use their item 
                        if enchanteditem_checker_argument == '1': 
                            if test_the_enchanteditemlimit() == 'True': #checks if user can use enchanted item
                                #saves the new points
                                loki_newpoints = enchanted_item_activated(25, Id_enchanteditem)

                                #update points 
                                points_tally('Ethos', loki_newpoints)

                                #print message to user
                                print(' ' * 26 + f'You have spent ', end = '')
                                print(f'{CBOLD}{CITALIC}{CYELLOW}{loki_newpoints} ', end = '')
                                print(f'{CBOLD}{CYELLOW}Ethos points{CEND}!\n')
                                
                                #break out of mini while loop
                                proceed_r2A_2 = False 
                            else:
                                #print message to player that their chances are maxxed out
                                print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You exceeded uses for the{CEND}', end = '')
                                print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n')
                        elif enchanteditem_checker_argument == 'incompatible': #enchanted item = incompatible
                            #print out message that they cannot use thier enchanted item
                            print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You cannot use your{CEND}', end = '')
                            print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n') 
            
            sleep(1)    #add suspense

            #2nd in-between story portion for option 3
            for aa in range(len(loki_arc_storyline_list)): 
                #adjust indentation of strings
                temp = 26   #the constant that controls indentation
                temp_2 = 0  #the variable that controls indentation

                #customises the indentation
                if aa == 181 or aa == 178 or (aa > 169 and aa < 174): #the description
                    temp_2 = -16
                elif aa > 178 and aa < 181:   #the quotes (by MC)
                    temp_2 = -10
                elif aa > 173 and aa < 178:   #quotes by Loki
                    temp_2 = 16

                x = (temp + (temp_2))    #the equation that adjusts the inentation of str's
                
                #prints the lines and adjusts the timing
                if (aa > 178 and aa < 181) or (aa > 173 and aa < 178): #prints quotes
                    sleep(0.5)  #add suspense
                    print(' ' * x + loki_arc_storyline_list[aa])
                    sleep(0.5)  #add suspense
                elif aa == 181 or aa == 178 or (aa > 169 and aa < 174): #description
                    print(' ' * x + loki_arc_storyline_list[aa])
            
            #the third part of option 3
            while proceed_r2A_3:     #code is under a while loop for neatness and repeatability 
                #prints choice(s)
                print(loki_arc_storyline_list[182])
                sleep(1)        #add timer for suspense

                #lets player 'choose' (this is pentaly for picking the worng choice)
                loki_choice_encounter_subcategory_2 = input_system_ingame(1, 1)
                
                #updates the points, etc.
                if loki_choice_encounter_subcategory_2 == '1': 
                    #checks if they would like to use their enchanted item and if they CAN use it 
                    enchanteditem_checker_argument = ask_activate_enchanteditem('Pathos')

                    if enchanteditem_checker_argument == '0':         #if user does NOT want to use their item
                        #update the player's points
                        points_tally('Pathos', 20) 

                        #print message to user
                        print('\n' + ' ' * 26 + f'You have spent {CBOLD}{CITALIC}{CRED}20{CEND} ', end = '')
                        print(f'{CBOLD}{CRED}Pathos points{CEND}!\n')  

                        #break out of mini while loop
                        proceed_r2A_3 = False       
                    else:                                           #if user wants to use their item 
                        if enchanteditem_checker_argument == '1': 
                            if test_the_enchanteditemlimit() == 'True': #checks if user can use enchanted item
                                #saves the new points
                                loki_newpoints = enchanted_item_activated(20, Id_enchanteditem)

                                #update points 
                                points_tally('Pathos', loki_newpoints)

                                #print message to user
                                print(' ' * 26 + f'You have spent ', end = '')
                                print(f'{CBOLD}{CITALIC}{CRED}{loki_newpoints} ', end = '')
                                print(f'{CBOLD}{CRED}Pathos points{CEND}!\n')
                                
                                #break out of mini while loop
                                proceed_r2A_3 = False 
                            else:
                                #print message to player that their chances are maxxed out
                                print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You exceeded uses for the{CEND}', end = '')
                                print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n')
                        elif enchanteditem_checker_argument == 'incompatible': #enchanted item = incompatible
                            #print out message that they cannot use thier enchanted item
                            print('\n' + ' ' * 26 + f'{CURL}{CURLUP}You cannot use your{CEND}', end = '')
                            print(f'{CURL}{CURLUP} enchanted item. Try again.{CEND}\n') 

            sleep(1)    #add suspense

            #3rd in-between story portion for option 3
            for aaa in range(len(loki_arc_storyline_list)): 
                #adjust indentation of strings
                temp = 26   #the constant that controls indentation
                temp_2 = 0  #the variable that controls indentation

                #customises the indentation
                if aaa == 197 or aaa == 195 or (aaa > 191 and aaa < 194):   #the description
                    temp_2 = -16
                elif (aaa > 182 and aaa < 185) or (aaa > 186 and aaa < 191):
                    #^^description pt. 2 - to be neater
                    temp_2 = -16
                elif aaa == 191 or aaa == 194 or aaa == 196:   #the quotes (by MC)
                    temp_2 = -10 
                elif aaa == 185 or aaa == 186:   #quotes by Loki
                    temp_2 = 16
                
                x = (temp + (temp_2))    #the equation that adjusts the inentation of str's
                
                #prints the lines and adjusts the timing
                if aaa == 191 or aaa == 194 or aaa == 196:  #prints quotes
                    sleep(0.5)  #add suspense
                    print(' ' * x + loki_arc_storyline_list[aaa])
                    sleep(0.5)  #add suspense
                elif aaa == 185 or aaa == 186:   #prints quotes pt. 2 
                    #I seperatead the "quotes" to not make the argument longer^^
                    sleep(0.5)  #add suspense
                    print(' ' * x + loki_arc_storyline_list[aaa])
                    sleep(0.5)  #add suspense
                elif aaa == 197 or aaa == 195 or (aaa > 191 and aaa < 194): 
                    #^^#prints description
                    print(' ' * x + loki_arc_storyline_list[aaa])
                elif (aaa > 182 and aaa < 185) or (aaa > 186 and aaa < 191): #prints description
                    print(' ' * x + loki_arc_storyline_list[aaa])

            #break out of the big big while loop
            break 

    ending_embelishment('loki')
    sleep(1)

    #the 'ending' portion of the Loki arc
    while True:     #contents are under while loop for neatness 
        #add timer for suspense
        sleep(1)

        #print the final portion of the Anansi Arc 
        for r in range(len(loki_arc_storyline_list)): 
            #adjust indentation of strings
            temp = 26   #the constant that controls indentation
            temp_2 = 0  #the variable that controls indentation

            #adjusts indentation
            if r > 197 and r < 205:   #limits index to: 198-204
                temp_2 = -16

            x = (temp + (temp_2))   #the equation that controls indentation
            
            #modifies the time and prints the strings
            if r > 197 and r < 203:   #limits index to: 28-30 
                print(' ' * x + f'{loki_arc_storyline_list[r]}')
            elif r == 204:           #limits index to: 31 
                print(' ' * x + f'{loki_arc_storyline_list[r]}')
                sleep(1)
        
        #break out of while loop
        break

    ending_embelishment('loki')
    sleep(1)

    #prints summary and rewards of the Loki Arc
    while True:     #contents are under while loop for neatness 
        #prints the rewards and summary
        for title, rewards in loki_arc_ending_dictionary.items():     #display the body w/ format 
            print(' ' * 5 + title)     #name = key, goes thorugh the dictionary one by one
            sleep(0.5)  #delays printing of title
            for reward in rewards:    #description = values in list, goes thorugh each value in list
                print(' ' * 10 + reward)     #adds indent and description
                sleep(0.5)  #delays printing of each body of text

        #break out of while loop
        break

    #output
    ending_embelishment('loki')
    sleep(1)

def the_endings():                                              #has all the different endings 
    """
    Contains all the possible endings for the game if completed sucessfully!
    args:
        none
    returns:
        none
    """
    #initialise lists
    true_ending_list = [
        f'The hand is warm and familiar.',
        f'You look up at the wrinkled smile and it is benevolent and warm.',
        f'You smile as {CVIOLETBG2}Hestia{CEND} pulls you up and brings you in an affectionate embrace.',
        f'“{CVIOLET2}You did so well, my brave{CWHITE} {CDOUBLEURL}{Player_name}{CEND}, '
            f'{CVIOLET2}but now it is time to go home.{CEND}',
        f'She holds your hand as you babble on about your adventures.',
        f'Your mother tears up as she scoops you into her arms.',
        f'You reassure her that all is well and bring your {CVIOLETBG2}aunt Hestia{CEND} into the house.',
        f'Your mother gives her a thankful smile and lights your home’s hearth. '
            f'Your [{CBOLD}Journey Home{CEND} has concluded',
        f'The crackling of the fire, the hushed happy voices of your family, and the warmth '
            f'in your home lulls you to a peaceful sleep.\n'
    ]
    ethos_ending_list = [   #all the str's inside the ethos ending 
        f'Your eyes focus and unfocus yet you know who you’re looking at.', 
        f'{CYELLOW2}“My present did you well, {CWHITE}{CDOUBLEURL}{Player_name}{CEND} '
            f'{CYELLOW2}you showed that puny trickster,”{CEND} {CYELLOWBG2}Sun Wukong{CEND} cackles.',
        f'He hoists your injured body and taunts the {CGREEN}goddess{CEND} you ‘sent packing’ until the '
            f'familiar door of your home greets you.',
        f'Your mother almost gets a heart attack as she sees her {CWHITEBG}child{CEND}, the '
            f'{CYELLOWBG2}monkey King{CEND}, and a {CVIOLETBG}loud-mouthed pig{CEND} barge into her home.',
        f'You end the day developed by warmth and a soothing feeling of contentment.', 
        f'Your family and new friends get on like a house on fire.',
        f'All night Long {CYELLOWBG2}Sun Wukong{CEND} and {CVIOLETBG}Zhu Bajie{CEND} recall long tales '
            f'to you and your mother.',
        f'You exchange details of your {CBOLD}Journey Home{CEND} and laugh until the yellow sun '
            f'peeks over the horizon.\n'
        ]
    pathos_ending_list = [  #all the str's inside the pathos ending 
        f'Not hand, more like many hands.', 
        f'When you raise your head you see the smiling spider god, Anansi.',
        f'{CRED2}“This story will be an entertaining one, {CDOUBLEURL}{CWHITE}{Player_name}{CEND},'
            f'{CRED2} a comedy and action one for the ages!”{CEND} {CREDBG2}Anansi’s{CEND} '
            f'eyes form cresents.',
        f'{CRED2}“Your use of my webs will be the highlight of course!”{CEND}', 
        f'The spider wraps you in webs and brings you to your home.',
        f'Your mother scolds you while {CREDBG2}Anansi{CEND} giggles in the background.',
        f'Your day ends with your mother and {CREDBG2}Anansi{CEND} sitting at the edge of their '
            f'seats as you recount the story of your journey.', 
        f'Seeing {CREDBG2}Anansi{CEND}, meeting {CGREYBG}other gods{CEND}, and finally defeating '
            f'{CGREENBG}Loki{CEND}.', 
        f'Your mother scolds you a second time and {CREDBG2}Anansi{CEND} advises to take a break '
            f'before providing him with any other action-packed stories.',
        f'You agree your {CBOLD}Journey Home{CEND} should be your last adventure, '
            f'at least for a while.'
            f'The night continues with plenty of laughs and food.\n',
        ]
    logos_ending_list = [   #all the str's inside the logos ending 
        f'Your vision clears and it is not one hand.',
        f'It is a pair of hands, both have familiar faces which smile down on you.',
        f'{CBLUE2}“You used our little gift, {CWHITE}{CDOUBLEURL}{Player_name}{CEND} '
            f'{CBLUE2}that was an exciting match!”{CEND} {CSELECTED}{CBLUE2}Junajpu{CEND} exclaims pulling you up.', 
        f'{CSELECTED}{CBEIGE2}Ixb’alanke{CEND} pats your back, {CBEIGE2}“Now gods and monsters alike will know better than to mess with us!”{CEND}',
        f'You grin along with them and they guide you home.',
        f'Your mother invites {CSELECTED}{CBLUE2}Junajpu{CEND} and {CSELECTED}{CBEIGE2}Ixb’alanke{CEND} in after berating you for once again getting hurt on the way home.', 
        f'The feast your mother prepares lulls you and your new friends to sleep.',
        f'With your friends knocked out on the couch and you on a nearby chair, you end the day loved and cared for and at home.',
        f'You would not end your {CBOLD}Journey Home{CEND} any other way\n',
    ]

    #initiate variables 
    global True_ending_confirmation
    
    #no input

    #process

    #comparing the digits - from 3.4 (nested conditionals) HW
    ending_embelishment('end')
    sleep(1)

    if True_ending_confirmation == 1:   #if the player fulfils the condition to get True Ending 
        while True:     #nested under a true loop to keep it clean 
            #prints ending contents
            for h in range(len(true_ending_list)): 
                #adjust indentation of strings
                temp = 26   #the constant that controls indentation
                temp_2 = 0  #the variable that controls indentation
                
                if h == 3:    #quotes
                    temp_2 = 16
                elif h < 3 or h > 3 and h < 9:  #description
                    temp_2 = -16

                x = (temp + (temp_2))   #the equation that controls indentation
                
                #modifies time it will print and prints the lines
                if h < 3 or (h > 3 and h < 9):    #quotes
                    print(' ' * x + true_ending_list[h])
                    sleep(0.5)
                else:   #description
                    print(' ' * x + true_ending_list[h])
                    sleep(1)

            #prints what ending player got
            true_ending_str = f'{CBOLD}YOU GOT THE {CITALIC}{CVIOLET2}TRUE ENDING{CEND}\n' 
            print(f' ' * 56, end = '')     #put empty space on the same line
            for l in true_ending_str:     #code that mimics a type-writer: from stackoverflow!
                sys.stdout.write(l)
                sys.stdout.flush()
                time.sleep(0.1)

            break     #break out of loop  
    
    elif Players_attributes['Ethos'] > Players_attributes['Pathos']:    #implies that Ethos is the greatest. 
        if Players_attributes['Ethos']  > Players_attributes['Logos'] : #Ethos ending
            #Ethos is the largest player attribute: Ethos Ending
            while True:     #nested under a true loop to keep it clean 
                #prints ending contents
                for ii in range(len(ethos_ending_list)): 
                    #adjust indentation of strings
                    temp = 26   #the constant that controls indentation
                    temp_2 = 0  #the variable that controls indentation
                    
                    if ii == 1:                #qutoes (Character)
                        temp_2 = 16
                    elif ii == 0 or ii > 1 and ii < 8:  #description
                        temp_2 = -16

                    x = (temp + (temp_2))   #the equation that controls indentation
                    
                    #modifies time it will print and prints the lines
                    if ii == 1:    #quotes
                        print(' ' * x + ethos_ending_list[ii])
                        sleep(0.5)
                    else:   #description
                        print(' ' * x + ethos_ending_list[ii])
                        sleep(1)

                #prints what ending player got
                ethos_ending_str = f'{CBOLD}YOU GOT THE {CITALIC}{CYELLOW}✧  ETHOS ENDING ✧{CEND}\n' 
                print(f' ' * 56, end = '')     #put empty space on the same line
                for l in ethos_ending_str:     #code that mimics a type-writer: from stackoverflow!
                    sys.stdout.write(l)
                    sys.stdout.flush()
                    time.sleep(0.1)

                break     #break out of loop 
        else:                                                           #logos ending 
            #Logos is the largest player attribute: Logos Ending
            while True:     #nested under a true loop to keep it clean 
                #prints ending contents
                for i in range(len(logos_ending_list)): 
                    #adjust indentation of strings
                    temp = 26   #the constant that controls indentation
                    temp_2 = 0  #the variable that controls indentation
                    
                    if i == 2 or i == 3:    #quotes
                        temp_2 = 16
                    elif i < 2 or i > 3 and i < 9:  #description
                        temp_2 = -16

                    x = (temp + (temp_2))   #the equation that controls indentation
                    
                    #modifies time it will print and prints the lines
                    if i < 2 or (i > 3 and i < 9):    #quotes
                        print(' ' * x + ethos_ending_list[i])
                        sleep(0.5)
                    else:   #description
                        print(' ' * x + ethos_ending_list[i])
                        sleep(1)

                #prints what ending player got
                logos_ending_str = f'{CBOLD}YOU GOT THE {CITALIC}{CBLUE}𖡎  LOGOS ENDING 𖡎{CEND}\n' 
                print(f' ' * 56, end = '')     #put empty space on the same line
                for l in logos_ending_str:     #code that mimics a type-writer: from stackoverflow!
                    sys.stdout.write(l)
                    sys.stdout.flush()
                    time.sleep(0.1)

                break     #break out of loop
    
    elif Players_attributes['Pathos'] > Players_attributes['Logos']: #implies that Pathos is the greatest. 
        if Players_attributes['Pathos'] > Players_attributes['Ethos']:
            #Pathos is the largest player attribute: Pathos Ending
            while True:     #nested under a true loop to keep it clean 
                #prints ending contents
                for iii in range(len(pathos_ending_list)): 
                    #adjust indentation of strings
                    temp = 26   #the constant that controls indentation
                    temp_2 = 0  #the variable that controls indentation
                    
                    if iii == 2 or iii == 3:  #quotes
                        temp_2 = 16
                    elif iii < 2 or iii > 3 and iii < 10:    #description
                        temp_2 = -16

                    x = (temp + (temp_2))   #the equation that controls indentation
                    
                    #modifies time it will print and prints the lines
                    if iii == 2 or iii == 3 or iii == 9:    #quotes
                        print(' ' * x + pathos_ending_list[iii])
                        sleep(0.5)
                    else:   #description
                        print(' ' * x + pathos_ending_list[iii])
                        sleep(1)

                #prints what ending player got
                pathos_ending_str = f'{CBOLD}YOU GOT THE {CITALIC}{CRED}❣ PATHOS ENDING ❣{CEND}\n' 
                print(f' ' * 56, end = '')     #put empty space on the same line
                for l in pathos_ending_str:     #code that mimics a type-writer: from stackoverflow!
                    sys.stdout.write(l)
                    sys.stdout.flush()
                    time.sleep(0.1)

                break     #break out of loop

    else:   #if by some miracle, at the end all the numbers are equal it will default to the Logos ending
        #Logos is the largest player attribute: Logos Ending
        while True:     #nested under a true loop to keep it clean 
            #prints ending contents
            for i in range(len(logos_ending_list)): 
                #adjust indentation of strings
                temp = 26   #the constant that controls indentation
                temp_2 = 0  #the variable that controls indentation
                
                if i == 2 or i == 3:    #quotes
                    temp_2 = 16
                elif i < 2 or i > 3 and i < 9:  #description
                    temp_2 = -16

                x = (temp + (temp_2))   #the equation that controls indentation
                
                #modifies time it will print and prints the lines
                if i < 2 or (i > 3 and i < 9):    #quotes
                    print(' ' * x + logos_ending_list[i])
                    sleep(0.5)
                else:   #description
                    print(' ' * x + logos_ending_list[i])
                    sleep(1)

            #prints what ending player got
            logos_ending_str = f'{CBOLD}YOU GOT THE {CITALIC}{CBLUE}𖡎  LOGOS ENDING 𖡎{CEND}\n' 
            print(f' ' * 56, end = '')     #put empty space on the same line
            for l in logos_ending_str:     #code that mimics a type-writer: from stackoverflow!
                sys.stdout.write(l)
                sys.stdout.flush()
                time.sleep(0.1)

            break     #break out of loop
    
    #output
    sleep(1)
    ending_embelishment('ending')
    sys.exit()      #ends the game

###

#MAIN PROGRAM / OUTPUT
the_menu()
choose_enchanted_item()
anansi_arc()
junajpu_ixbalanke_arc()
sun_wukong_arc()
loki_arc()
the_endings()

###

#TESTS
#the test functions
def test_input_str_checking():                                  #test 1 
    '''
    Test for the function input_checking(highest, lowest) using 3 different cases.
            Test 1: misspelled word: 'pprofile'
            Test 2: upperase word: 'Side Quests
            Test 3: inputted a word that is not accepted
    args: 
        none
    returns:
        none
    '''
    #input

    #process
    #Test 1 - Misspelled word
    if input_str_checking(Str_inputs, 'pprofile') == 'not found':
        print('\nTesting the "input_str_checking()":\nTest 1: Pass')
    else: 
        print('\nTesting the "input_str_checking()":\nTest 1: Fail')

    #Test 2 - Uppercase word
    if input_str_checking(Str_inputs, 'Side Quests') == 'found':
        print('Test 2: Pass')
    else:
        print('Test 2: Fail')

    #Test 3 - inputted a word not applicable
    if input_str_checking(Str_inputs, 'bio') == 'not found':
        print('Test 3: Pass')
    else:
        print('Test 3: Fail')
    
    # output
    print('Test Finished')
def test_the_inventory():                                       #test 2 
    '''
    Test for the function the_inventory(index_address) using 3 different cases.
            Test 1: index_address inputted is out of range of indexes
            Test 2: index_address inputted is a string
            Test 3: a normal case (input 5)
    args: 
        none
    returns:
        none
    '''
    #no input

    #process
    #Test 1 - index inputted is out of range
    if the_inventory(13) == 'indexerror_payattention_abby':
        print('\nTesting the "input_str_checking()":\nTest 1: Pass')
    else:
        print('\nTesting the "input_str_checking()":\nTest 1: Fail')
        print(the_inventory(13))

    #Test 2 - index inputted is a string
    if the_inventory('e') == 'shouldbeanint_abby':
        print('Test 2: Pass')
    else:
        print('Test 2: Fail')

    #Test 3 - normal case (index: 5)
    if the_inventory(5) == ['Mosquito Jar\n\tA gift from the Hero Twins \x1b[94mJunajpu\x1b[0m and \x1b[96mIxb’alanke\x1b[0m. It houses 1 mosquito that can multiply and absorb the life force of its victims.']:
        print('Test 3: Pass')
    else:
        print('Test 3: Fail')
    
    #output
    print('Test Finished')
def test_points_tally():                                        #test 3 
    '''
    Test for the function points_tally(attribute_affecte, dec_num) using 3 different cases.
            Test 1: index_address inputted is out of range of indexes
            Test 2: index_address inputted is a string
            Test 3: checks the validity of the attribute_affected
    args: 
        none
    returns:
        none
    '''
    #no input

    #process
    #Test 1 - negative dec_num (adding)
    #assuming all the points are set to 20 at first
    if points_tally('Ethos', -10) == 30:
        print('\nTesting the "points_tally()":\nTest 1: Pass')
    else:
        print('\nTesting the "points_tally()":\nTest 1: Fail')
    
    #Test 2 - positive dec_num (subtracting) 
    if points_tally('Ethos', '10') == 'change_decnum_abby':
        print('Test 2: Pass')
    else:
        print('Test 2: Fail')

    #Test 3 - the validity of the attribute parameter
    if points_tally('jojo', 0) == 'change_attributeaffected_abby':
        print('Test 3: Pass')
    else:
        print('Test 3: Fail')

    #output
    print('Test Finished')

#the tests
# test_input_str_checking()
# test_the_inventory()
# test_points_tally()