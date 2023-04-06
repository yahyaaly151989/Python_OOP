# ========================= ABCs Abstract Base Class =========================

from abc import ABCMeta, abstractmethod


class Programming(metaclass=ABCMeta):
    @abstractmethod
    def has_oop(self):
        pass
    
    def test(self):
        return "Test"
    
class Python(Programming):
    def has_oop(self):
        return "Yes"

    
# class C(Programming):
#     def has_oop(self):
#         return "No"
    
p_one = Python()

print( p_one.has_oop() )

print( p_one.test() )