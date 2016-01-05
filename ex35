from sys import exit

def gold_room():
    print 'This room is full of gold. I think it\'s close to $10,000,000! How much will you take?' #Study Drill 4
    
    next = raw_input ('> ')
    # if int(next) == True:
    # if '0' in next or '1' in next:
    
    if int(next): #Study Drill 5
        how_much = int(next)
        if how_much < 5000000:
            print "Nice, you're not greedy, you win!"
            exit (0)
        else:
            dead('You greedy bastard!')
    else:
        dead('Man, learn to type a number.')
        
def bear_room():
    print 'There is a fat bear here.'
    print 'He has a jar of honey.'
    print 'The bear is in front of the door.'
    print 'How are you going to move the bear?'
    bear_moved = False
    
    while True:
        next = raw_input('> ')
                
        if ('take' or 'honey') in next:
            dead ('The bear looks at you then slaps your face off.')
        elif next == 'taunt bear' and not bear_moved: # not bear_moved = not False = True
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif next == 'taunt bear' and bear_moved: # This will only run if 'taunt bear' was written because that's when bear_moved = True.
            dead('The bear gets pissed off and chews your leg off.')
        elif next == "open door" and bear_moved: # This will only run if 'taunt bear' was written because that's when bear_moved = True.
            gold_room()
        else:
            print 'I got no idea what that means.'

def cthulhu_room():
    print 'Here you see the great evil Cthulhu.'
    print 'He, it, whatever, stares at you and you go insane.'
    print 'Do you flee for your life or eat your head?'
    
    next = raw_input('> ')
    
    if 'flee' in next:
        start ()
    elif 'head' in next:
        dead ('Well that was tasty!')
    else:
        cthulhu_room()

def dead(why):
    ''' This function is to exit the game because the player died.''' # Study Drill 3 (just to remember what doc comment is)
    print why, 'Good job!'
    exit (0)
    
def start():
    print 'You are in a dark room.'
    print 'There are doors on your right and left.'
    print 'Which one do you take?'
    
    next = raw_input('> ')
    
    if 'l' in next:
        bear_room()
    elif 'r' in next:
        cthulhu_room()
    else:
        dead('You stumble around the room until you starve.')
        
start()
