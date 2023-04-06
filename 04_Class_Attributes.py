# ========================= Class Attributes =========================

class User:
    
    users_count = 0
    
    def __init__(self, fn):
        self.first_name = fn
        
        User.users_count += 1
    

print( User.users_count )

user_one = User("Yehya")
user_two = User("Yehya")
three = User("Yehya")

print( User.users_count )




