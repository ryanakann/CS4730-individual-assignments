import io
import os

# data setup
rooms = {
    'floor 1': {
        'bedroom': {
            'objects': {
                'window': {
                    'desc': 'Outside you see a lush landscape, ripe with vast rolling planes and flowers as far as the eye can see. The sun is rishing, shining a glinting light on the empyrean mountain range in the distance.',
                },
                'bed': {
                    'desc': 'It looks reeeeeealy comfy...',
                    'options': [
                        'sleep'
                    ]
                }
            }
        }
    },
    'floor 2': {

    },
    'floor 3': {

    }
}
directions = ['north', 'south', 'east', 'west']
current_room = rooms['floor 1']['bedroom']

index = 0


def intro():
    global name
    while True:
        answer = input("Select your gender (male/female/other): ")
        if answer == 'male' or answer == 'm':
            name = 'Wizard'
            print("""                                                                   
 _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ 
|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|                                                                      
 _   __    __ _                  _ _        ____                 _     _ 
| | / / /\ \ (_)______ _ _ __ __| ( )__    /___ \_   _  ___  ___| |_  | |
| | \ \/  \/ / |_  / _` | '__/ _` |/ __|  //  / / | | |/ _ \/ __| __| | |
| |  \  /\  /| |/ / (_| | | | (_| |\__ \ / \_/ /| |_| |  __/\__ \ |_  | |
| |   \/  \/ |_/___\__,_|_|  \__,_||___/ \___,_\ \__,_|\___||___/\__| | |
|_|                                                                   |_|
 _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ 
|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|                                                                                                                                    
            """)
            break
        elif answer == 'female' or answer =='f':
            name = 'Witch'
            print("""
 _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ 
|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|                                              
 _   __    __ _ _       _    _        ____                 _     _ 
| | / / /\ \ (_) |_ ___| |__( )__    /___ \_   _  ___  ___| |_  | |
| | \ \/  \/ / | __/ __| '_ \/ __|  //  / / | | |/ _ \/ __| __| | |
| |  \  /\  /| | || (__| | | \__ \ / \_/ /| |_| |  __/\__ \ |_  | |
| |   \/  \/ |_|\__\___|_| |_|___/ \___,_\ \__,_|\___||___/\__| | |
|_|                                                             |_|
 _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ 
|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|
            """)
            break
        elif answer =='other' or answer == 'o':
            name = 'Magic Person'
            print("""                                                                                     
 _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____   
|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|                                                                        
 _       __                  _     _                            ____                 _     _ 
| |   /\ \ \___  _ __       | |__ (_)_ __   __ _ _ __ _   _    /___ \_   _  ___  ___| |_  | |
| |  /  \/ / _ \| '_ \ _____| '_ \| | '_ \ / _` | '__| | | |  //  / / | | |/ _ \/ __| __| | |
| | / /\  / (_) | | | |_____| |_) | | | | | (_| | |  | |_| | / \_/ /| |_| |  __/\__ \ |_  | |
| | \_\ \/ \___/|_| |_|     |_.__/|_|_| |_|\__,_|_|   \__, | \___,_\ \__,_|\___||___/\__| | |
|_|                                                   |___/                               |_|  
 _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____   
|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|  
            """)
            break
    wait_for_any()
    text('You are a {name} inside your {name} spire. It is just past dawn, and you arise from your bed, groggy and grumpy. "Where is my cauldron?" you ask yourself. After brief contemplation, you remember you left it in your observatory on the third floor of your spire. Find your way there!'),
    wait_for_any()

def text(s):
    print(s.replace('{name}', name))

def game_loop():
    intro()

def wait_for_any():
    import os
    try:
        os.system("pause")
    except:
        os.system('read -sn 1 -p "Press any key to continue..."')
        print("")

def wait_for_command(key):
    pass

if __name__ == "__main__":
    game_loop()
