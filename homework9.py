import tkinter
import random
import time

def hawkID():
    return("agbarloon")

#Math Functions. All return (problem string, [answer, num1, num2])
def addition(lower, upper):
  number1, number2 = random.randint(lower, upper), random.randint(lower, upper)
  return_string = f"{number1} + {number2} = ?"
  return_numbers = [number1 + number2, number1, number2]
  return return_string, return_numbers

def subtraction(lower, upper):
  number2 = random.randint(lower, upper-1)
  number1 = random.randint(number2, upper)
  return_string = f"{number1} - {number2} = ?"
  return_numbers = [number1 - number2, number1, number2]
  return return_string, return_numbers

def multiplication(lower, upper):
  #override upper limit
  global multi_limit
  upper = multi_limit

  number1, number2 = random.randint(lower, upper), random.randint(lower, upper)
  return_string = f"{number1} * {number2} = ?"
  return_numbers = [number1 * number2, number1, number2]
  return return_string, return_numbers

def division(lower, upper):
  #both numbers must be less than 1000, so lower and upper don't have much use. 50 * 19 is 950, max possible.
  number2 = random.randint(lower+1, 50)
  number1 = number2 * random.randint(0, 19)
  return_string = f"{number1} / {number2} = ?"
  return_numbers = [number1 / number2, number1, number2]
  return return_string, return_numbers

def check_answer():
  global current_answer
  global current_attempts
  global questions_answered
  global all_time_attempts
  user_answer = int(entry_field.get())
  entry_field.delete(0, tkinter.END)
  if user_answer == current_answer:
    feedback_label.configure(text = "That's right! Good job!")
    entry_field.configure(state=tkinter.DISABLED)
    submit_button.configure(state=tkinter.DISABLED)
    questions_answered += 1
  else:
    all_time_attempts += 1
    current_attempts += 1
    feedback_label.configure(text = f"Not Quite. Attempts: {current_attempts}")
  calculate_stats()
  

def new_problem():
  global lower_limit
  global upper_limit
  global current_answer
  global current_attempts
  global questions_attempted
  global all_time_attempts
  global options
  global all_questions
  problem_settings = options.get()
  problem_choices = [addition, subtraction, multiplication, division]
  if problem_settings == 4:
    choice = random.choice(problem_choices)
  else:
    choice = problem_choices[problem_settings]
  new_problem_string, new_problem_numbers = choice(lower_limit, upper_limit)
  timeout = time.time() + 0.5
  did_it_break = False
  while new_problem_string in all_questions:
    new_problem_string, new_problem_numbers = choice(lower_limit, upper_limit)
    if time.time() > timeout:
      did_it_break = True
      break
  all_questions.append(new_problem_string)
  #print(new_problem_string, new_problem_numbers)
  current_problem_label.configure(text = new_problem_string)
  current_answer = new_problem_numbers[0]
  questions_attempted += 1
  all_time_attempts += 1
  calculate_stats()
  if did_it_break:
    current_problem_label.configure(text = "We ran out of problems to give you! Stop doing math!")

  #reset variables and widgets
  entry_field.configure(state=tkinter.NORMAL)
  submit_button.configure(state=tkinter.NORMAL)
  current_attempts = 0

def calculate_stats():
  global questions_attempted
  global questions_answered
  global all_time_attempts
  try:
    accuracy = round(questions_answered * 100 / all_time_attempts, 2)
  except ZeroDivisionError:
    accuracy = "N/A"

  user_stats_label.configure(text = f"Questions Attempted: {questions_attempted}. Questions Answered: {questions_answered}. Average: {accuracy}%")

def quit():
  global questions_answered
  global questions_attempted
  global all_time_attempts
  try:
    accuracy = round(questions_answered * 100 / all_time_attempts, 2)
  except ZeroDivisionError:
    accuracy = "N/A"

  print("Thanks For Playing!")
  print(f"You tried {questions_attempted} questions and answered {questions_answered}.")
  print(f"That means you had an accuracy of {accuracy}.")
  print("Come back soon!")
  window.destroy()

#Initialize global variables
global lower_limit
lower_limit = 0
global upper_limit
upper_limit = 1000
global multi_limit
multi_limit = 100
global current_answer
global current_attempts
current_attempts = 0
global all_time_attempts
all_time_attempts = 0
global questions_attempted
questions_attempted = 0
global questions_answered
questions_answered = 0
global all_questions
all_questions = []



#Initialize GUI
window = tkinter.Tk()
window.title("Math!")

global options
options = tkinter.IntVar()

  #First Row - Problem and Answer Input
frame_main = tkinter.Frame(window)
frame_main.pack()
current_problem_label = tkinter.Label(frame_main, text="current_problem")
current_problem_label.pack(side=tkinter.LEFT)
entry_field = tkinter.Entry(frame_main)
entry_field.pack(side=tkinter.LEFT)
submit_button = tkinter.Button(frame_main, text="Submit", command=check_answer)
submit_button.pack(side=tkinter.LEFT)
  #Second Row - Feedback on User Correctness, New Problem Request
frame_two = tkinter.Frame(window)
frame_two.pack()
feedback_label = tkinter.Label(frame_two, text="")
feedback_label.pack(side=tkinter.LEFT)
new_problem_request_button = tkinter.Button(frame_two, text="New Problem?", command=new_problem)
new_problem_request_button.pack(side=tkinter.LEFT)
  #Third Row - User Stats on Correctness
frame_three = tkinter.Frame(window)
frame_three.pack()
user_stats_label = tkinter.Label(frame_three, text=f"")
user_stats_label.pack(side=tkinter.LEFT)
  #Fourth Row - Problem Type Selection and Quit
frame_four = tkinter.Frame(window)
frame_four.pack()
add_button = tkinter.Radiobutton(frame_four, text = "+", variable = options, value = 0)
add_button.pack(side=tkinter.LEFT)
sub_button = tkinter.Radiobutton(frame_four, text = "-", variable = options, value = 1)
sub_button.pack(side=tkinter.LEFT)
mul_button = tkinter.Radiobutton(frame_four, text = "*", variable = options, value = 2)
mul_button.pack(side=tkinter.LEFT)
div_button = tkinter.Radiobutton(frame_four, text = "/", variable = options, value = 3)
div_button.pack(side=tkinter.LEFT)
all_button = tkinter.Radiobutton(frame_four, text = "All", variable = options, value = 4)
all_button.pack(side=tkinter.LEFT)
all_button.select()
quit_button = tkinter.Button(frame_four, text = "Quit", command = quit)
quit_button.pack()

#Run!
new_problem()
window.mainloop()