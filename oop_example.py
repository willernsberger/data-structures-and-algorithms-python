# an example of inheritance in python


class Thing(object):
    def __init__(self):
        pass

    def reveal_identity(self):
        print("I am just a thing.")


class Person(Thing):
    def __init__(self, name):
        super(Person, self).__init__()
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


pencil = Thing()
bill = Person("William Ernsberger")
superman = SuperHero("Clark Kent", "SuperMan")

pencil.reveal_identity()
bill.reveal_identity()
superman.reveal_identity()