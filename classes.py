class pet:
    def __init__(self , Name, age):
        self.name= Name
        self.age = age

    def show(self):
        print(f"I am {self.name} and my age is {self.age}")
    
class cat(pet):
    def speak(self):
        print("Meeow!")

class dog(pet):
    def speak(self):
        print("Woooff!")

p = pet("Tommy", 10)
p.show()

c = cat("bill", 3)
c.show()
c.speak()
d = dog("musky",2)
d.show()
d.speak()
