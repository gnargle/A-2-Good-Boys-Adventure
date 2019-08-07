# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define g = Character("Guy")
define b = Character("Barry")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg podcast

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show guy happy

    play music "music/roundabout.mp3" fadeout 3.0

    # These display lines of dialogue.

    b "...the Cow Gun."

    b "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
