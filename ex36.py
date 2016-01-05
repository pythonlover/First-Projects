''' TODO
- the if statements with lots of words don't work so fix them:
    - Idea: put the words in a list. Loop over it and check if it's in the variable.
'''
from sys import exit
from time import sleep #To stop the rest from printing while the player reads.
from random import randint #To prevent the game from being predictable.
from subprocess import call #To clear the screen.
from platform import system #To check the platform to know what command to run to clear the screen.

p = '\n>>> '

def Platform(): #Check what platform it is and return the corresponding clear shell command.
    cur_system = system()
    if cur_system == 'Windows':
        cmd = 'cls'
    else:
        cmd = 'clear'
    return cmd
    
def countdown(sec):
    number = sec + 1 #so it works in range
    seconds = sorted(range(1,number), reverse = True) # Create a list of seconds.
    
    for num in seconds: #Countdown
        print '\a%r' %num
        sleep(1)
        
def start():
    print """
    This is an adventure game. The story will play out and
    you will be asked to make all the big decisions so pay attention.
    Have Fun.
    """
    sleep(8)
    
    cmd = Platform()
    call(cmd, shell = True) # Clear the screen. 
    
    countdown(5)
    
    print "\nThe government is trying to implant software in human"
    print "brains. You can see everyone around you walking in a row."
    print "They all look sleepy so you decide to run out."; sleep(7)
    
    print "\nYou're in a cave."
    print "You can here someone running towards you."
    print "It's dark but you can make out",
    print "tunnels on your right and left."; sleep(7)
    
    print "On your right, you can hear a train whistle."; sleep(3)
    print "On your left, you can't hear anything."; sleep(3)
    print "\nWhich one do you take?"
    
    tunnel = raw_input(p)
    
    if 'right' in tunnel or 'train' in tunnel:
        train()
    elif 'left' in tunnel:
        jungle()
    elif 'back' in tunnel or 'stay' in tunnel:
        dead("Agents came and took you back.")
    else:
        print "I guess you don't wanna play."
        print "I'll give you another game."
        print "Opening 'ex35.py'..."
        countdown(10)
        import ex35 # Just for Study Drill, otherwise it ruins the story.
        dead('')
        
def train():
    print "You finally get out of the tunnel."
    print "You see a train now and robots moving something onto the train."
    print "Don't worry these robots can't see you.",
    print "But someone's running towards you."
    
    train = raw_input(p)
    
    if 'on' or 'in' or 'hide' in train:
        print "From your position. You see who was running towards you."
        print "These guys look like secret agents."
        print "They're all wearing suits and you can see some have a gun."
        print "'We can't let that idiot get away,",
        print "it's gonna ruin the bosses plans. We'll look in every cartridge" # I couldn't remember the right word will change it
        print "if we have to!' says one of the guys. He looks scary."
        print "You can see another train over there that's about to leave."
        print "What should you do?"
        run = raw_input(p)
        
        if 'get on' or 'go to' or '2nd' or 'second' in run:
            print "The train starts to move and you run out out of your spot."
            print "One of the agents spots you and starts to shoot at you."
            move = raw_input(p)
            
            if 'jump on' in move:
                print "You got on the train on time."
                end()
            else:
                dead("You got caught.")
        
        elif 'hide' in run or 'stay' in run:        
            dead("I haven't programmed what will happen in next yet. Bye")
    else:
        train()
        
def jungle():
    print "You turn around and look back at the tunnel entrance."
    print "You got out a while ago."
    print "Despite the dense jungle you're in the entrance is visible."
    print "You here a chanting. It's going to be dark soon."
    print "You go over to the chanting and see multiple boats."
    
    find_boat = randint(0 or 1) # 0 is False
                                # 1 is True
    while True:
        next = raw_input(p)
        
        if ('take' or 'boat' or 'get in' or 'get on') in next and find_boat:
            print "You goat on the boat safely and got away."
            end()
        elif ('run' or 'steal') in next:
            dead("%r wasn't a good idea. You got shot." %next)
        elif find_boat == False:
            dead("You couldn't find an empty boat. You got caught.")
        else:
            print "I got no idea what that means."
            
def end():
    sleep(5)
    print "\n\n\nA while later..."
    print "You see a mountain of gold on one side."
    print "And the way back home the other."
    print "Where do you go?"
    end = raw_input(p)
    
    if ('gold' or 'mountain' or 'money') in end:
        dead("""
        You get to live on a beautiful Island with lots of,
        good looking people for the rest of your life.
        """)
    elif ('home' or 'back') in end:
        dead("Purchase Part. 2 of the story for what follows.")
    else:
        print "I don't understand."
        end()

def dead(why):
    print why
    exit(0)

def main():
    start()

if __name__ == '__main__':
    main()
