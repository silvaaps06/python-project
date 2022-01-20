# Issues to solve: 
# 1. doll image comes to fast. and after it takes a while to continue (not a big problem)
# 2. map image doesn't pop up
# 3. sounds - check them in another computer
# 4. glass corridor room appears as 'glass squares'.. 

# import required modules
import os
import pygame
import time

# define rooms and items

doll = {
    "name": "doll",
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
    "type": "map",
    "target": 'glass_obstacle_door',
}

glass_obstacle = {
    "name": "glass obstacle",
    "type": "obstacle",
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

glass_obstacle_door = {
    "name": "glass obstacle",
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
    "name": "glass corridor room",
    "type": "room",
}

outside = {
  "name": "outside"
}

all_rooms = [court_yard, kitchen, dorm, glass_room, outside]

all_doors = [door_a, security_guard, door_c, door_d, marble_box, glass_obstacle_door]

card_code = 1234
glass_code = 100110

# define which items/rooms are related

object_relations = {
    "court yard": [doll, door_a],
    "doll": [key_a],
    "kitchen" : [stove, door_a, security_guard, door_c],
    "stove": [cookie_b],
    'gamers dorm' : [bunk_bed1, bunk_bed2, security_guard],
    'second bunkbed' : [key_c],
    'glass corridor room' : [door_d, glass_obstacle, marble_box],
    "door a": [court_yard, kitchen],
    "security guard": [kitchen, dorm],
    "door c": [kitchen, glass_room],
    "door d": [glass_room, outside],
    "box with marbles" : [map],
    "glass obstacle" : [],
    "outside": [door_d]
}

# define game state. Do not directly change this dict. 
# Instead, when a new game starts, make a copy of this
# dict and use the copy to store gameplay state. This 
# way you can replay the game multiple times.



INIT_GAME_STATE = {
    "current_room": court_yard,
    "keys_collected": [],
    "maps_collected": [],
    "target_room": outside
}



def im(obj):
    #pwd_path= os.path.dirname(os.path.abspath(__file__))
    #path = os.path.join(pwd_path, str(obj) + '.png')
    pygame.init()
    # define the RGB value
    # for white colour
    white = (255, 255, 255)
    running = True
    # assigning values to X and Y variable
    X = 600
    Y = 600
    # create the display surface object
    # of specific dimension..e(X, Y).
    display_surface = pygame.display.set_mode((X, Y ))
    # set the pygame window name
    #pygame.display.set_caption(str(obj))
    # create a surface object, image is drawn on it.
    wanted_image = pygame.image.load(obj)
    # infinite loop
    #x = 10
    while running :
        # completely fill the surface object
        # with white colour
        display_surface.fill(white)
        # copying the image surface object
        # to the display surface object at
        # (0, 0) coordinate.
        display_surface.blit(wanted_image, (0, 0))
        pygame.display.update()
        # iterate over the list of Event objects
        # that was returned by pygame.event.get() method.
        #for event in pygame.event.get() :
            # if event object type is QUIT
            # then quitting the pygame
            # and program both.
            #if event.type == pygame.QUIT :
                # deactivates the pygame library
                #pygame.quit()
                # quit the program.
                #quit()
            # Draws the surface object to the screen.
        time.sleep(5)
        running = False
        pygame.quit()
        break
        
        #x = x - 1

def linebreak():
    """
    Print a line break
    """
    print("\n\n")


def start_game():
    """
    Start the game
    """
    print("You feel cold and wake you in a courtyard where you've never been before.") 
    print("You see a creepy doll in the middle of the courtyard. She has a card: remember what the card says!")
    
    im('cardcode_im.png')
    time.sleep(3)
    play_room(game_state["current_room"])


def play_room(room):
    """
    Play a room. First check if the room being played is the target room.
    If it is, the game will end with success. Otherwise, let player either 
    explore (list all items in this room) or examine an item found here.
    """
    game_state["current_room"] = room
    if(game_state["current_room"] == game_state["target_room"]):
        print("Congrats! You've just won Squid Game!")
        # play sound
        file1 = "win_sound.wav"
        os.system("afplay " + file1)
        

    else:
        print("You are now in " + room["name"])
        intended_action = input("What would you like to do? Type '1' to explore or '3' to examine?").strip()
        if intended_action == "1":
            
            if room['name'] == 'court yard':
                im('courtyard_im.png')
            elif room['name'] == 'kitchen':
                im('coockie.png')
            elif room['name'] == 'gamers dorm':
                im('dorm_room.png')
            elif room['name'] == 'glass corridor room':
                im('glass_room.png')

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

                submitted_card_code = int(input("Enter a four-digit code: "))
                while submitted_card_code != card_code:
                    print('Sorry, the code is incorrect, you have another try')
                    submitted_card_code = int(input("Enter a four-digit code: "))
                
                if submitted_card_code == card_code:
                    print('The code is correct! The box opens and you find a map inside, which is a solution to go through the glass corridor safely')
                    game_state["maps_collected"].append('map') 
                    im('mapglass_im.png')
                    
            elif (item["type"] == "obstacle"):
                if 'map' in game_state["maps_collected"]:
                    print('You have to walk on the glass corridor to reach the door.')
                    submitted_glass_code = int(input("Enter the code you get in the map to walk the glass corridor: "))
                    while submitted_glass_code != glass_code:
                        print('Ops, you stepped on the wrong square. You can try once again')
                        submitted_glass_code = int(input("Enter the code to walk the glass corridor: "))
                    if submitted_glass_code == glass_code:
                        game_state["keys_collected"].append(key_d)
                        print('Good job! You got to end of the glass corridor and you receive a key as a gift')

                else:
                    print('Sorry, you can not access the glass corridor. You need to find a map to walk the corridor.')    
    

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
    
    if(next_room and input("Do you want to go to the next room? Enter 'y' for yes or 'n' for no").strip() == 'y'):
        # play sound
        file1 = "door_sound.wav"
        os.system("afplay " + file1)
        play_room(next_room)
    else:
        play_room(current_room)
        
        
game_state = INIT_GAME_STATE.copy()

start_game()

