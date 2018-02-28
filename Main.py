from tkinter import *
import random


class Hangman:

    def __init__(self, master):
        self.master = master
        self.master.title("HangMan")
        self.master.resizable(width=False, height=False)

        self.gameState = 0
        self.secretWord = ""
        self.dashes = ""
        self.totalGuesses = 6
        self.guessCount = 0
        self.progress = []
        self.words = []

        self.infoText = StringVar()
        self.inputText = StringVar()
        self.guessedLettersText = StringVar()
        self.randomButtonText = StringVar()
        self.guessesText = StringVar()
        self.guessButtonText = StringVar()
        self.WIDTH = 200
        self.HEIGHT = 300

        self.randomButton = Button(self.master, textvariable=self.randomButtonText, command=self.random_button)
        self.randomButton.pack(fill=BOTH, side=TOP)

        self.guessesLabel = Label(self.master, textvariable=self.guessesText)
        self.guessesLabel.pack(fill=BOTH, side=TOP, anchor="e")

        self.canvas = Canvas(self.master, width=self.WIDTH, height=self.HEIGHT, background='white')
        self.canvas.pack(side=TOP)

        self.guessButton = Button(self.master, textvariable=self.guessButtonText, command=self.guess_button)
        self.guessButton.pack(fill=BOTH, side=BOTTOM)

        self.input = Entry(self.master, textvariable=self.inputText)
        self.input.pack(fill=BOTH, side=BOTTOM)
        self.input.focus()

        self.wordLabel = Label(self.master, textvariable=self.infoText)
        self.wordLabel.pack(fill=BOTH, side=BOTTOM)

        self.guessedLetters = Label(self.master, textvariable=self.guessedLettersText)
        self.guessedLetters.pack(fill=BOTH, side=BOTTOM)

        self.initial_setup()

    def guess_button(self):
        if self.gameState == 0:
            if len(self.inputText.get()) < 5:
                self.input.delete(0, 'end')
                self.guessButtonText.set("I Require a longer word.")
                return
            else:
                self.guessButtonText.set("Guess")
                self.secretWord = self.inputText.get().lower()
                self.input.delete(0, 'end')
                for self.letter in self.secretWord:
                    self.progress.append('_ ')
                self.dashes = "".join(self.progress)
                self.infoText.set(self.dashes)
                self.gameState = 1

        elif self.gameState == 1:

            if self.inputText.get() == self.secretWord:

                self.randomButtonText.set("You Win!")
                self.input.delete(0, 'end')
                self.gameState = 2
                return

            elif len(self.inputText.get()) != 1:

                self.input.delete(0, 'end')
                self.randomButtonText.set("Enter a letter or the word.")
                return

            if len(self.inputText.get()) == 1:
                if self.guessCount < self.totalGuesses:

                    if (self.inputText.get() in self.secretWord) and \
                            (self.inputText.get() not in self.guessedLettersText.get()):

                        guessed = self.guessedLettersText.get() + self.inputText.get() + ", "
                        self.guessedLettersText.set(guessed)
                        self.randomButtonText.set("Correct!")
                        self.progress_updater(self.inputText.get(), self.secretWord, self.progress)
                        self.infoText.set(self.dashes)
                        self.input.delete(0, 'end')
                        if self.secretWord == self.dashes:
                            self.randomButtonText.set("You Win!")
                            self.input.delete(0, 'end')
                            self.gameState = 2
                            return

                    elif (self.inputText.get() not in self.secretWord) and \
                            (self.inputText.get() not in self.guessedLettersText.get()):

                        guessed = self.guessedLettersText.get() + self.inputText.get() + ", "
                        self.guessedLettersText.set(guessed)
                        self.guessCount += 1
                        self.guessesText.set("{} out of {} guesses".format(self.guessCount, self.totalGuesses))
                        self.randomButtonText.set("Wrong!")
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
                        self.input.delete(0, 'end')
                        if self.guessCount == self.totalGuesses:
                            self.randomButtonText.set("You lose.")
                            self.gameState = 2

                    else:

                        self.randomButtonText.set("You already guessed that.")
                        self.input.delete(0, 'end')

    def random_button(self):
        if self.gameState == 0:
            self.words = ["hangman", "chairs", "backpack", "bodywash", "clothing",
                          "computer", "python", "program", "glasses", "sweatshirt",
                          "sweatpants", "mattress", "friends", "clocks", "biology",
                          "algebra", "suitcase", "knives", "ninjas", "shampoo"
                          ]
            self.secretWord = random.choice(self.words).lower()
            for self.letter in self.secretWord:
                self.progress.append('_ ')
            self.dashes = "".join(self.progress)
            self.infoText.set(self.dashes)
            self.randomButtonText.set("Word Chosen!")
            self.guessButtonText.set("Guess")
            print(self.secretWord)
            self.input.delete(0, 'end')
            self.gameState = 1

    def progress_updater(self, guess, the_word, progress):
        i = 0
        while i < len(the_word):
            if guess == the_word[i]:
                progress[i] = guess
                i += 1
            else:
                i += 1
        self.dashes = "".join(self.progress)
        return self.dashes

    def initial_setup(self):

        self.canvas.create_line(self.WIDTH * 3/4, 100, self.WIDTH * 3/4, self.HEIGHT, width=2.0, fill='#303030')
        self.canvas.create_line(0, self.HEIGHT, self.HEIGHT, self.HEIGHT, width=2.0, fill='#303030')
        self.canvas.create_line(self.WIDTH * 3 / 4, 100, 75, 100, width=2.0, fill='#303030')
        self.canvas.create_line(75, 100, 75, 125, width=2.0, fill='#303030')

        self.infoText.set("Type a word or randomize")
        self.randomButtonText.set("Randomize")
        self.guessButtonText.set("Play!")


root = Tk()
game = Hangman(root)

root.mainloop()
