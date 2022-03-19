from pprint import pprint


import pprint
# pages 104 - 112
# dictionaries
# indexes for dictionaries are called keys

#key-value pairs

myCat = {'size': 'fat', 'color': 'gray', 'disposition':'loud'}
# key:
print(myCat['size'])

#ouput:
# 'fat'

print('my cat has ' + myCat['color'] + ' fur.')
# output:
#'my cat has gray fur.'
spam = { 12345: 'luggage combination', 42: 'the answer' }


# dictionaries are unordered

# example give is that two lists like this
[1,2,3] == [3,2,1]
#returns false
# where as with dictionaries
eggs = { 'name': 'Zophie', 'species': 'cat', 'age': 8 }
ham = {   'age': 8, 'species': 'cat', 'name': 'Zophie' }
# would return true:
eggs == ham 
# true

'name' in eggs 
# is true

# this is false:
'name' not in eggs 

# dictionaries are mutable, there is no "first" in a dictionary

# methods for dictionaries:
# keys(), values, and items()

list(eggs.keys())
#returns:
#['name', 'species', 'age']
# or?
print(list(eggs.keys()))
# oh, above works. can get the same idle output with just a print() 

print(list(eggs.values() ) )
# output
# ['Zophie', 'cat', 8]

print(list(eggs.items() ) )
# output
# [('name', 'Zophie'), ('species', 'cat'), ('age', 8)]
# "returns two item tuples"  which i guess is a thing?

print( eggs.keys() )
# output
# dict_keys(['name', 'species', 'age'])


for k in eggs.keys():
    print(k)
# output:

# name
# species
# age

#similarly for values
for k in eggs.values():
    print(k)

# output:

# Zophie
# cat
# 8

# using two assignment trick
for k, v in eggs.items():
    print(k, v)

# output:

# name Zophie
# species cat
# age 8

# tuples are like lists but immutable and use ( in stead of ) in place of [brackets]

# use of in/not in operator to see if key or value is in dictionary

# this'd return true
#'cat' in eggs.values()

# dictionary get() method

if 'color' in eggs:
    print(eggs['color'])

# get method alternative to above

# test if key 'age' exists and returns 0 if that age test is false
# this is true though since there is an key
eggs.get('age', 0)

# would return blank string
eggs.get('color', '')

picnicItems = { 'apples': 5, 'cups': 2 }
print('I am bringing ' + str(picnicItems.get('napkins', 0)) + ' to the picnic.')
# just outputs 0 since napkins not in the dictionary


# set default dictionary method

#if 'color' not in eggs:
#    eggs['color'] = 'black'

#set default does same in one line
eggs.setdefault('color', 'black')
# output is 'black'

# i guess i can't override that to a different color once that default is set

#character counting program

#message = 'It was a bright cold day in April, and the clocks were striking thirteen'
#count = {} # blank dictionary
# loop through
#for character in message:
#    count.setdefault(character, 0) # start blank dictionary with a 0
#    count[character] = count[character] + 1

#print(count)

# slightly altered version
#message = 'It was a bright cold day in April, and the clocks were striking thirteen'
#count = {}
#for character in message.upper():
 #   count.setdefault(character, 0) # start blank dictionary with a 0; without this get key error
 #   count[character] = count[character] + 1

#print(count)

# the triple quotes, ''', allows for putting quotes around unescaped quotes in strings
message = '''This is a dev log about creating a game called Newtius in GameMaker Studio 2 (Indie edition). Starting with entry one might make this easier to follow.

In entry 13 I tried yet again to do some work with a camera system. I’m not saying it’s still as clear as mud. Maybe marginally clearer than mud.

I think I’m going to do something a little different in this post. But I’ll get back to Newtius more directly eventually.

As always, the official Newtius project page on itch.io is up, featuring the last playable version. Which may or may not have sound since it’s HTML5 (the fix to this turns out is clicking the game in the browser – then the sound works).

A different version of a camera system
I was getting a little frustrated with both the Udemy course and my own side attempt to apply what I was learning from the Udemy course. Recognizing this as part of a learning process I’ve experienced in the past but not wanting to lose momentum, I decided to go on a side adventure with an entirely different tutorial with a game in an entirely different genre. My learning process is more of a zig-zag rather than a straight line.

In this case, I decided to start following the Little Town playlist on YouTube. I started off with the little town page on the YoYo site, (skimming this YoYo page to get an idea what I’m talking about will make below much easier to follow) to get some instructions and download the assets. As a side note may I just say having to go to a separate site – AudioHero – and create/activate a whole new account just to download 15 MP3 files is kind of…obnoxious. Actually having to download a PDF to read instructions on how to click a link, create an account and activate that account when that PDF could have been a web page…is obnoxious in and of itself. These better be the best sound files in existence.

There’s actually six “sessions” to the whole tutorial. Each playlist being 20+ videos a piece, though many of the videos are under five minutes. There is also a companion PDF covering all six sessions as an offline alternative – again no idea why there wouldn’t at least be an option for an HTML file – that I won’t directly link to because I find clicking a link that turns out to be a PDF obnoxious (it’s linked on the little town YoYo page I mentioned).

I played the finished product of little town before starting the walk through and sure, it seems incredibly simple to the point of wondering why you’d bother. But actually it has a lot going on in that thing.

I wanted to dedicate at least a portion of a post to what I thought were some clever approaches and approaches that would never have occurred to me. Also, at least so far the camera system is just through the check boxes in the room properties. So no need to worry about it.

Firstly the control system: it starts out the way a few other GML tutorials have approached it with checking for keypresses in the step event.

But this one is slightly different:

1
2
3
4
5
6
7
8
9
// player object "create" event: establish  Variables
walkSpeed = 16;
vx = 0;
vy = 0;
dir = 3;
moveRight = 0;
moveLeft = 0;
moveUp = 0;
moveDown = 0;
Some programmers might already see where this is going but I’ll just keeping walking through.

He uses a Key Down: Right event for the single line
moveRight = 1;

And then the equivalent for left, up and down Key Down Events for the player object.

For movement, the tutorial uses this in the step event.

1
2
3
4
5
6
7
8
9
10
// First entry into the player object/step event: Calculate movement
vx = (moveRight * walkSpeed);
// If Idle
if (vx == 0) {
// do nothing for now
}
// If moving
if (vx != 0) {
x += vx;
}
So even though the event being worked on is just for when the key is down as opposed to pressed then released – this event still works. And all it’s doing is adding a 1 to the x of the player object (or subtracting 1 for the other direction). I for one thought that was really clever. Maybe not practical for use because of what comes later. But clever. The PDF edition of the this session explains it worlds better than I can ever hope to, but this is the sum up. Eventually he converts all those individual key down events to a switch/case to check for each one and do the calculations. In other words each of the four directions gets a number and a switch loop reacts based on the directions event.

There’s also some things in this first session about editing the room with the uses of a Tile set. Tile sets are something I hope to be able to eventually utilize but have not managed to figure out an excuse for one. And I doubt I could make one from scratch or fix one I downloaded if it didn’t work exactly right. Or maybe I could, I wouldn’t know until I tried.

The next thing I’ll mention – which I’m still trying to wrap my head around – is “depth sorting”.

Okay I think I know what the mans conceptually: some layers are in front of other layers. If you’ve ever used Photoshop, .NET Paint or similar sort of imaged editors with layers you’ve encountered this. It’s this particular author’s implementation of “depth sorting” in so little code and that it works some how that still confuses me. And this is in session one of a six session course.

I’ll attempt to summarize the approach to this simplified depth sorting: he creates a controller or “parent” object called obj_par_environment which he then sets as a parent to a bunch of “environment” objects like barrels, trees, rocks, fences and a few other things.

1
2
3
// Inside of object obj_par_environment Step Event
// put in this one line for Depth sorting:
depth =-y;
This couple of paragraphs covers it:

This takes obj_player’s current y value in the Room (e.g., 500 pixels from the top) and reverses it to assign it a new depth, every step. So as the player moves down in the Room, its depth will change (-500, -501, -502, etc.). As it moves up, it will change in reverse (-500, -499, -498, etc.). This simple trick works well because our game has a top-down view.

However, this only works if we apply the same line of code to all other Objects in our Room for which we want to have correct depth sorting. In our case right now, those are our barrels.

Session one section of “Little Town” PDF (see link)
I think I almost understand what that’s saying and why this works.

This depth sorting code is the entire underlying basis of how collision works in this game from here on. Or through most of session 2, anyway. This works along side custom collision masks to make sure the player looks right relative to standing in front of verses behind a barrel but not working through or over a barrel for instance.

Speaking of which, I think I understand collision masks and origin points that much better now. I mean I know I did before but the comprehension is that much better now since I had to re-adjust a few things to make sure the player character looked right when standing in front of versus behind a fence or barrel.

Well why doesn’t everybody do that?
Back in my early dev log posts – like eight weeks ago – I was having some issues with player objects stopping at edges of the room. Eventually I figured out and it involved calculating the coordinate of the edge of the room along with subtracting a dimension of the player sprite…

Anyway, this game doesn’t do any of that. Instead he takes this 200×200 pixel magenta square, applies the same parent object with the depth sorting, and simply drags the the shape of four of these magenta box to cover the edges of the room. So the player can’t go past these boxes. That’s it.'''

# that's a biggun string
count = {}
for character in message.upper():
    count.setdefault(character, 0) # start blank dictionary with a 0; without this get key error
    count[character] = count[character] + 1

# the pprint module
# or "pretty print"

#print(count)
pprint.pprint(count) # slightly prettier version

# if just wanted to save as a string rather than printing out to the screen
# could use 

rjtext = pprint.pformat(count)
# for instances
# print that out later
print(rjtext)



