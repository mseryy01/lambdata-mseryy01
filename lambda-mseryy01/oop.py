class Person:
    ### Name and Age tracking#

    def __init__(self, Name, Age):
        self.name = Name
        self.age = Age

    def show_name(self):
        return print('My name is ' + self.name)

    def show_age(self):
        years = self.age + 1
        return print("I will be " + years + "years old next year")
