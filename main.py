# import tkinter as tk
# from tkinter import messagebox

# # # a=8769823689
# # # b=8769823689
# # # c= b+a
# # # d= "hello"
# # # print(c)
# # # if (b>2334):
# # #     print("b is greater than 2334")
# # # else:
# # #     print("b is less than 2334")
# # # print(type(d))

# # # #this is calculator for bigneer 
# # # a= int(input("Enter the first number: "))
# # # b= int(input("Enter the second number: "))
# # # add= a+b
# # # sub=a-b
# # # mul=a*b
# # # div=a/b
# # # print("Addition of two numbers is: ", add)
# # # print("Subtraction of two numbers is: ", sub)
# # # print("Multiplication of two numbers is: ", mul)
# # # print("Division of two numbers is: ", div)

# # MAXSIZE = 8
# # stack = [0] * 8
# # top = -1
# # def isfull():
# #     if(top == MAXSIZE):
# #         return 1
# #     else:
# #         return 0
# # def peek():
# #     return stack[top]

# # def push(data):
# #     global top
# #     if(isfull() != 1):
# #         top = top + 1
# #         stack[top] = data
# #     else:
# #         print("Could not insert data, Stack is full.")
# #     return data
# # push(44)
# # push(10)
# # push(62)
# # push(123)
# # push(15)
# # print("Stack Elements: ")
# # for i in range(MAXSIZE):
# #     print(stack[i], end = " ")
# # print("\nElement at top of the stack: ", peek())
# # a = input("enter the number: ")
# # b = input("enter the number: ")
# # c=a+b
# # # print(int(a) + int(b))
# # print(c)
# # print("hello world \"hello\" this is a word")
# # print('hello world "hello" this is a word')
# # a = "danish"
# # for i in range(10):
# #     print(a + "how are you")
# # a = "Danish"
# # b= "khan"
# # print(a[0:3] + b[0:2])
# # for character in a:
# #     print(character)
# # a ="1212Danish1212"
# # print(a.replace("danish", "khan"))
# # import time 
# # greeting = time.strftime("%H:%M:%S")
# # if "00:00:00" < greeting < "12:00:00":
# #   print ("good morning sir ")
# # elif "16:00:00" < greeting:
# #   print("good evening sir")
# # else:
# #   print("okey sir")

# print("i'm a logo deigner")

# # <a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&pause=1000&color=F7F7F7&width=435&lines=Hi%2C+I%E2%80%99m+%40themohammaddanish;I%E2%80%99m+Web+Developer!!;And+I+will+be+an+software+Engineer" alt="Typing SVG" /></a>

# x = int(input("Enter the numeber:"))
# y = int(input("Enter the numeber:"))
# operation = input("Enter the operation:")
# match operation:
#   case "+":
#     print(x+y)
#   case "-":
#      print(x-y)
#   case "*":
#     print(x*y)

# for i in range(10):
#   a = input("Enter the number: ")
#   for x in a:
#     print(x)

# questions = [
#   {
#     "question": "What is the capital of India?",
#     "options": ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
#     "correct": "B",
#     "prize": 1000
#   },
#   {
#     "question": "Which planet is known as the Red Planet?",
#     "options": ["A. Jupiter", "B. Venus", "C. Mars", "D. Saturn"],
#     "correct": "C",
#     "prize": 2000
#   },
#   {
#     "question": "Who is known as the Father of Computer?",
#     "options": ["A. Charles Babbage", "B. Alan Turing", "C. Bill Gates", "D. Steve Jobs"],
#     "correct": "A",
#     "prize": 5000
#   }
# ]

# class QuizGame:
#   def __init__(self):
#     self.window = tk.Tk()
#     self.window.title("Quiz Game")
#     self.window.geometry("600x500")
#     self.window.config(bg="#f0f0f0")
    
#     self.current_question = 0
#     self.total_prize = 0
    
#     self.create_widgets()
    
#   def create_widgets(self):
#     # Title
#     title = tk.Label(self.window, text="Knowledge Quiz", font=("Arial", 24, "bold"), bg="#f0f0f0")
#     title.pack(pady=20)
    
#     # Question frame
#     self.question_frame = tk.Frame(self.window, bg="#f0f0f0")
#     self.question_frame.pack(fill="both", padx=20)
    
#     self.question_label = tk.Label(self.question_frame, wraplength=500, 
#                    font=("Arial", 12), bg="#f0f0f0")
#     self.question_label.pack(pady=20)
    
#     # Options frame
#     self.options_frame = tk.Frame(self.window, bg="#f0f0f0")
#     self.options_frame.pack(fill="both", padx=20)
    
#     self.option_buttons = []
#     for i in range(4):
#       btn = tk.Button(self.options_frame, font=("Arial", 10),
#               command=lambda x=i: self.check_answer(x))
#       btn.pack(pady=5, fill="x")
#       self.option_buttons.append(btn)
    
#     # Prize label
#     self.prize_label = tk.Label(self.window, text="Current Prize: ₹0",
#                   font=("Arial", 12, "bold"), bg="#f0f0f0")
#     self.prize_label.pack(pady=20)
    
#     self.show_question()
    
#   def show_question(self):
#     if self.current_question < len(questions):
#       q = questions[self.current_question]
#       self.question_label.config(text=q["question"])
#       for i, option in enumerate(q["options"]):
#         self.option_buttons[i].config(text=option)
#     else:
#       self.end_game()
  
#   def check_answer(self, choice):
#     q = questions[self.current_question]
#     selected = q["options"][choice][0]  # Get first letter (A/B/C/D)
    
#     if selected == q["correct"]:
#       self.total_prize += q["prize"]
#       messagebox.showinfo("Correct!", f"You won ₹{q['prize']}!")
#       self.current_question += 1
#       self.prize_label.config(text=f"Current Prize: ₹{self.total_prize}")
#       self.show_question()
#     else:
#       messagebox.showerror("Wrong!", "Game Over!")
#       self.end_game()
  
#   def end_game(self):
#     for btn in self.option_buttons:
#       btn.config(state="disabled")
#     messagebox.showinfo("Game Over", f"Total Prize Won: ₹{self.total_prize}")
  
#   def run(self):
#     self.window.mainloop()

# if __name__ == "__main__":



  # game = QuizGame()
  # game.run()
  
# a = int(input("enter the first number"))
# b = int(input("enter the second number"))
# a =1
# b =1
# def calculation( a=5, b=6 ):
#   c=a+b
#   print(c)
# calculation(a , b)
# print("do it chenging or not")
# print("so now lets tes agian it working or not ")
# school=[ 1, 2,3, 4]
# for i in school:
#   print(i)
#   if i == 3:
#     break
# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#   if x == "big":
#     break
#   for y in fruits:
#     print(x, y)
    
# a = "danish"
# for i in range(1):
#   print(a + "hello")
  
# school= ["ssh", 3, 4, "bkvm" ,5 ,3,1]
# print(school[-1])
# if "ssh" in school:
#   print("yes ther is ")
# else:
#   print("no ther is not")

# print(school[0:7:2])

# new_list=[i for i in range(12) if i%3==0]
# print(new_list)
'''starting list method'''
# list1=[2,1,4,6,5,9,10]
# list1.sort()
# list1.sort(reverse=True)
# list1.append(3)
# list1.reverse()
# print(list1)
# print(list1.count(2))
# list2=list1.copy()
# list2[2]=10
# print(list2)
# list1.insert(3, "danish")
# print(list1)
# list1.extend(list2)
# print(list1)
'''learning tupple now'''
# a = (2,3,4,4,4,)
# print(type(a), a)
# b = a
# # b[0]=19  tupple can not be modified
# print(b)
# b = a[1:4]
# print(b)
# if 3 in a:
#   print("yes 3 is in tupple list variable of a")
# import time
# t = int(time.strftime("%H"))
# print(t)

# if (t>0 and t<12):
#   print("good mornign sir welcome")
# elif(t>12 and t<17):
#   print("good afternoon sir")
# else: 
#   print("gooad evening sir ")
'''Leraning f string '''
# string= "my name is {} khan and im form {}"
# name= "danish"
# country="nepal"
# print(string.format(name,country))
# name = str(input("Enter Your name "))
# country = str(input("Enter Your name "))
# letter = f"My name is {name} and im form {country}"
# print(letter)
'''learnign doc string'''
# def name(n):
#   '''This is doc string i have already written before learnig any thing but we can print it if its in any function but it should be right after the string '''
#   print(n**56)
  
# name(3)
# print(name.__doc__)

'''Recursion The best example is factorial'''
# a=int(input("inter the number for factorial value"))

# def factorial(n):
#   if (n==0 or n==1):
#     return 1
#   else:
#     return n * factorial(n-1)
# result=factorial(a)
# print(result)
# print(f"this is the value of your desire number factorial {result}")

# '''fibonacci'''
# a=int(input("inter the number for factorial value"))

# def fibonacci(f):
#   if (f==0 ):
#     return 0
#   elif (f==1):
#     return 1
#   else:
#     return fibonacci(f-1) + fibonacci(f+1)
# result=factorial(a)
# print(result)
# print(f"this is the value of your desire number fibonacci {result}")

'''Today We Will learn Set in Python'''
# a = {"danish", "danish", "khan"}
# print(f"this a set, set helps to store only original value it do not store duplicate value {a}")

'''set method'''
# s1 = {2,3,4,5,6}
# s2 = {3,6,2,7,8,9}
# print(s1.union(s2))
# s1.update(s2)
# print(s1)
# print(s1.isdisjoint(s2))
# s1.add(9)
# print(s1)
# print()

'''starting dictionay in python'''
dic = {
  "name": "danish",
  "age": 21,
  "semester": 3,
  "lcID": "lc0016001000"
}

print(dic)
print(dic.get("lcID"))