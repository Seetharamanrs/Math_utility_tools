class arithmetic_sequence:
      def __init__(self,a,d,n):
        self.a=a
        self.d=d
        self.n=n
      def a_series(self):
        e=[]
        curr=self.a
        for i in range(1,(self.n)+1):
          e.append(curr)  
          curr=curr+self.d
        return e