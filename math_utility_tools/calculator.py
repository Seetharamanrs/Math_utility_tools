class calculator:
    def __init__(self)->None:
        pass
    def sub(self,a,b):
        return a-b
    def mult(self,a,b):
        return a*b
    def div(self,a,b):
        if b==0:
            return "Enter the valid division"
        return a/b 
    def pow(self,a):
        return a**2
    def fact(self,a):
        if a<0:
            return "Doesn't takenegative values"
        sum=1
        i=1
        while i<=a:
            sum=sum*i
            i+=1
        return sum
    def squareroot(self,a):
        return round(a**(0.5),3)

