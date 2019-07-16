#construtor and destructor are optional.
#The constructor is typically to set up the varibales.

class Partyanimal:
    x = 0
    name = ''
#constructor with addition parameters z
    def __init__(self,z):
        self.name  = z
        print('I am constructed', self.name)   # called when object created

#method
    def party(self):
        self.x = self.x +1
        print('%s so far %d :'% (self.name,self.x))

#destructor
    def __del__(self):
        print(self.name,' am destructed ',self.x)


cn = Partyanimal('cn') #create a object and set up instance varible
an = Partyanimal('an') #create a object and set up instance varible
an.party()  #call method
an.party()
cn.party()
an = 42     #destruct the object and reassign 42 into an variable
print('an contains ', an)
print(type(cn))
