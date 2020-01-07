from abc import abstractmethod,ABC

class bmw(ABC):
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    
    def start(self):
        print("starting the car")
    
    def stop(self):
        print("Stopping the car")
    @abstractmethod                   #decorator
    def drive(self):
        pass
        
#interface is class with all methods as abstract methods        
        
class threeseries(bmw):
    def __init__(self,cr,make,model,year):
        #bmw.__init__(self,make,model,year)    ONE WAY TO INITAILISE PARENT CLASS
        super().__init__(make,model,year)     #initialise using super()
        self.cruisecontrolenabled=cr
    def display(self):
        print("cruise controlled enabled",self.cruisecontrolenabled)
    def start(self):
        super().start()                     #constructor of parent class
        print("starting the car with button")
    def drive(self):
        print("THREE SERIES IS BEING DRIVEN")
        
        
class fiveseries(bmw):
    def __init__(self,pa,make,model,year):
        bmw.__init__(self,make,model,year)
        #super().__init__(make,model,year)    #both method are correct
        self.parkingassistenabled=pa
    def drive(self):
        print("FIVE SERIES IS BEING DRIVEN")
        
        
t=threeseries(True,"BMW","328i",2017)
print(t.cruisecontrolenabled,t.make,t.model,t.year)

f=fiveseries(True,"BMW","320i",2016)
print(f.parkingassistenabled)
t.start()
t.stop()
t.display()
t.start()          #OVERRIDING THE FUNCTION
t.drive()
f.drive()
"""
b=bmw("BMW","328i",2017)
Can't instantiate abstract class bmw with abstract methods drive
"""