# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define g = Character("Guy", color = "#b603fc")
define b = Character("Barry", color = "#009933")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    "18:07, Barry's Podcasting Lounge"

    scene bg podcast

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show guy idle at left
    show barry idle at right

    play music "music/roundabout.mp3" fadeout 3.0

    # These display lines of dialogue.

    b "..And thanks for listening to the fourth series of 2 Good Boys. The juice is thicker than ever."

    b "I have been Barry Topping. I'm a good boy."

    g "I was Guy Woodward. Am a good boy."

    "[[Barry hits stop on the big podcast machine.]"

    g "Chippy?"

    b "I dunno, I was wanting a munchy box, man."

    g "Let's away and wander, see what takes our fancy."

    "Little did the 2 Good Boys know, but this decision would put the fate of the podcast in utmost peril..."


    # This ends the game.

    return
