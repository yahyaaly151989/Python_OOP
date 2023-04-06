# ========================= Object Methods =========================

class User:
    def __init__(self, fn, ln, email, phone):
        self.first_name = fn
        self.last_name = ln
        self.email = email
        self.phone = phone
    
    def login(self):
        return f"{self.first_name} is singing in."
    
    def logout(self):
        return f"{self.first_name} is signing out."
    
    
user_one = User("Yehya", "Ali", "ya@yahoo.com", "123456789")

print( user_one.login() )
print( user_one.logout() )




