import random
import tkinter as tk
from tkinter import messagebox

def hangman_mcq():
  questions = [
    {
      "question": "What is the capital of France?",
      "options": ["A. Paris", "B. London", "C. Rome", "D. Berlin"],
      "answer": "A"
    },
    {
      "question": "Which planet is known as the Red Planet?",
      "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
      "answer": "B"
    },
    {
      "question": "What is 5 + 3?",
      "options": ["A. 6", "B. 7", "C. 8", "D. 9"],
      "answer": "C"
    },
    {
      "question": "Which animal is known as the King of the Jungle?",
      "options": ["A. Tiger", "B. Elephant", "C. Lion", "D. Giraffe"],
      "answer": "C"
    }
  ]

  random.shuffle(questions)
  lives = 5
  current_question_index = 0

  def draw_hangman():
    """Draw the hangman figure based on remaining lives."""
    stages = [
      lambda: canvas.create_line(50, 200, 150, 200, width=3),  # Base
      lambda: canvas.create_line(100, 200, 100, 50, width=3),  # Pole
      lambda: canvas.create_line(100, 50, 150, 50, width=3),   # Top bar
      lambda: canvas.create_line(150, 50, 150, 80, width=3),   # Rope
      lambda: canvas.create_oval(140, 80, 160, 100, width=3),  # Head
      lambda: canvas.create_line(150, 100, 150, 140, width=3), # Body
      lambda: canvas.create_line(150, 110, 130, 120, width=3), # Left arm
      lambda: canvas.create_line(150, 110, 170, 120, width=3), # Right arm
      lambda: canvas.create_line(150, 140, 130, 170, width=3), # Left leg
      lambda: canvas.create_line(150, 140, 170, 170, width=3)  # Right leg
    ]
    if 5 - lives < len(stages):
      stages[5 - lives]()

  def load_question():
    nonlocal current_question_index
    if current_question_index < len(questions):
      question_label.config(text=questions[current_question_index]["question"])
      for i, option in enumerate(questions[current_question_index]["options"]):
        option_buttons[i].config(text=option, state=tk.NORMAL)
    else:
      messagebox.showinfo("Congratulations!", "You answered all questions correctly!")
      root.destroy()

  def check_answer(selected_option):
    nonlocal lives, current_question_index
    correct_answer = questions[current_question_index]["answer"]
    if selected_option == correct_answer:
      messagebox.showinfo("Correct!", "Your answer is correct!")
    else:
      lives -= 1
      draw_hangman()
      messagebox.showerror("Wrong!", f"Wrong answer! The correct answer was {correct_answer}. You have {lives} lives remaining.")
      if lives == 0:
        messagebox.showerror("Game Over", "You have no lives left. Game Over!")
        root.destroy()
        return
    current_question_index += 1
    load_question()

  # GUI setup
  root = tk.Tk()
  root.title("Hangman MCQ Game")
  root.geometry("600x500")

  tk.Label(root, text="Welcome to the Hangman MCQ Game!", font=("Arial", 16)).pack(pady=10)
  tk.Label(root, text="Answer the questions correctly to avoid the hangman!", font=("Arial", 12)).pack(pady=5)

  canvas = tk.Canvas(root, width=300, height=250, bg="white")
  canvas.pack(pady=10)

  question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=400, justify="center")
  question_label.pack(pady=20)

  option_buttons = []
  for i in range(4):
    btn = tk.Button(root, text="", font=("Arial", 12), width=20, command=lambda i=i: check_answer(questions[current_question_index]["options"][i][0]))
    btn.pack(pady=5)
    option_buttons.append(btn)

  load_question()
  root.mainloop()

if __name__ == "__main__":
  hangman_mcq()