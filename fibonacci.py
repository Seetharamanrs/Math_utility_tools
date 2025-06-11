class fibonacci:
    def __init__(self):
        pass
    def fib(self,n):
        d=[]
        i=0
        j=1
        sum=0
        for _ in range(1,n+1):
            d.append(i)
            sum=i+j
            i,j=j,sum
        return d