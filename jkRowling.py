from random import randint
tweetType = randint(0,5)
d1 = (randint(0, 20))
HP1 = (randint(1, 22))
excuse1 = (randint(0, 5))
if d1 == 0:
    if tweetType > 2 and tweetType < 5:
        d = "homosexuality"
    elif tweetType < 3 or tweetType == 5:
        d = "gay"
elif d1 == 1:
    if tweetType > 2 and tweetType < 5:
        d = "a social anxiety disorder"
    elif tweetType < 3 or tweetType == 5:
        d = "socially anxious"
elif d1 == 2:
    if tweetType > 2 and tweetType < 5:
        d = "autism"
    elif tweetType < 3 or tweetType == 5:
        d = "autistic"
elif d1 == 3:
    if tweetType > 2 and tweetType < 5:
        d = "crippled legs"
    elif tweetType < 3 or tweetType == 5:
        d = "in a wheelchair"
elif d1 == 4:
    if tweetType > 2 and tweetType < 5:
        d = "severe mental issues"
    elif tweetType < 3 or tweetType == 5:
        d = "mentally disabled"
elif d1 == 5:
    if tweetType > 2 and tweetType < 5:
        d = "depression"
    elif tweetType < 3 or tweetType == 5:
        d = "depressed"
elif d1 == 6:
    if tweetType > 2 and tweetType < 5:
        d = "anorexia"
    elif tweetType < 3 or tweetType == 5:
        d = "anorexic"
elif d1 == 7:
    if tweetType > 2 and tweetType < 5:
        d = "social anxiety"
    elif tweetType < 3 or tweetType == 5:
        d = "socially anxious"
elif d1 == 8: 
    if tweetType > 2 and tweetType < 5:
        d = "bisexuality"
    elif tweetType < 3 or tweetType == 5:
        d = "bisexual"
elif d1 == 9:
    if tweetType > 2 and tweetType < 5:
        d = "PTSD"
    elif tweetType < 3 or tweetType == 5:
        d = "suffering from PTSD"
elif d1 == 10:
    if tweetType > 2 and tweetType < 5:
        d = "gender dysphoria"
    elif tweetType < 3 or tweetType == 5:
        d = "gender dysphoric"
elif d1 == 11:
    if tweetType > 2 and tweetType < 5:
        d = "african american ancestors"
    elif tweetType < 3 or tweetType == 5:
        d = "african american"
elif d1 == 12:
    if tweetType > 2 and tweetType < 5:
        d = "gender fluidity"
    elif tweetType < 3 or tweetType == 5:
        d = "gender fluid"
elif d1 == 13:
    if tweetType > 2 and tweetType < 5:
        d = "hispanic ancestors"
    elif tweetType < 3 or tweetType == 5:
        d = "hispanic"
elif d1 == 14:
    if tweetType > 2 and tweetType < 5:
        d = "parents of mixed race"
    elif tweetType < 3 or tweetType == 5:
        d = "multiracial"
elif d1 == 15:
    if tweetType > 2 and tweetType < 5:
        d = "no gender"
    elif tweetType < 3 or tweetType == 5:
        d = "non-binary"
elif d1 == 16:
    if tweetType > 2 and tweetType < 5:
        d = "down syndrome"
    elif tweetType < 3 or tweetType == 5:
        d = "troubled with down syndrome"
elif d1 == 17:
    if tweetType > 2 and tweetType < 5:
        d = "cereberal palsy"
    elif tweetType < 3 or tweetType == 5:
        d = "faced with cereberal palsy"
elif d1 == 18:
    if tweetType > 2 and tweetType < 5:
        d = "ADHD"
    elif tweetType < 3 or tweetType == 5:
        d = "facing issues with ADHD throughout the books"
elif d1 == 19:
    if tweetType > 2 and tweetType < 5:
        d = "been blessed with demiagender"
    elif tweetType < 3 or tweetType == 5:
        d = "demiagender"
elif d1 == 20:
    if tweetType > 2 and tweetType < 5:
        d = "arabic parents"
    elif tweetType < 3 or tweetType == 5:
        d = "arabic"        

if HP1 == 1:
    HP = "Harry"
elif HP1 == 2:
    HP = "Hermionie"
elif HP1 == 3:
    HP = "Ron"
elif HP1 == 4:
    HP = "Dumbledore"
elif HP1 == 5:
    HP = "Hagrid"
elif HP1 == 6:
    HP = "Luna Lovegood"
elif HP1 == 7:
    HP = "Voldemort"
elif HP1 == 8:
    HP = "Draco"
elif HP1 == 9:
    HP = "Snape"
elif HP1 == 10:
    HP = "Crabbe"
elif HP1 == 11:
    HP = "Goyle"
elif HP1 == 12:
    HP = "Dobby"
elif HP1 == 13:
    HP = "Neville"
elif HP1 == 14:
    HP = "Hedwig"
elif HP1 == 15:
    HP = "Ginny"
elif HP1 == 16:
    HP = "Sirius"
elif HP1 == 17:
    HP = "Viktor Krum"
elif HP1 == 18:
    HP = "Cornelius Fudge"
elif HP1 == 19:
    if tweetType > 4:
        HP = "The Sorting Hat"
    else:
        HP = "the Sorting Hat"
elif HP1 == 20:
    HP = "Dudley"
elif HP1 == 21:
    HP = "Fred"
elif HP1 == 22:
    HP = "George"

if excuse1 == 0:
    excuse = "To those of you who call me a liar, I have one question: did you write the Harry Potter books?"
elif excuse1 == 1:
    excuse = "I think that some readers just weren't able to read into the story well enough."
elif excuse1 == 2:
    excuse = "If you reread the books, you'll find subtle hints to show that I really did write " + HP + " that way."
elif excuse1 == 3:
    excuse = "It's just that some of you don't understand that an author could be woke in the 90s."
elif excuse1 == 4:
    excuse = "Just because you don't agree with my political opinions doesn't mean you have to criticize my plans for my characters."
else:
    if tweetType > 2 and tweetType < 5:
        excuse = "You're homophobic and racist if you don't think that " + HP + " had " + d
    elif tweetType < 3 or tweetType == 5:
        excuse = "You're homophobic and racist if you don't think that " + HP + " was actually " + d
if tweetType == 0:
    print(HP + " was actually " + d + " all along. " + excuse)
elif tweetType == 1:
    print("I actually intended for " + HP + " to be " + d + " from the start.")
elif tweetType == 2:
    print("When I wrote the books, I made sure that " + HP + " was " + d + ".")
elif tweetType == 3:
    print("I'll just say it. " + HP + " has " + d + ".")
elif tweetType == 4:
    print("Some of you seem to think that I was lying when I said that " + HP + " had " + d + ". " + excuse)
else:
    print(HP + " is " + d)