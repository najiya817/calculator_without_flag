class Parent_class:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print("name:",self.name)
        print("age:",self.age)
class Child_class(Parent_class):
    def __init__(self,name,age,city):
        super().__init__(name,age)
        self.city=city
    def show(self):
       super().show()
       print("city:",self.city)



class GrandChild_class(Child_class):
    def __init__(self,name,age,city,country):
        super().__init__(name,age,city)
        self.country=country
    def show(self):
       super().show()
       print("country:",self.country)


p=Parent_class("John",30)
p.show()
c=Child_class("John",30,"New York")
c.show()
g=GrandChild_class("John",21,"New York","USA")
g.show()