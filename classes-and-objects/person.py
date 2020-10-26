class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print(f'Hi, my name is {self.name}')


albena = Person('Albena')
jordan = Person('Jordan')
maria = Person('Maria')

albena.say_hi()
jordan.say_hi()