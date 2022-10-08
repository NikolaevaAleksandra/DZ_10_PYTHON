class Road:
def__init__(self,length,wight):
self.length=length
self.wight=wight

def func(self,weight,thickness):
    return self.length*self.wight*weight*thickness/1000
a=Road(10.10)
print(a.func(20,20))