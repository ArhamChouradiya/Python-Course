class product:
    def __init__(self):
        self.name = 'iphone'
        self.description = 'good'
        self.price = 700
       
    def display(self):
        print(self.name,self.description,self.price)
        
        
        
        
p1 = product()

print(p1.name)
print(p1.description)
print(p1.price)
#product.display(p1)    '''one way to use'''
p1.display()