class staticstools:
    def __init__(self,a:list):
        self.a=a.copy()
    def mean(self):
        return (sum(self.a)/len(self.a))
    def median(self):
        c=sorted(self.a)
        n=len(c)
        mid=n//2
        if n%2 ==0:
            return (c[mid-1]+c[mid])/2
        else:
            return c[mid]
    def mode(self):
        d={}
        for i in self.a:
            d[i]=d.get(i,0)+1
        mx=max(d.values())
        modes=[i for i, j in d.items() if j==mx]
        return modes if len(modes)>1 else modes[0]
    def rang(self):
        c=sorted(self.a)
        return c[-1]-c[0]