# ========================= Object Attributes =========================

class User:
    
    def __init__(self, fn, ln, email, phone):
        
        self.first_name = fn
        self.last_name = ln
        self.email = email
        self.phone = phone
    
    
user_one = User("Yehya", "Ali", "ya@yahoo.com", "123456789")

user_tow = User("Ahmad", "Omar", "ao@yahoo.com", "987654321")

print( user_one.first_name, user_one.last_name, user_one.email, user_one.phone )

print( user_tow.first_name, user_tow.last_name, user_tow.email, user_tow.phone )
