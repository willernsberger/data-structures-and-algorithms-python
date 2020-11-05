# example inheritance

class Person(object):
    def __init__(self, name):
        self.name = name

    def reveal_identity(self):
        print("My name is " + self.name + ".")


class SuperHero(Person):
    def __init__(self, name, hero_name):
        super(SuperHero, self).__init__(name)
        self.hero_name = hero_name

    def reveal_identity(self):
        super(SuperHero, self).reveal_identity()
        print("And I am " + self.hero_name + ".")


Bill = Person('William Ernsberger')
SuperMan = SuperHero('Clark Kent', 'SuperMan')

Bill.reveal_identity()
SuperMan.reveal_identity()
