import random
import tkinter as tk
from PIL import ImageTk, Image

LABEL_WRONG_LETTERS = "Lettres essayées : "
GAME_OVER_TEXT = "Perdu ! Le mot était {word}"

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.master = master

        # If the counter equals 7, game over.
        self.hangman_state_counter = 1

        self.wrong_letters_set = set()
        self.attempted_letters_set = set()

        self.has_won = False

        self.master.geometry("640x480")
        
        self.pack()
        self.pick_random_word()
        self.create_widgets()

    def pick_random_word(self):
        line = open('dico.py').read().splitlines() 
        self.random_word = random.choice(line)
        print(self.random_word)
        self.current_word = list("_" * len(self.random_word))

    @classmethod
    def get_hangman_steps(self):
        PhotoImage(file="ball.ppm")
    
    def reveal_word(self, letter):
        found = False
        for i, w in enumerate(self.random_word):
            if letter.upper() == w.upper() and self.current_word[i] == '_':
                self.current_word[i] = letter.upper()
                found = True
        return found
    
    def check_letter(self):

        # If the player has lost or won, do not do anything.
        if self.hangman_state_counter == 7 or self.has_won:
            return  # Game over.

        # Get the first letter in the input.
        letter = self.input_letter.get()[0]
        
        # If the letter has been tried already, do not do anything.
        if letter in self.attempted_letters_set:
            return

        self.attempted_letters_set.add(letter)

        found = self.reveal_word(letter)
        if found:
            self.word_guessed["text"] = self.display_current_word()

            # If there is no more letter to guess, we have won.
            if "_" not in self.current_word:
                self.game_over_state["fg"] = "green"
                self.game_over_state["text"] = "Bravo !"
                self.has_won = True

        else:
            self.wrong_letters_set.add(letter.upper())
            self.wrong_letters["text"] = LABEL_WRONG_LETTERS + ", ".join(
                self.wrong_letters_set
            )

            self.hangman_state_counter += 1
            self.update_hangman_state()

            if self.hangman_state_counter == 7:
                self.game_over_state["text"] = GAME_OVER_TEXT.format(
                    word=self.random_word
                )
            
        # Clear the entry.
        self.input_letter.insert(0, '')

    def update_hangman_state(self):
        hangman_picture = ImageTk.PhotoImage(
            Image.open(f"hangman{self.hangman_state_counter}.png")
        )
        self.hangman_state.configure(image=hangman_picture)
        self.hangman_state.image = hangman_picture

    def display_current_word(self):
        """Display the current word with spaces to improve readability."""
        return " ".join(self.current_word)

    def create_widgets(self):
        self.letter_label = tk.Label(
            self, text="Entrez une lettre"
        )
        self.letter_label.pack(side="top")

        self.input_letter = tk.Entry(self)
        self.input_letter.pack(side="top")

        self.check_letter_button = tk.Button(
            self,
            text="Essayer",
            command=self.check_letter
        )
        self.check_letter_button["command"] = self.check_letter
        self.check_letter_button.pack(side="top")

        self.word_guessed = tk.Label(
            self, text=self.display_current_word()
        )
        self.word_guessed.pack(side="top")

        hangman_picture = ImageTk.PhotoImage(Image.open("hangman1.png"))
        self.hangman_state = tk.Label(
            self, image=hangman_picture
        )
        self.hangman_state.image = hangman_picture
        self.hangman_state.place(x=0, y=0)
        self.hangman_state.pack(side="top")

        self.wrong_letters = tk.Label(self, text="Lettres essayées :")
        self.wrong_letters.pack(side="top")

        self.game_over_state = tk.Label(fg="red", text="")
        self.game_over_state.pack(side="top")


root = tk.Tk()
app = Application(master=root)
app.mainloop()