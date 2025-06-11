import cmath
class quadratic_equ:
  def __init__(self, a,b,c):
    if a==0:
        raise ValueError("Invalid 'a' can't be zero in quadratic equation")
    self.a=a
    self.b=b
    self.c=c
  def equation(self):
    result =f"Equation: {self.a}x**2+{self.b}x+{self.c}"
    d=(self.b**2)-(4*self.a*self.c)
    sqrt=cmath.sqrt(abs(d))
    if d>0:
      result+="\nThe equation has two distinct real roots " 
      X1=((-self.b+sqrt)/(2*self.a))
      X2=((-self.b-sqrt)/(2*self.a))
      result+=f" X1={X1:.2f} , X2={X2:.2f} "
    elif d==0:
          x=-self.b/(2*self.a)
          result+=" The equation has one double root: X={x:.2f} "
    else:
      result+="  The equation has the complex root and real root "
      x1=complex((-self.b/(2*self.a)),sqrt/(2*self.a))
      x2=complex((-self.b/(2*self.a)),-sqrt/(2*self.a))
      result+=f"  {x1:.2f} and {x2:.2f} "
    return result