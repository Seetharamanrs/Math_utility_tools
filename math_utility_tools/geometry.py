pi=3.1415
class geometry:
  def __init__(self) -> None:
    pass
  def circle(self,r):
    return f"The area of circle is {pi*((r)**2)} and circumference is{2*pi*r}"
  def rect(self,l,w):
    return f"The area of rectangle is {l*w} and circumference is {(2*l)+(2*w)}"
  def traingle(self,a,b,c,h):
    return f"The area of the traingle is {0.5*b*h} and perimeter is {a+b+c}"