# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd-1-1/20min/

get_started = """\n Fill in the Banks and Test your Python knowledge!""
\n Choose your level of difficulty (easy, medium, hard, impossible" and answer when prompted to fill in the blanks."""

# all of the options for the blanks in the quiz. Each paragraph can have up to 4 blanks
blank_options = ["___1___", "___2___", "___3___", "___4___"]

#	Asks user for desired level, then returns corresponding paragrpah and solution word set
def choose_level():
	level = ""
	print "\nWhich level do you choose?: easy, medium, hard, or impossible?"
	levels = ["easy", "medium", "hard", "impossible"]
	while level not in levels:
		level = raw_input("Choose a level: ")
        if level == "easy":
            return easy_paragraph, easy_answers
        elif level == "medium":
            return medium_paragraph, medium_answers
        elif level == "hard":
            return hard_paragraph, hard_answers
        elif level == "impossible":
            return impossible_paragraph, impossible_answers
        else:
            print "Invalid input. Choose from these levels: easy, medium, hard, impossible"


#if the user selects "easy" game mode, this is the corresponding paragraph and answers
easy_paragraph = """A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary, tuple, and ___4___ or can be more complicated such as objects and lambda functions."""
easy_answers = ["function", "parameters", "None", "list"]

#if the user selects "medium" game mode, this is the corresponding paragraph and answers
medium_paragraph = """A ___1___ in Python can either be a "#" for a single line or a triple quote for multi-line, but each of these are interpreted differently. A # ___1___ is ignored by the computer. A triple quote ___1___ is more like a manual for others, and you can call the documentation for a function, myFunc, by typing this into the bash: myFunc.__doc___. Let's talk loops. The proper formatting for a ___2___ loop is: ___2___ " x in List:". Let's talk string functions. The ___3___ function breaks apart a string using the input as the delimiter, and the ___4___ function does exactly the opposite."""
medium_answers = ["comment", "for", "split", "join"]

#if the user selects "hard" game mode, this is the corresponding paragraph and answers
hard_paragraph = """The main difference between a ___1___ and a list is mutability: a ___1___ is immutable, whereas a list is mutable. Items in a ___1___ can't be modified. One of the cool things you can do with a list is ___2___ lists within lists. A list within a list only takes one index slot. To increment an integer variable by 1, use "var ___3___." In Python, users can be prompted to provide inputs using the function ___4___."""
hard_answers = ["tuple", "nest", "+= 1", "raw_input"]

#if the user selects "impossible" game mode, this is the corresponding paragraph and answers
impossible_paragraph = """We didn't learn this in the course, but Python has this concept called ___1___, which store connections between pieces of
information. Each item in each of these ___1___ is a key-value pair. Other concepts not covered in the course: A ___2___ defines the behavior of an object and the kind of information an object can store. The information in a ___2___is stored in attributes, and functions that belong to a class
are called ___3___. Lastly, to debug your Python, consider using an ___4___, which tells the program to test a condition and trigger an error if the condition is false."""
impossible_answers = ["dictionaries", "class", "methods", "assert"]

# asks the user to provide an answer to the current blank.
def guess(successful_blanks):
    current_blank = successful_blanks
    if successful_blanks == 0:
        current_blank = blank_options[0]
    elif successful_blanks == 1:
        current_blank = blank_options[1]
    elif successful_blanks == 2:
        current_blank = blank_options[2]
    elif successful_blanks == 3:
        current_blank = blank_options[3]
    guess = raw_input("\nEnter your best guess for {}: \n Your guess: ".format(current_blank))
    return guess

# # asks the user to provide number of acceptable attempts
def max_attempts():
    max_attempts = 1 # default to one attempt
    print "\nHow many attempts do you want per blank?: "
    max_attempts = int(raw_input(" "))
    return max_attempts

# where the magic happens. The engine for the game. Takes user input, uses other functions, and congratulates users when they complete the level.
def quiz_engine():
    successful_blanks = 0
    attempts = 0
    print get_started
    user_level, answer_set = choose_level()
    maxAttempts = max_attempts()
    while successful_blanks < len(blank_options):
        print user_level
        user_guess = guess(blank_options[successful_blanks])
        if user_guess == answer_set[successful_blanks]:
            print "\nCorrect! Nice job.\n"
            user_level = user_level.replace(blank_options[successful_blanks], user_guess)
            successful_blanks += 1
            attempts = 0
            if successful_blanks == len(blank_options):
                print user_level
                print "\n Congratulations! You filled in all the blanks correctly. \n"
                break
        else:
            attempts += 1
            if attempts >= maxAttempts:
                print "\nSorry, you failed!  Do a bit of Python research and try again! \n"
                break
            else:
                print "\nSorry, try again. You've attempted ", attempts, " times \n"

quiz_engine()
