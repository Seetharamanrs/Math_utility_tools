import streamlit as st
from calculator import calculator
from geometry import geometry, geometric_sequence
from Quadrtic_solver import quadratic_equ
from staticstools import staticstools
from arithmetic import arithmetic_sequence
from fibonacci import fibonacci

def main():
    calc=calculator()
    geo=geometry()
    fib=fibonacci()
    st.title(" Math Utility Tools")
    tools=[ "Calculator",
        "Geometry",
        "Statistics Tools",
        "Quadratic Equation",
        "Arithmetic Sequence",
        "Geometric Sequence",
        "Fibonacci Sequence"]
    choice=st.selectbox("",tools)
    if choice=="Calculator":
        st.subheader("Basic Calculator")
        operations=st.selectbox("operation",["add", "sub", "mult", "div", "square", "fact", "squareroot"])
        a=st.number_input("Enter the number a")
        if operations in ["add","sub","multi","div"]:
            b=st.number_input("Enter the number b")
        if st.button("Calculate"):
            if operations=="add":
                st.success(f"Results:{a+b}")
            elif operations == "sub":
                st.success(f"Result: {calc.sub(a, b)}")
            elif operations == "mult":
                st.success(f"Result: {calc.mult(a, b)}")
            elif operations == "div":
                st.success(f"Result: {calc.div(a, b)}")
            elif operations == "square":
                st.success(f"Result: {calc.pow(a)}")
            elif operations == "fact":
                st.success(f"Result: {calc.fact(a)}")
            elif operations == "squareroot":
                st.success(f"Result: {calc.squareroot(a)}")
    elif choice=="Geometry":
        st.subheader("Simple Geometry calculator")
        shape=st.selectbox("Shapes",["Circle","Rectangle","Traingle"])
        if shape=="Circle":
            r=st.number_input("Enter the radius")
            if st.button("Calculate"):
                st.success(geo.circle(r))
        elif shape=="Rectangle":
            l=st.number_input("Enter the height")
            w=st.number_input("Enter the width")
            if st.button("Calculate"):
                st.success(geo.rect(l,w))
        elif shape=="Traingle":
            a=st.number_input("Side A")
            b=st.number_input("Base b")
            c=st.number_input("Side C")
            h=st.number_input("Height H")
            if st.button("Calculate"):
                st.success(geo.traingle(a,b,c,h))
    elif choice=="Statistics Tools":
        st.subheader("Statistics Tools")
        nums=st.text_input("Enter numbers separated by comma")
        if nums:
            data=list(map(int,nums.split(",")))
            stat=staticstools(data)
            me=stat.mean()
            mo=stat.mode()
            l="  ".join(str(i) for i in mo)
            md=stat.median()
            ran=stat.rang()
            st.text("Mean")
            st.success(me)
            st.text("mode")
            st.success(l)
            st.text('Median')
            st.success(md)
            st.text('range')
            st.success(ran)
    elif choice=="Quadratic Equation":
        st.subheader("Quadratic Equation")  
        a=st.number_input("a",value=1)
        b=st.number_input("b",value=2)
        c=st.number_input("c",value=3)
        qua=quadratic_equ(a,b,c)
        if st.button("solve"):
            st.success(qua.equation())
    elif choice=="Arithmetic Sequence":
        st.subheader("Arithmetic Sequence")
        a=st.number_input("Enter the starting number",value=1)
        d=st.number_input("Enter the range",value=2)
        n=st.number_input("Enter the end number",value=5)
        ar=arithmetic_sequence(a,d,n)
        ae=ar.a_series()
        if st.button("Generate"):
            a=", ".join(str(i)for i in ae)
            st.write(a)
    elif choice=="Geometric Sequence":
        st.subheader("Geometric Sequence")
        a=st.number_input("Enter the starting number",value=1)
        d=st.number_input("Enter the range",value=2)
        n=st.number_input("Enter the end number",value=5)
        gr=geometric_sequence(a,d,n)    
        se=gr.g_series()
        if st.button("Generate"):
            l=", ".join(str(val) for val in se  )
            st.success (l)
    elif choice=="Fibonacci Sequence":
        st.subheader("Fibonacci Sequence")
        count=st.number_input("Enter the number of count",value=5)
        fb=fib.fib(count)
        if st.button("Generate"):
            f="  ".join(str(val)for val in fb)
            st.success(f)
    
    
if __name__=="__main__":
    main()