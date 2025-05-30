import random
class guess_number:
  def __init__(self):
    self.t=random.randint(1,100)
  def guess(self,n):
    print("Guess the number between 1 to 100")
    for i in range (10):
      try:
        guess=int(input(f"Attempt {i+1}"))
        if guess==self.t:
          print("Awesome that correct")
          return
        elif guess <self.t:
          print("The guess is low")
        else:
          print("The guess is high")
      except ValueError:
        print("Enter the valid number!!")
    print(f"Sorry! The correct number was {self.target}.")