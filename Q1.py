#F111 KEISHNA SHARMA

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def print(self):
       print("My name is ",name)    
       print("My age is ",age)

    def greet(self):
      print("name",self.name)
      print("age",self.age)
       

p=person("krishna",19)
p.greet()



