# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define char = Character("???")

default points = 0



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show char happy

    # These display lines of dialogue.

    char "You've created a new Ren'Py game."

    char "Once you add a story, pictures, and music, you can release it to the world!"

    
    "{i}Ring Ring Ring Ring{/i}"
    
    if points > 5:

        jump good_end
    
    else:

        jump bad_end

label good_end:
    char "The thing I have to tell you is that..."
    return

label bad_end:
    char "It's nothing, mom. Don't worry about it"
    return
