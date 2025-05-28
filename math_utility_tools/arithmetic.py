class arithmetic_sequence:
      def __init__(self,a,d,n):
        self.a=a
        self.d=d
        self.n=n
      def a_series(self):
        curr=self.a
        for i in range(1,self.n+1):
            print(curr,end=" ")
            curr=curr+self.d