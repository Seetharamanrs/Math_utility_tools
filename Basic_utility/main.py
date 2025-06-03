from unit_conventer import unitconverter
from matrix import matrix
from date_time import dob
from guess_the_number import guess_number
from ceaser_cipher import cipher
from sci_cal import scicalculator
def unit_conv():
    uc=unitconverter()
    print("\n--Unit converter--")
    print("1. Temperature")
    print("2. Weight")
    print("3. Length")
    choice=input("Choose conversion type:")
    a= int(input("Enter the convertion value: "))
    unit=input("Convert to (celsius<->fahrenheit, kg<->lb, km<->miles):")
    if choice=="1":
        print("Results: ", uc.temp(a,unit))
    elif choice=="2":
        print("Results: ", uc.weight(a,unit))
    elif choice=="3":
        print("Results: ", uc.length(a,unit))
    else:
        print("INVALID CHOICE")
def cipher():
  c=cipher()
  print("\n --Cipher Tool--")
  key=int(input("Enter the key:"))
  text=input("Enter the text: ")
  print("1.Encrypt")
  print("2.Decrypt")
  choice=input("Enter the choice: ")
  if choice=="1":
    print("Encrypted message: ",c.en_cipher(key,text))
  elif choice=="2":
    print("Decrypted message: ",c.de_cipher(key,text))
  else:
    print("Enter the valid options!!")
def dob():
  d=dob()
  print("\n--Age and date Calculator--")
  print("1.Age calculator")
  print("2.Time until next birthday or specific day")
  print("3. Difference between two day")
  print("4.Counter timer")
  choice=input("Enter the choice: ")
  if choice=="1":
    y,m,n=map(int,input("Enter the format in YYYY:MM:DD").split(":"))
    print("Age(Y:M:D)", d.do(y,m,n))
  elif choice=="2":
    y,m,n=map(int,input("Enter the format in YYYY:MM:DD").split(":"))
    print("days left: ", d.u_n_b(y,m,n))
  elif choice=="3":
    print("Difference: ",d.d_two())
  elif choice=="4":
    y=float(input("Enter the time in mintues: "))
    d.coutertime(y)
  else:
    print("Invalid option!")
def guess():
  g=guess_number()
  print("\n-- Random Games--")
  print("1.Guess the number")
  print("2.Dice roller")
  print("3.lottery")
  print("4.coin toss")
  choice=input("Enter the choice: ")
  if choice=="1":
    n=int(input("Enter the number attempt you wanna try: "))
    g.guess(n)
  elif choice=="2":
    print("Dice rolled: ",g.dice_roller())
  elif choice=="3":
    s=input("Enter the max number: ")
    n=input("Enter how many number to select: ")
    print("Lottery winners are ", g.lottery(s,n))
  elif choice=="4":
   print("Coin Toss",g.coin_toss())
  else:
    print("Invalid options!")

def sci():
    s=scicalculator()
    print("\n--Scientific calculator--")
    print("1.sin")
    print("2.cos")
    print("3.tan")
    print("4.exp")
    print("5.log")
    choice=input("Enter the choice:")
    if choice  in ["1","2","3","4"]:
        n=float(input("Enter value:"))
        if choice=="1":
            print("Result:", s.sin(n))
        elif choice=="2":
            print("Result:", s.cos(n))
        elif choice=="3":
            print("Result:", s.tan(n))
        elif choice=="4":
            print("Result:", s.exp(n))
    elif choice=="5":
        n=float(input("Enter value:"))
        b=float(input("Enter base:"))
        print("Results:",s.log(n,b) )
    else:
        print("Enter valid option!")
