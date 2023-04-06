# ========================= @Property Decorator =========================

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def welcome(self):
        return f"Welcome {self.name}."
    
    @property
    def my_age(self):
        return self.age
    
person_one = Person("Yehya", 33)

# print( person_one.name )
# print( person_one.age )

# print( person_one.welcome() )

print( person_one.my_age() )

print( person_one.my_age )