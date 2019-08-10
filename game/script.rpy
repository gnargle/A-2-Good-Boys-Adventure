# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define g = Character("Guy", color = "#b603fc", image = "guy")
define gh = Character("Guy's Head", color = "#b603fc")
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

label chippy:

    scene bg black
    with fade

    centered "There'd be a fancy title screen here if I could do graphic design"

    centered "Just imagine it's like 2 Good Boys but in the JoJo font"

    stop music fadeout 3.0

    scene bg chippy
    with fade

    window auto

    show guy left at left with dissolve

    g "Aye, a lovely fish supper. That'll do us right."

    g "Haud on, what the fuck?"

    show thistle right at center with moveinright

    t "Awrite?"

    show barry right at right with dissolve

    b "Whit's the Partick Thistle doing at the chippy?"

    g "Here, everyone's got to eat! Even that cunt."

    t "Fuckin', GUY WOODWARD."

    t "Guy FUCKING Woodward!"

    g "Whit?"

    t "I'm coming for you, Woodward. I want what you have."

    g "I work in a hairdressers with the daftest customers alive, man, I'm no sure you really want that."

    t "I will become a good boy. The good boy."

    b "Awrite now, away and shite. This is nonsense."

    t "You just fuckin' wait."

    show thistle right at offscreenright with moveoutright

    "[[The Partick Thistle dashes off to god knows where.]"

    g "..."

    b "..."

    g "So youse wanting cod or haddock?"    

label end:

    show bg eog with fade

    play music "music/kommsussertod.mp3"

    hide guy

    show barry right at right with dissolve

    b "I didn't really see it ending up like this."

    gh "Aye, me neither."

    b "So what's it gonna be? Still doing the podcast?"

    gh "Not sure I can fit in the recording room, let's be honest here."

    b "It's awrite, I'll bring the mic to you. We can get a big one with the Patreon money."

    gh "There's a thought, with everyone soup, nobody can cancel their pledges."

    b "Do you think people will come back?"

    gh "Ah hate this and I came back."

    gh "Maybe some people like to be free of the pain of existence, I dunno. Not having to worry about money was awrite, for a bit."

    gh "Nae shagging, though."

    b "We've got a chance to start again. So."

    b "Series five?"

    hide barry

    window hide

    show bg black with fade

    centered "A stupid game about a much better podcast by @AtheneAllen."

    centered "The fact that I even took time to make this should tell you how greate 2 Good Boys is."

    centered "Anyway."

    centered "See ya."
    # This ends the game.

    return
