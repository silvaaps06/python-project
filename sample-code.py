# define rooms and items

doll = {
    "name": "creepy doll",
    "type": "furniture",
}

stove = {
    "name": "stove",
    "type": "furniture",
}

bunk_bed1 = {
    "name": "first bunkbed",
    "type": "furniture",
}

bunk_bed2 = {
    "name": "second bunkbed",
    "type": "furniture",
}

marble_box = {
    "name": "box with marbles",
    "type": "box",
}

map = {
    "name": "solution for going through the glass obstacle",
    "type": "image",
}

glass_obstacle = {
    "name": "glass obstacle",
    "type": "furniture",
}

door_a = {
    "name": "door a",
    "type": "door",
}

security_guard = {
    "name": "security guard",
    "type": "doorman",
}

door_c = {
    "name": "door c",
    "type": "door",
}

door_d = {
    "name": "door d",
    "type": "door",
}

key_a = {
    "name": "key for door a",
    "type": "key",
    "target": door_a,
}

cookie_b = {
    "name": "cookie for the security guard",
    "type": "key",
    "target": security_guard,
}

key_c = {
    "name": "key for door c",
    "type": "key",
    "target": door_c,
}

key_d = {
    "name": "key for door d",
    "type": "key",
    "target": door_d,
}

#TO USE IF WE CANT MAKE CODE
# key_box = {
#   "name": "misterious key",
#   "type": "key",
#   "target": marble_box,
#}

court_yard = {
    "name": "court yard",
    "type": "room",
}

kitchen = {
    "name": "kitchen",
    "type": "room",
}

dorm = {
    "name": "gamers dorm",
    "type": "room",
}

glass_room = {
    "name": "glass corridor",
    "type": "room",
}

outside = {
  "name": "outside"
}

all_rooms = [court_yard, kitchen, dorm, glass_room, outside]

all_doors = [door_a, security_guard, door_c, door_d, marble_box]

card_code = 1234

# define which items/rooms are related

object_relations = {
    "court yard": [doll, door_a],
    "creepy doll": [key_a],
    "kitchen" : [stove, door_a, security_guard, door_c],
    "stove": [cookie_b],
    'gamers dorm' : [bunk_bed1, bunk_bed2, security_guard],
    "first bunkbed": [key_c],
    'second bunkbed' : [key_d],
    'glass corridor' : [door_d,glass_squares,marble_box],
    "door a": [court_yard, kitchen],
    "security guard": [kitchen, dorm],
    "door c": [kitchen, glass_squares],
    "door d": [glass_squares, outside],
    "box with marbles" : [map],
    "outside": [door_d]
}

# define game state. Do not directly change this dict. 
# Instead, when a new game starts, make a copy of this
# dict and use the copy to store gameplay state. This 
# way you can replay the game multiple times.

import PIL

INIT_GAME_STATE = {
    "current_room": court_yard,
    "keys_collected": [],
    "target_room": outside
}

def linebreak():
    """
    Print a line break
    """
    print("\n\n")

import pygame
import time
# activate the pygame library .
# initiate pygame and give permission
# to use pygame's functionality.

def im(obj):

    path = '/Users/AnaPSilva/Documents/Ana/Ironhack/Bootcamp/Week1/Project1/python-project/' + str(obj) + '.png'
    pygame.init()
    # define the RGB value
    # for white colour
    white = (255, 255, 255)

    # assigning values to X and Y variable
    X = 1328
    Y = 887
    # create the display surface object
    # of specific dimension..e(X, Y).
    display_surface = pygame.display.set_mode((X, Y ))
    # set the pygame window name
    pygame.display.set_caption(str(obj))
    # create a surface object, image is drawn on it.
    wanted_image = pygame.image.load(path)
    # infinite loop
    x = 10
    while x :
        # completely fill the surface object
        # with white colour
        display_surface.fill(white)
        # copying the image surface object
        # to the display surface object at
        # (0, 0) coordinate.
        display_surface.blit(wanted_image, (0, 0))
        # iterate over the list of Event objects
        # that was returned by pygame.event.get() method.
        for event in pygame.event.get() :
            # if event object type is QUIT
            # then quitting the pygame
            # and program both.
            if event.type == pygame.QUIT :
                # deactivates the pygame library
                pygame.quit()
                # quit the program.
                quit()
            # Draws the surface object to the screen.
            pygame.display.update()
        time.sleep(1)
        x = x - 1

# import required module
import os

def start_game():
    """
    Start the game
    """
    print("You feel cold and wake you in a court yard that you've never been before. You notice you have a card in your hand that reads: ")
    im('card_im')
    play_room(game_state["current_room"])

def play_room(room):
    """
    Play a room. First check if the room being played is the target room.
    If it is, the game will end with success. Otherwise, let player either 
    explore (list all items in this room) or examine an item found here.
    """
    game_state["current_room"] = room
    if(game_state["current_room"] == game_state["target_room"]):
        # play sound
        file1 = "win_sound.wav"
        os.system("afplay " + file1)
        print("Congrats! You've just won Squid Game!")
    else:
        print("You are now in " + room["name"])
        intended_action = input("What would you like to do? Type '1' to explore or '3' to examine?").strip()
        if intended_action == "1":
            explore_room(room)
            play_room(room)
        elif intended_action == "3":
            examine_item(input("What would you like to examine?").strip())
        else:
            print("Not sure what you mean. Type '1' or '3'.")
            play_room(room)
        linebreak()

def explore_room(room):
    """
    Explore a room. List all items belonging to this room.
    """
    items = [i["name"] for i in object_relations[room["name"]]]
    print("You explore the room. This is " + room["name"] + ". You find " + ", ".join(items))

def get_next_room_of_door(door, current_room):
    """
    From object_relations, find the two rooms connected to the given door.
    Return the room that is not the current_room.
    """
    connected_rooms = object_relations[door["name"]]
    for room in connected_rooms:
        if(not current_room == room):
            return room



def examine_item(item_name):
    """
    Examine an item which can be a door, furniture or a box to be opened.
    First make sure the intended item belongs to the current room.
    Then check if the item is a door. Tell player if key hasn't been 
    collected yet. Otherwise ask player if they want to go to the next
    room. If the item is not a door, then check if it contains keys.
    Collect the key if found and update the game state. At the end,
    play either the current or the next room depending on the game state
    to keep playing.
    """
    current_room = game_state["current_room"]
    next_room = ""
    output = None
    

    for item in object_relations[current_room["name"]]:
        if(item["name"] == item_name):
            output = "You examine " + item_name + ". "
            if(item["type"] == "door"):
                have_key = False
                for key in game_state["keys_collected"]:
                    if(key["target"] == item):
                        have_key = True
                if(have_key):
                    output += "You unlock it with a key you have."
                    next_room = get_next_room_of_door(item, current_room)
                else:
                    # play sound
                    file1 = "nodoor_sound.wav"
                    os.system("afplay " + file1)
                    output += "It is locked but you don't have the key."
            elif(item["type"] == "doorman"):
                have_key = False
                for key in game_state["keys_collected"]:
                    if(key["target"] == item):
                        have_key = True
                if(have_key):
                    output += "You bribe the security guard with the cookie you found. He was happy and let you through the door."
                    next_room = get_next_room_of_door(item, current_room)
                else:
                    output += "The security guard doesn't let you in."

            elif (item["type"] == "box"):
                print("The box needs a code to be unlocked. You might already have seen it")

                submitted_code = int(input("Enter a four-digit code: "))
                while submitted_code != card_code:
                    print('Sorry, the code is incorrect, you have another try')
                    submitted_code = int(input("Enter a four-digit code: "))
                
                if submitted_code == card_code:
                    print('The code is correct! The box opens and you find a map inside, which is a solution to go through the glass corridor safely')
                    im('mapglass_im')
                    print('The map image goes here')
            else:
                if(item["name"] in object_relations and len(object_relations[item["name"]])>0):
                    item_found = object_relations[item["name"]].pop()
                    game_state["keys_collected"].append(item_found)
                    output += "You find " + item_found["name"] + "."
                else:
                    output += "There isn't anything interesting about it."
            print(output)
            break

    if(output is None):
        print("The item you requested is not found in the current room.")
    
    if(next_room and input("Do you want to go to the next room? Enter 'yes' or 'no'").strip() == 'yes'):
        # play sound
        file1 = "door_sound.wav"
        os.system("afplay " + file1)
        play_room(next_room)
    else:
        play_room(current_room)
        
        
game_state = INIT_GAME_STATE.copy()

start_game()

