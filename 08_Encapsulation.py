# ========================= Encapsulation =========================

# # Public
# class Car:
#     def __init__(self, speed):
#         self.speed = speed
        
# car_one = Car(220)
# print(car_one.speed)
# car_one.speed = 300
# print(car_one.speed)

# # Protected
# class Car:
#     def __init__(self, speed):
#         self._speed = speed
        
# car_one = Car(220)
# print(car_one._speed)
# car_one._speed = 300
# print(car_one._speed)

# Private
# class Car:
#     def __init__(self, speed):
#         self.__speed = speed
        
# car_one = Car(220)
# # print(car_one.__speed) # error

# print(car_one._Car__speed)

# car_one._Car__speed = 300

# print(car_one._Car__speed)


# getters and setters

class Car:
    def __init__(self, speed):
        self.__speed = speed
        
    def get_speed(self):
        return self.__speed
    
    def set_speed(self, new_speed):
        self.__speed = new_speed
        
car_one = Car(220)

print(car_one.get_speed())

car_one.set_speed(300)

print(car_one.get_speed())



