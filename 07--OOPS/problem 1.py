class Twovector():
    def __init__(self,i,j):
        self.i = i
        self.j = j
    
    def show(self):
        print(f"the two d vector is {self.i}i {self.j}j ")

class Threevector(Twovector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k
        super().show()

    def show(self):
        print(f"the three d vector is {self.i}i {self.j}j {self.k}k")

a = Threevector(2,3,4)
a.show()