# ========================= Class Methods =========================

class User:
    
    @staticmethod
    def welcome():
        return "Welcome to the application."
    
    users_count = 0
    
    @classmethod
    def show_users(cls):
        return f"We have {cls.users_count} users in our system."
    
    def __init__(self, fn):
        self.first_name = fn
        
        User.users_count += 1
    

print( User.users_count )

user_one = User("Yehya")
user_two = User("Ahmad")
user_three = User("Maher")
user_four = User("Mona")


print( User.show_users() )


print( User.welcome() )

