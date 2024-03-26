# creating classes in python
class Person:
    def __init__(self):
        self.name = "Michael"
        self.age = 23
        self.gender = "male"

    def introduce(self):
        print("Hello i am",  self.name, "i am", self.age, "years old and i am a",  self.gender )


p1 = Person()
print(p1.introduce())


