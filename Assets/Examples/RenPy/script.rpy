﻿# This is a comment, comments are only seen when looking at the script itself.
# This file contains the script for the Unity Raconteur demo. 
# Execution starts at the start label.

# Labels have blocks of text associated with them. Keep a look at for labels below.

# The game starts here.
#begin start
label start:

    #end start

    # Start the background music playing.
    play music "theme.ogg"

    #window show

    r "Hello, my name is Raconteur. Welcome to the Unity Raconteur tutorial."
    r "In this tutorial, you'll learn some basics of Ren'Py and how they interact with Unity."
    r "Pick from the options below to learn about how to use Raconteur."

    menu:
        "Structure of Ren'Py Scripts - How sections and non-linear progression works.":
            jump scriptstructure
        "Using Images and Sound - Help tell your story with images and sound.":
            jump imagesound
        "Basic Script Commands - Helpful tools for transitions.":
            jump commands
        "Variables and Control Structures - How to make choices and control the flow of the story.":
            jump variables
        "What is Ren'Py?":
            jump renpy
        "I'm finished here,":
            jump end

label mainmenu:

    $ story_started = False

    r "Welcome back to the main menu, what do you want to learn?"

    menu:
        "Structure of Ren'Py Scripts - How sections and non-linear progression works.":
            jump scriptstructure
        "Using Images and Sound - Help tell your story with images and sound.":
            jump imagesound
        "Basic Script Commands - Helpful tools for transitions.":
            jump commands
        "Variables and Control Structures - How to make choices and control the flow of the story.":
            jump variables
        "What is Ren'Py?":
            jump renpy
        "I'm finished here.":
            jump end

label scriptstructure:

    r "Scripts in Ren'Py are made up of lines."
    r "Labels group up lines in blocks."
    r "The line you're reading now is actually part of a block inside a label."
    r "I don't really have choice in what I say."
    r "Once I hit a label, I say everything inside the block. Who needs free will?"

    menu:
        "Tell me more about labels.":
            jump labels
        "I'm finished here.":
            jump mainmenu

label labels:

    r "Labels are used to divide a script into sections."
    r "They also allow non-linear progression through these sections. Let's try an example."
    r "I'm going to tell you a short story, and you can decide how you want to hear it."

    menu:
        "Tell me the start of the story.":
            jump startstory
        "Tell me the end of the story.":
            jump endstory
        "I'm finished here.":
            jump mainmenu

label startstory:


    r "The hero did not eat a very good breakfast."

# If the player started the story before this label, show this extra line
    if story_started
    r "See? Labels can create non-linear storytelling hrough the jump command. Check the comments to understand jump."

    $ story_started = True

# Notice that here we set the variable to true after checking, so that the player won't see the text
# The first time around

# Notice that the jump command changes to the label specified, a real jump!
    menu:
        "Tell me the end of the story.":
            jump endstory
        "I'm finished here.":
            jump mainmenu

label endstory:

    r "So she did not vanquish the dragon."

# If the player started the story before this label, show this extra line
    if story_started
    r "See? Labels can create non-linear storytelling hrough the jump command. Check the comments to understand jump."

    $ story_started = True

# Notice that here we set the variable to true after checking, so that the player won't see the text
# The first time around

# Notice that the jump command changes to the label specified, a real jump!
    menu:
        "Tell me the start of the story.":
            jump startstory
        "I'm finished here.":
            jump mainmenu

label imagesound:

    r "Section on images and sound TODO"

    menu:
        "I'm finished here.":
            jump mainmenu

label commands:

    r "Section on commands TODO."

    menu:
        "I'm finished here.":
            jump mainmenu

label variables:

    r "Section on variables TODO"

    menu:
        "I'm finished here.":
            jump mainmenu

label renpy:

    r "Ren'Py is a visual novel engine that helps you use words, images, and sounds to tell stories with the computer."
    r "These can be both visual novels and life simulation games. The easy to learn script language allows you to efficiently write large visual novels, while its Python scripting is enough for complex simulation games."

    menu:
        "I'm finished here.":
            jump mainmenu

label end:

    r "Thanks for joining me today!"

    r "Looking forward to seeing what you can make with Ren'Py and Raconteur."

    r "Don't forget about me when you make it big!"

    # window hide

    # Returning from the top level quits the game.
    return