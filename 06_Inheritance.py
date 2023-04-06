# ========================= Inheritance =========================


# class A:
#     def __init__(self):
#         print("I am class A")
        
# class B(A):
#     pass

# b = B()

# class User:
#     def __init__(self, fn, ln, email, country):
#         self.first_name = fn
#         self.last_name = ln
#         self.email = email
#         self.country = country
        
#     def home(self):
#         return f"{self.first_name} from {self.country}"
    
# class Student(User):
#     def __init__(self, fn, ln, email, country, school):
#         # User.__init__(self, fn, ln, email, country)
#         super().__init__(fn, ln, email, country)
#         self.school = school

#     def study(self):
#         return f"{self.first_name} studies at {self.school}"
        
        
# student_one = Student("Ahmad", "Omar", "ao@gmail.com", "Sudan", "Test School")

# print( student_one.home() )

# print( student_one.study() )


# class A:
#     def __init__(self):
#         print("A")

# class B:
#     def __init__(self):
#         print("B")

# class C(A, B):
#     pass

# c = C()


# print(C.mro())


# class A:
#     pass

# class B(A):
#     pass


# class C(B):
#     pass