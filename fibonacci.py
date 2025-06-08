class fibonacci:
    def __init__(self):
        pass
    def fib(self,n):
        i=0
        j=1
        sum=0
        for z in range(1,n+1):
            sum=i+j
            i,j=j,sum
            print(sum,end=" ")