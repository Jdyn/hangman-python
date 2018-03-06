from tkinter import *  # Import everything inside of the Tkinter library
import random  # Import the Random library


class Hangman:  # Create a class

    def __init__(self, master):  # Variable initiation method. All variable should be declared here before use.
        self.master = master  # Tkinter instantiation
        self.master.title("HangMan")  # Window title
        self.master.resizable(width=False, height=False)  # Non resizable window

        self.gameState = 0  # Standard state machine. handles which code you want to be called at any given time
        self.secretWord = ""  # The secret word - String
        self.dashes = ""  # The secret word hidden - String
        self.totalGuesses = 6  # Maximum guesses
        self.guessCount = 0  # Guess counter
        self.progress = []  # Array containing the unknown and known letters
        self.words = []  # Array of available random words

        self.infoText = StringVar()  # Tkinter method which updates a GUI element text if this container variable is updated.
        self.inputText = StringVar()  # If this variable is changed. The GUI element will update according to the change
        self.guessedLettersText = StringVar()
        self.randomButtonText = StringVar()
        self.guessesText = StringVar()
        self.guessButtonText = StringVar()
        self.WIDTH = 200  # A constant indicating the exact width of the window
        self.HEIGHT = 300  # A constant indicating the exact height of the window

        # the following happens linearly so if you create some GUI on at the same position the GUI will be placed below it
        self.randomButton = Button(self.master, textvariable=self.randomButtonText, command=self.random_button)  # Create a button
        self.randomButton.pack(fill=BOTH, side=TOP)  # add it to the window

        self.guessesLabel = Label(self.master, textvariable=self.guessesText)  # Create a button
        self.guessesLabel.pack(fill=BOTH, side=TOP, anchor="e")  # add it to the window

        self.canvas = Canvas(self.master, width=self.WIDTH, height=self.HEIGHT, background='white')  # Create a canvas below the buttons
        self.canvas.pack(side=TOP)  # add it to the window

        self.guessButton = Button(self.master, textvariable=self.guessButtonText, command=self.guess_button)  # Create a button anchor to the bottom
        self.guessButton.pack(fill=BOTH, side=BOTTOM)  # add it to the bottom of the window

        self.input = Entry(self.master, textvariable=self.inputText)  # Create a text field above the bottom button (linear creation)
        self.input.pack(fill=BOTH, side=BOTTOM)  # add it to the window at the bottom
        self.input.focus()  # The cursor will start in the textbox on launch

        self.wordLabel = Label(self.master, textvariable=self.infoText)  # Create an element to display text
        self.wordLabel.pack(fill=BOTH, side=BOTTOM)  # Add it to the window above the text field

        self.guessedLetters = Label(self.master, textvariable=self.guessedLettersText)  # create an element to display text above the previous label
        self.guessedLetters.pack(fill=BOTH, side=BOTTOM)  # Add tge label to the window above the previous label

        self.initial_setup()  # call a method

    def guess_button(self):  # this method is called every time the guess button is pressed
        if self.gameState == 0:  # Perform this logic if gameState is equal to 0.
            if len(self.inputText.get()) < 5:  # Perform this logic if the length of the string inputed in the text field is less than 5 characters
                self.input.delete(0, 'end')  # delete all characters inside of the text field
                self.guessButtonText.set("I Require a longer word.")  # Set the text of a button equal to this string
                return  # Stop reading the rest of the method
            else:  # if gameState is not 0
                self.guessButtonText.set("Guess")  # set the text on this button equal to this string
                self.secretWord = self.inputText.get().lower()  # set this variable equal to the text inputed into the text field
                self.input.delete(0, 'end')  # Delete everything inside of the text field
                for self.letter in self.secretWord:  # Perform logic for each character inside of the string
                    self.progress.append('_ ')  # for each character in the secret word, append an underscore at a new index
                self.dashes = "".join(self.progress)  # Using string interpolation, set this string into a string version of the specified array
                self.infoText.set(self.dashes)  # set the label equal to this string
                self.gameState = 1  # set gameState equal to 1. This logic will never be called again now.

        elif self.gameState == 1:  # if the function is called and gameState is 1, execute this code
            # Everything happens linearly
            if self.inputText.get() == self.secretWord:  # First always check if the user inputed text is equal to the final word

                self.randomButtonText.set("You Win!")  # if it is, set the button text
                self.input.delete(0, 'end')  # delete what is in the text field
                self.gameState = 2  # Set gameState to 2
                return  # end the function and stop all code in the rest of the function to be read

            elif len(self.inputText.get()) != 1:  # check if the inputted text is not 1 character in length

                self.input.delete(0, 'end')  # Delete what is in the input text
                self.randomButtonText.set("Enter a letter or the word.")  # set the text on the button
                return  # end the function and stop all code in the rest of the function to be read

            if len(self.inputText.get()) == 1:  # If the length of the inputted text is equal to 1 character
                if self.guessCount < self.totalGuesses:  # Check if the amount of guess left is less than total guesses

                    if (self.inputText.get() in self.secretWord) and (self.inputText.get() not in self.guessedLettersText.get()):
                    # Check if the inputted letter is inside of the secret word and that the player has not already guessed this letter before

                        guessed = self.guessedLettersText.get() + self.inputText.get() + ", "  # use string concatenation to form a string of all of guessed letters
                                                                                               # plus the newly guessed letter, plus a comma
                        self.guessedLettersText.set(guessed)  # Set the label on the window equal to the "guessed" variable
                        self.randomButtonText.set("Correct!")  # set the text on the button
                        self.progress_updater(self.inputText.get(), self.secretWord, self.progress)  # Call a function and pass in the following variables
                        self.infoText.set(self.dashes)  # Show this variable on this label in the window.
                        self.input.delete(0, 'end')  # Empty the text field
                        if self.secretWord == self.dashes:  # Check if the secret word is equal to the dashed word
                            self.randomButtonText.set("You Win!")  # Set the text on a label
                            self.input.delete(0, 'end')  # Delete what is inside of the text field
                            self.gameState = 2  # Set the gameState variable equal to 2
                            return  # Stop the rest of the function to be read

                    elif (self.inputText.get() not in self.secretWord) and (self.inputText.get() not in self.guessedLettersText.get()):
                    # Check if the inputted letter is not inside of the secret word and the inputted letter is not in the list of guessed letters

                        guessed = self.guessedLettersText.get() + self.inputText.get() + ", "  # Create a variable equal to the current list of
                                                                                               # guess letters, plus the current guessed letter, plus a comma
                        self.guessedLettersText.set(guessed)  # Set the label equal to the variable above
                        self.guessCount += 1  # Simply, add 1 to yourself. (yourself is equal to yourself + 1)
                        self.guessesText.set("{} out of {} guesses".format(self.guessCount, self.totalGuesses))  # Python 3.6.3 String interpolation allows for the
                                                                                                                 # Format function which places any variable you want
                                                                                                                 # inside of the curly braces.
                        self.randomButtonText.set("Wrong!")  # Set the text on a label

                        # every time the button is pressed, a drawing will be made on the canvas depending on how many times guessCount has increased
                        if self.guessCount == 1:
                            self.canvas.create_oval(60, 125, 90, 155, fill='white')  # Head
                        if self.guessCount == 2:
                            self.canvas.create_line(75, 155, 75, 215, width=2.0)  # Body
                        if self.guessCount == 3:
                            self.canvas.create_line(75, 160, 55, 190, width=2.0)  # Left arm
                        if self.guessCount == 4:
                            self.canvas.create_line(75, 160, 95, 190, width=2.0)  # Right arm
                        if self.guessCount == 5:
                            self.canvas.create_line(75, 215, 55, 250, width=2.0)  # Left leg
                        if self.guessCount == 6:
                            self.canvas.create_line(75, 215, 95, 250, width=2.0)  # Right leg
                        self.input.delete(0, 'end')  # empty the text field
                        if self.guessCount == self.totalGuesses:  # Check if guessCount is equal to totalGuesses
                            self.randomButtonText.set("You lose.")  # Set the button text
                            self.gameState = 2  # Change gameState to 2

                    else:  # if the aforementioned conditions are not met do this

                        self.randomButtonText.set("You already guessed that.")  # Set the text on a button
                        self.input.delete(0, 'end')  # Empty the text field

    def random_button(self):  # Method called when the random button is pressed
        if self.gameState == 0:  # Check if gameState is 0
            self.words = ["hangman", "chairs", "backpack", "bodywash", "clothing",
                          "computer", "python", "program", "glasses", "sweatshirt",  # set the words array equal to an array of strings
                          "sweatpants", "mattress", "friends", "clocks", "biology",
                          "algebra", "suitcase", "knives", "ninjas", "shampoo"
                          ]
            self.secretWord = random.choice(self.words).lower()  # Set the secret word equal to a random string from the word list
            for self.letter in self.secretWord:  # perform logic for each character inside of this string
                self.progress.append('_ ')  # Add each character to a new position in the array
            self.dashes = "".join(self.progress)  # Essentially, convert the "progress" array to a string and save it into this variable
            self.infoText.set(self.dashes)  # Set the text of a label
            self.randomButtonText.set("Word Chosen!")  # Set the text of a button
            self.guessButtonText.set("Guess")  #  Set the text of a button
            self.input.delete(0, 'end')  # Empty the text in the text field
            self.gameState = 1  # Set the gameState to 1. This logic cannot be called any more

    def progress_updater(self, guess, the_word, progress):  # Method called in guess_button
        i = 0  # set local variable equal to 0
        while i < len(the_word):  # English: Perform this logic if the variable i is less than the length of the secretWord
            if guess == the_word[i]:  # check if the guessed letter is at any index within the secret word
                progress[i] = guess  # Set the array named "progress" at the position which the letter was found in, equal to that letter. This array was filled
                # with dashes equal to the secret word in the beginning
                i += 1  # Add 1 to the variable i
            else:
                i += 1  # Add 1 to the variable i
        self.dashes = "".join(self.progress)  # set the variable dashes equal to the entire array of "progress"
        return self.dashes  # When this function is called the result of its calling will be this variable

    def initial_setup(self):  # This method is called at the beginning of the game

        # Draw the lines onto the canvas that form the background
        self.canvas.create_line(self.WIDTH * 3/4, 100, self.WIDTH * 3/4, self.HEIGHT, width=2.0, fill='#303030')
        self.canvas.create_line(0, self.HEIGHT, self.HEIGHT, self.HEIGHT, width=2.0, fill='#303030')
        self.canvas.create_line(self.WIDTH * 3 / 4, 100, 75, 100, width=2.0, fill='#303030')
        self.canvas.create_line(75, 100, 75, 125, width=2.0, fill='#303030')

        # Initialize the text on the buttons
        self.infoText.set("Type a word or randomize")
        self.randomButtonText.set("Randomize")
        self.guessButtonText.set("Play!")


root = Tk()  # Initialize the Tkinter module
game = Hangman(root)  # pass in the root variable in the Hangman class so that necessary variables can use it.

root.mainloop()  # Continue running the program as long as the window is alive
