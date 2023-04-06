# ====================== Bank System ======================
import datetime

class User:
    @staticmethod
    def welcome():
        print("Welcome to the Bank.")
    
    def __init__(self):
        User.welcome()
        self.first_name = input("First Name. ").strip().capitalize()
        self.last_name = input("Last Name. ").strip().capitalize()
        self.id = str(datetime.datetime.now()).replace("-", "").replace(" ", "").replace(":", "").replace(".", "")
        self.balance = 0
        print(f"Hello {self.first_name} {self.last_name}, your id is {self.id}")
        
class Bank(User):
    def __init__(self):
        super().__init__()
        self.deposite()
        self.choose_options()
        
    def deposite(self):
        print(f"You have $ {self.balance}.")
        self.amount = int(input("Enter a number ").strip())
        self.balance += self.amount
        print(f"You have $ {self.balance}.")
        
    def withdraw(self):
        print(f"You have $ {self.balance}.")
        self.amount = int(input("Enter a number ").strip())
        
        if self.amount > self.balance:
            print("You can not.")
        else:
            (f"You have $ {self.balance}.")
            self.balance -= self.amount
            (f"You have $ {self.balance}.")
        
    def exit(self):
        print("Bye.")
        
    def choose_options(self):
        while True:
            self.choose_option = input("Select an option: 1 => deposite | 2 => witdraw | 3 => exite ")
            if self.choose_option == "1":
                self.deposite()
            elif self.choose_option == "2":
                self.withdraw()
            else:
                self.exit()
                break
            
            
user_one = Bank()

        



