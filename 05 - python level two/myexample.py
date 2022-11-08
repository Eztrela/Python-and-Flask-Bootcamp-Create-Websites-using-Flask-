#=================================== DOG ========================================



# class Dog():

#     #CLASS OBJECT ATTRIBUTES
#     species = 'mammal'

#     def __init__(self,breed,name) -> None:
#         self.breed = breed
#         self.name = name

# sam = Dog('Huskie', 'Sammy')



#=================================== CIRCLE ========================================

# class Circle():

#     pi = 3.14

#     def __init__(self,radius = 1) -> None:
#         self.radius = radius
    
#     def area(self):
#         return self.radius * self.radius * self.pi

#     def circumfrence(self):
#         return 2*self.pi*self.radius

# mycircle = Circle(10)
# print(mycircle.radius)
# print(mycircle.area())
# print(mycircle.circumfrence())


#=================================== HERANÇA ========================================


class Animal():
    def __init__(self,fur) -> None:
        self.fur = fur
    
    def report(self):
        print('Animal')
    def eat(self):
        print('Eating')

class Dog(Animal):
    def __init__(self,fur) -> None:

        Animal.__init__(self,fur)
        print('Dog Created')

    def report(self):
        print('I am a dog')

d = Animal('Fuzzy')
d.eat()
