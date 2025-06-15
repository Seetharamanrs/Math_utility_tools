pi=3.1415
class geometry:
  def __init__(self) -> None:
    pass
  def circle(self,r):
    return f"The area of circle is {round(pi*((r)**2),2)} and circumference is{2*pi*r}"
  def rect(self,l,w):
    return f"The area of rectangle is {l*w} and circumference is {(2*l)+(2*w)}"
  def traingle(self,a,b,c,h):
    return f"The area of the traingle is {round(0.5*b*h,2)} and perimeter is {a+b+c}"
class geometric_sequence:
    def __init__(self,a,r,n):
        self.a=a
        self.r=r
        self.n=int(n)
    def g_series(self):
        a=[]
        for i in range(1,self.n+1):
            tn=self.a*(self.r**(i-1))
            a.append(tn)
        return a