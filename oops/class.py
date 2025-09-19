class Car:

    def __init__(self, name, model, price):
        self.name = name
        self.model = model
        self.price = price

    def output(self):
        print(self.name)

    def input(self):
        print(self.model)


car1 = Car()
car1.output()

car1.input()

print(car1.price)
print(type(car1))
