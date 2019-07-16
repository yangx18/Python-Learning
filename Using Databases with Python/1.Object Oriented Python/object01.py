
#class and object

# create a class named Partyanimal
class Partyanimal:

    x = 0
#Method
    def party(self):
        self.x = self.x + 1
        print('so far :' ,self.x)

#Create an object an for Partyanimal
an = Partyanimal()
an.party()  # call the method
an.party()
print(an.x) #print the object an's varible x.
print('type: ', type(an)) #print the type of an
print('dir : ', dir(an))  #print the dir in an
