print("Hello world")

class Employee:

    def __init__(self, name, age):
        self.name = name
        self.age = age


Leo = Employee("Leo", 23)
Max = Employee("Maxwell", 26)

print(Leo.name, "is", Leo.age, "old.")
print(Max.name + " is", Max.age, "old")