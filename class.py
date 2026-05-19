#example1
class fruit:
    def __init__(self,color):
        self.color=color
        
apple=fruit("red")
print(apple.color)

#example2
class teacher:
    def __init__(self,name,reg):
        self.name=name
        self.regno=reg
    def display(self):
        print("name",self.name)
        print("reg no",self.regno)

t1=teacher("thomes","1")
t2=teacher("john","2")

t1.display()
t2.display()
