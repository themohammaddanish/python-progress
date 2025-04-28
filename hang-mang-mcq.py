import random
import tkinter as tk
from tkinter import messagebox

class HangmanGame:
  def __init__(self):
    self.words = [
      {"word": "elephant", "hint": "A large animal with a trunk."},
      {"word": "giraffe", "hint": "An animal with a long neck."},
      {"word": "tiger", "hint": "A big cat with stripes."},
      {"word": "penguin", "hint": "A bird that cannot fly but swims."},
      {"word": "zebra", "hint": "An animal with black and white stripes."}
    ]
    self.mcq_questions = [
      {"question": "Which animal has a trunk?", "options": ["A. Elephant", "B. Tiger", "C. Giraffe", "D. Zebra"], "answer": "A"},
      {"question": "Which animal has a long neck?", "options": ["A. Penguin", "B. Giraffe", "C. Tiger", "D. Zebra"], "answer": "B"},
      {"question": "Which animal has stripes?", "options": ["A. Elephant", "B. Penguin", "C. Tiger", "D. Giraffe"], "answer": "C"}
    ]
    self.max_lives = 6
    self.lives = self.max_lives
    self.score = 0
    self.current_word = None
    self.guessed_letters = []
    self.current_mcq_index = 0
    self.setup_game()

  def setup_game(self):
    self.root = tk.Tk()
    self.root.title("Hangman Game for Kids")
    self.root.geometry("600x500")

    tk.Label(self.root, text="Welcome to the Hangman Game!", font=("Arial", 16)).pack(pady=10)
    tk.Label(self.root, text="Guess the word before the hangman is complete!", font=("Arial", 12)).pack(pady=5)

    self.canvas = tk.Canvas(self.root, width=300, height=250, bg="white")
    self.canvas.pack(pady=10)

    self.hint_label = tk.Label(self.root, text="", font=("Arial", 14), wraplength=400, justify="center")
    self.hint_label.pack(pady=10)

    self.word_label = tk.Label(self.root, text="", font=("Arial", 18))
    self.word_label.pack(pady=10)

    self.entry = tk.Entry(self.root, font=("Arial", 14))
    self.entry.pack(pady=5)

    self.guess_button = tk.Button(self.root, text="Guess", font=("Arial", 12), command=self.check_guess)
    self.guess_button.pack(pady=5)

    self.feedback_label = tk.Label(self.root, text="", font=("Arial", 12))
    self.feedback_label.pack(pady=10)

    self.start_new_round()

    self.root.mainloop()

  def start_new_round(self):
    self.lives = self.max_lives
    self.guessed_letters = []
    self.current_word = random.choice(self.words)
    self.update_word_display()
    self.hint_label.config(text=f"Hint: {self.current_word['hint']}")
    self.feedback_label.config(text="")
    self.canvas.delete("all")

  def update_word_display(self):
    display_word = " ".join([letter if letter in self.guessed_letters else "_" for letter in self.current_word["word"]])
    self.word_label.config(text=display_word)

  def check_guess(self):
    guess = self.entry.get().lower()
    self.entry.delete(0, tk.END)

    if len(guess) != 1 or not guess.isalpha():
      self.feedback_label.config(text="Please enter a single letter.")
      return

    if guess in self.guessed_letters:
      self.feedback_label.config(text="You already guessed that letter.")
      return

    self.guessed_letters.append(guess)

    if guess in self.current_word["word"]:
      self.feedback_label.config(text="Correct guess!")
    else:
      self.lives -= 1
      self.feedback_label.config(text=f"Wrong guess! Lives remaining: {self.lives}")
      self.draw_hangman()

    self.update_word_display()

    if "_" not in self.word_label.cget("text"):
      self.score += 10
      messagebox.showinfo("Congratulations!", "You guessed the word!")
      self.ask_mcq()
    elif self.lives == 0:
      messagebox.showerror("Game Over", f"You lost! The word was '{self.current_word['word']}'.")
      self.ask_mcq()

  def draw_hangman(self):
    stages = [
      lambda: self.canvas.create_line(50, 200, 150, 200, width=3),  # Base
      lambda: self.canvas.create_line(100, 200, 100, 50, width=3),  # Pole
      lambda: self.canvas.create_line(100, 50, 150, 50, width=3),   # Top bar
      lambda: self.canvas.create_line(150, 50, 150, 80, width=3),   # Rope
      lambda: self.canvas.create_oval(140, 80, 160, 100, width=3),  # Head
      lambda: self.canvas.create_line(150, 100, 150, 140, width=3)  # Body
    ]
    if self.max_lives - self.lives < len(stages):
      stages[self.max_lives - self.lives]()

  def ask_mcq(self):
    if self.current_mcq_index < len(self.mcq_questions):
      question = self.mcq_questions[self.current_mcq_index]
      self.current_mcq_index += 1

      def check_mcq_answer(selected_option):
        if selected_option == question["answer"]:
          self.score += 5
          messagebox.showinfo("Correct!", "You answered correctly!")
        else:
          messagebox.showerror("Wrong!", f"The correct answer was {question['answer']}.")
        self.start_new_round()

      mcq_window = tk.Toplevel(self.root)
      mcq_window.title("MCQ Question")
      tk.Label(mcq_window, text=question["question"], font=("Arial", 14), wraplength=400).pack(pady=10)
      for option in question["options"]:
        tk.Button(mcq_window, text=option, font=("Arial", 12),
              command=lambda opt=option[0]: [mcq_window.destroy(), check_mcq_answer(opt)]).pack(pady=5)
    else:
      messagebox.showinfo("Game Complete", f"Your final score is: {self.score}")
      self.root.destroy()

if __name__ == "__main__":
  HangmanGame()