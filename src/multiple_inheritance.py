class Person:
    def talk(self):
        print('Hello')

class Car:
    def run(self):
        print('boon')


class Molcar(Person, Car):
    def talk(self):
        print('Pui Pui')

    def eat(self):
        print('eating...')

molcar = Molcar()
molcar.talk()
molcar.eat()
molcar.run()