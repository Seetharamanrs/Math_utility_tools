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
    print(f"Sorry! The correct number was {self.t}.")
  def dice_roller(self):
    return random.randint(1,6)
  def lottery(self,s,n):
    a=set()
    while len(s)<=n-1:
      a.add(random.randint(1,s))
    return s
  def coin_toss(self):
    return "Head" if random.randint(0,1)==0 else "Tail"
