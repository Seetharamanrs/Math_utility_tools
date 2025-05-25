import cmath
class quadratic_equ:
  def __init__(self, a,b,c):
    if a==0:
        raise ValueError("Invalid 'a' can't be zero in quadratic equation")
    self.a=a
    self.b=b
    self.c=c
  def equation(self):
    print(f"{self.a}x**2+{self.b}x+{self.c}")
    d=(self.b**2)-(4*self.a*self.c)
    sqrt=cmath.sqrt(abs(d))
    if d>0:
      print("The equation has two distinct real roots")
      print("X1=",((-self.b+sqrt)/(2*self.a)))
      print("X2=",((-self.b-sqrt)/(2*self.a)))
    elif d==0:
      print("The equation has one double root",-self.b/(2*self.a))
    else:
      print("The equation has the complex root and real root")
      x1=complex((-self.b/(2*self.a)),sqrt/(2*self.a))
      x2=complex((-self.b/(2*self.a)),-sqrt/(2*self.a))
      print(f"{x1} and {x2}")