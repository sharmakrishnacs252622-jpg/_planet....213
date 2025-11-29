#F111 krishna sharma

class MyClass:
    
    def method_one(self):
        print("Inside method_one")
        
        result = self.method_two()
        
        print("Value returned from method_two:", result)
    
    def method_two(self):
        print("Inside method_two")
        return 42

obj = MyClass()

obj.method_one()
