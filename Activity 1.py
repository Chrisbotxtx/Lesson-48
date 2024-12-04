class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def info(self):
        return "I am {} and my age is {} years old".format(self.name,self.age)
    
    def make_sound(self):
        return "I bark at the strangers"
    
d=Dog("Leon",3)
print(d.info())
print(d.make_sound())

class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def info(self):
        return "I am {} and my age is {} years old".format(self.name,self.age)
    
    def make_sound(self):
        return "I meow when i'm hungry"
    
d=Dog("Leon",3)
print(d.info())
print(d.make_sound())

c=Cat("Kitty",5)
print(c.info())
print(c.make_sound())