class Complex():
    def __init__(self,l):
        self.l = l
    
    def __len__(self):
        return(len(self.l))
    
a = Complex([1,2,3,4,5,8])
print(a.__len__())
# is se hum kissi ki bhi len find kerwa sekta ha 

''' liken python ko batana ho ga ke lenth hoti kia ha humeha usko 
class mein def ke sath define kerta ha '''
    

