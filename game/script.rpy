# Still kind of insane for essentially making this how 
# I come out to a wide group
# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Characters
define b = Character("Basil")
define ca = Character("Classmate A")
define cb = Character("Classmate B")
define bp = Character("Ball Player")
define m = Character("Mom")

# Character Images
image basil default:
    "images/basil/maincharacterv2.png"
    zoom 0.3
    pos (0.0, 1.0)

image basil young:
    "images/basil/childcharacterv2.png"
    zoom 0.3
    pos (0.0, 1.0)

image person: 
    "images/sillouettecharacter_masculine.png"
    zoom 0.3
    pos (0.0, 1.0)

# Background images
image bg black_bg = "images/backgrounds/black_bg.png"
image bg classroom = "images/backgrounds/background_classroom.png" 
image bg bedroom = "images/backgrounds/background_bedroom.png"
image bg park = "images/backgrounds/background_park.png"

default points = 0

# The game starts here.

label start:

    # Start with black screen
    # Color blue represents inner thoughts
    scene bg black_bg
    "{color=#A7C7E7}This thing bubbles up inside me.\n
    I don't know how much longer I can keep going like this...{/color}"

    # Light flicker sound effect goes here
    scene bg bedroom

    show basil default at center
    "???" "Man, I am {i}so TIRED{/i}!"


    "{color=#A7C7E7}Hang on, I haven't introduced myself.
    \nThe name's Basil. Welcome to this bit of my life
    \nin which an import phone call awaits{/color}"

    b "Mom's prolly gonna call any minute. I'm not sure if I can do this."

    b "{color=#A7C7E7}I've been feeling like this about myself at least the past year...
    maybe longer.\nNow that I think it, this hight have been a problem for even longer
    than that."

    call classtime

    scene bg bedroom
    show basil default at center
    b "{color=#A7C7E7}Okay, maybe not that far back! 
    At the very least, I've known that I'm a bit of a pushover,
    a doormat even. Hell, I was known as crybaby.{/color}"
    b "{color=#A7C7E7}I probably still am one, even though sometimes I feel
    like my tears have run dry. I don't have the time to dwell on that, after
    all, I have more a pressing concern.{/color}" 
    
    b "{color=#A7C7E7}If I don't lay this problem to rest, I'm sure it'll kill me.{/color}"

    b "{color=#A7C7E7}It does make sense, growing up and having all of that happen.
    \nLooking at myself in the mirror, and just hating what I, who I saw."

    b "{i}*sigh*{/i} Guess my mind is stuck on {i}that{/i} again."

    b "{color=#A7C7E7}It's not like I wanna think about this. It just bubbles within,
    and scared of it bursting."

    menu action:
        b "{color=#A7C7E7}So..., what now?"
        "Focus on the problem":
            $points = points + 2
        "Think of something else":
            $points = points + 1
            b "Yeah, it's not the biggest deal. Besides I still haven't eaten
            any dinner."
            b "{color=#A7C7E7}Liar. You said that you're sure it'll kill you."
    
    b "{color=#A7C7E7}You do know how this makes you feel. After all,
    don't you remember?"

    b "Right, that did happen. I really don't wanna think about this right now."

    call park
    
    scene bg bedroom
    show basil default at center
    b "{color=#A7C7E7}I'll spare you the details. After that thought,
    I began castrophizing the ramifications of speaking my truth,
    as well as the ramifications of running from my truth."

    b "{color=#A7C7E7}It eventually became too much for me. And so,
    I retreated back a place that is all too familiar to me. This very room."

    b "{color=#A7C7E7}I'm know that my phone is gonna ring any second... I'm scared"

    menu motivation:
        "I'll have to try":
            $points = points + 2
            b "I'll have to try, not for anyone, but for me. It has to be for me, or
            saying it will be meaningless."
        "I'm not sure":
            $points = points + 1
            b "I'm really not sure how this will go, but I really won't know unless
            I try."

    "{i}Ring Ring Ring Ring{/i}"

    menu phone:
        "Pick up":
            if points > 5:
                jump good_end   
            else:
                jump bad_end
        "Ignore":
            jump no_answer

label classtime:
    # background is called here
    # i would assume transition, if made is before call statement
    scene bg classroom
    show basil young at left
    
    ca "Social Studies is so {i}BORING{/i}"
    menu classmate_question:
        cb "True that, what did you think?"
        "I liked it!":
            b "I liked it!"
            #jump class_cont
        "I thought it was okay.":
            b "I thought it was okay."
            #jump class_cont
    ca "Of course you'd saying that! You're such a teacher's pet."
    cb "Yeah, teacher's pet"
    b "I just like learning stuff..."
    ca "Yeah right, you'll probably tell the teacher we think class is boring."
    b "..."
    return
        
label park:
    scene bg park
    show basil default at left
    b "It's pretty nice out today, I needed this. Getting away from there,
    away from there. Even if is for a few hours."

    "*bap*"

    b "Ow! A ball?"

    show person at right
    bp "Hey bro, can you pass me the ball?"

    menu conversation:
        "Bro?":
            $points += 1
            b "Bro?"
            bp "You got problem with me calling you bro?"

            menu conversation_cont:
                "A little":
                    $points += 2
                    b "A little..."
                "...":
                    $points += 1
                    b "..."
            bp "...just give me back the ball."
        "Pass ball":
            b "Here."
    "The passerby gets the ball back"
    hide person

    b "{color=#A7C7E7}And now I have to think about this.
    Being perceived like that, I've been trying to not be seen
    like that. Am I just not trying hard enough?{/color}"

    menu internal_question:
        "Definitely":
            $points += 1
        "Probably":
            $points += 1
    
    b "{color=#A7C7E7}Even if that's the case... I'm WAY too scared to
    make it happen.{/color}"

    b "{color=#A7C7E7}I just don't know if making it happen will make it
    better{/color}"

    return

label good_end:
    hide basil default
    scene bg black_bg
    m "Hello my son! How are you doing this evening"

    b "I'm doing fine, Mom"

    m "We barely hear from you, are you eating?"
    
    b "I am, I just have a lot on my mind"
    b "The thing I have to tell you is, i-is that..."

    "I'm trans."
    "I let it out, I'm not sure what lies ahead, but at the very least, I'm happy its finally out there"
    "{color=#FFB6C1}End.{/color}"
    return

label bad_end:
    hide basil default
    scene bg black_bg
    m "Hello my son! How are you doing this evening"

    b "I'm doing fine, Mom"

    m "We barely hear from you, are you eating?"
    
    b "I am, I just... I just..."
    b "It's nothing, mom, it's nothing. I'm fine."

    b "{color=#A7C7E7}After a conversation catching up about
    stuff that I've missed, it ended just like that"
    b "{color=#A7C7E7}Like watching a bubble prematurely burst, I
    didn't have a chance to speak my truth."
    b "*sob sob* I'm such a coward, I couldn't even let it out."
    "{color=#FFB6C1}End.{/color}"
    return

label no_answer:
    hide basil default
    scene bg black_bg
    b "{color=#A7C7E7}I couldn't even muster the strength to answer...{/color}"
    b "{color=#A7C7E7}The bubble I envisioned floating freely, never had a
    chance to float freely...{/color}"
    b "I'm sorry..."
    "{color=#FFB6C1}End.{/color}"
    return