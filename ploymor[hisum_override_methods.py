class shoppingbag:
    def __init__(self,A,B,C):
        self.A=A
        self.B=B
        self.C=C

    def __len__(self):
        return self.A*2+self.B+self.C*2
    def __add__(self, other):
        return  self.A*2+self.B
