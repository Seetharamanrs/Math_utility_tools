from calculator import calculator
from geometry import geometry,geometric_sequence
from Quadrtic_solver import quadratic_equ
from staticstools import staticstools
from main import main
from arithmetic import arithmetic_sequence
from fibonacci import fibonacci

def main():
    calc=calculator()
    geo=geometry()
    fib=fibonacci()
    while True:

        print("\n---Math Utility Tools---")
        print("1.Calculator")
        print("2.Geometry")
        print("3.statics tools")
        print("5.Quadratic equation")
        print("5.Arithmetic_sequence")
        print("6.Geometric_sequence")
        print("7.Fibonacci_sequence")
        print("8.Exit")
        choice=input("Enter the choice (1-8): ")

        if choice=="1":
            print("Options: add , sub, mult, div, square, fact, squareroot")
            o=input("Enter the method to perform: ")
            a=int(input("Enter the number:"))
            b=int(input("Enter the number (if needed):"))if o not in ["square","factorial","squareroot"] else None

            if o=="add":
                print(a+b)
            elif o=="sub":
                print(calc.sub(a,b))
            elif o=="div":
                print(calc.div(a,b))
            elif o=="multi":
                print(calc.mult(a,b))
            elif o=="fact":
                print(calc.fact(a))
            elif o=="square":
                print(calc.pow(a))
            elif o=="squareroot":
                print(calc.squareroot(a))
            else:
                print("Invalid Enter correctly!!")


        elif  choice=="2":
            print("Shapes:circle,rect,traingle")
            s=input("Enter the shape: ")

            if s=="circle":
                r=float(input("Enter the radius"))
                print(geo.circle(r))
            elif s=="rect":
                l=float(input("Enter the length of the rectangle: "))
                w=float(input("Enter the width of the rectangle: "))
                print(geo.rect(l,w))
            elif s=="traingle":
                a=float(input("side A: "))
                b=float(input("base B:  "))
                c=float(input("side C: "))
                h=float(input("Height h: "))
                print(geo.traingle(a,b,c,h))
            else:
                print("Enter the valid shape!!")
            
        elif choice=="3":
            a=list(map(int,input("Enter the number by sperated space: 4").split()))
            stat=staticstools(a)
            print("Mean: ",stat.mean())
            print("Mode: ",stat.mode())
            print("Median: ",stat.median())
            print("range: ",stat.rang())
        elif choice=="4":
            a,b,c=map(int,input("Enter the number by commas:").split(","))
            qua=quadratic_equ(a,b,c)
            qua.equation()
        elif choice =="5":
            a=int(input("Enter the starting number: "))
            d=int(input("Enter the range: "))
            n=int(input("Enter the end number: "))
            ar=arithmetic_sequence(a,d,n)
            ar.a_series()

        elif choice=="6":
            a=int(input("Enter the starting number: "))
            r=int(input("Enter the range: "))
            n=int(input("Enter the end number: "))
            gr=geometric_sequence(a,r,n)
            gr.g_series()
        elif choice=="7":
            a=int(input("Enter the count: "))
            fib.fib(a)
        elif choice=="8":
            print("Thank you for using Toolkit :)")
            break
        else:
            print("Invalid option!!")
if __name__=="__main__":
    main()