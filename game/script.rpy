# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define g = Character("Guy", color = "#b603fc", image = "guy")
define b = Character("Barry", color = "#009933", image = "barry")
define t = Character("Partick Thistle", color = "#ffcc00", image = "thistle")


# The game starts here.

label start:

    window hide

    scene bg black

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    centered "{cps=4}18:07, Barry's Podcasting Lounge{/cps}"

    scene bg podcast 
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show barry right at right with dissolve

    play music "music/roundabout.mp3" fadeout 3.0

    window auto

    # These display lines of dialogue.

    b "..And thanks for listening to the fourth series of 2 Good Boys. The juice is thicker than ever."

    b "I have been Barry Topping. I'm a good boy."

    show guy left at left with dissolve

    g "I was Guy Woodward. Am a good boy."

    "[[Barry hits stop on the big podcast machine.]"

    g "Chippy?"

    b "I dunno, I was wanting a munchy box, man."

    g "Let's away and wander, see what takes our fancy."

    "Little did the 2 Good Boys know, but this decision would put the fate of the podcast in utmost peril..."

    window hide

    scene bg black
    with fade

    centered "There'd be a fancy title screen here if I could do graphic design"

    centered "Just imagine it's like 2 Good Boys but in the JoJo font"

    scene bg chippy
    with fade

    window auto

    show guy left at left with dissolve

    g "Aye, a lovely fish supper. That'll do us right."

    g "Haud on, what the fuck?"

    show thistle right at right with moveinright

    t "Awrite?"
    # This ends the game.

    return
