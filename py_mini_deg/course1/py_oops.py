class Animal(object):
    def speak(self):
        print('Speak')

class Lion(Animal):
    def __init__(self):
        self.type = 'Cat'
    def speak(self):
        print('Roar')

simba = Lion()
print(simba.type)
#super(Lion,simba).speak()
#Lion.speak(simba)
simba.speak()

animal = Animal()
animal.speak()
