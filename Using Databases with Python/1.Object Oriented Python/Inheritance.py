#Inheritance

class Partyanimal():
    name = ''
    x = 0

#constructor
    def __init__(self,z):
        self.name = z
        print(self.name,'Constructor created')

#method
    def party(self):
        self.x = self.x + 1
        print('so far :', self.x)

#Inheritance/subcalsses

class Football(Partyanimal):

    point = 0
#Addition method/ Exstends Partyanimal
    def touchdown(self):
        self.point = self.point + 1
        print(self.name,'points',self.point)
        self.party()


#Objects
s = Partyanimal('cat')
s.party()

j = Football('dog')
j.party()
j.touchdown()

##test for create a subclasses for any known class
#example list:
class alist(list):
    name = ''
    n = 0
    def __init__(self,n):
        self.n = n
        print('the number: ',self.n)

    def haha(self,z):
        self.name = z
        print ('your list name is ', self.name)

xy = alist(5)
xy.append(5)
xy.append(6)
xy.haha('xy')
print(xy)
print(type(xy))
