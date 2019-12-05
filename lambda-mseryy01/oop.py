class Person:
    ### Namee and age tracking ###

    def __init__(self, personName, personAge):
        self.name = personName
        self.age = personAge

    def showName(self):
        print("My name is" + self.name)

    def showAge(self):
        years = self.age + 1
        print("I am " + years + " years old")


person1 = Person("Mike", 32)
person2 = Person("Sara", 41)

person1.showAge()
person2.showName()
