class Car():
    # python we call all the method
    # def start(potato):
    #     print(potato.color)
    #     print("This is method")
    def __init__(self, **kwargs):
        self.wheels = 4
        self.doors = 4
        self.windows = 4
        self.seats = 4
        self.color = kwargs.get("color",
        "black")
        self.price = kwargs.get("price",
        "$20")

    def __str__(self):
        return f"Car with {self.wheels} wheels"

# def istart():
#     print("This is function")


# porche = Car()
# porche.color = "Red Sexy Red"
# porche.start()
# this will be running by porche.start(porche)
# def start(self)

# all the property on the method
# print(dir(Car))

# will print in str type
porche = Car(color="green", price="$40")
print(porche.color, porche.price)

#defalt value comes out
mini = Car()
print(mini.color, mini.price)


class Convertible(Car):

    def __init__(self, **kwargs):
        # super class can access all of the class (inheritened)
        super().__init__(**kwargs)
        self.time = kwargs.get("time", 10)

    def take_off(self):
        return "taking off"
    def __str__(self):
        return f"Car with no roof"




# same as print(porche.__str__())

porche = Convertible(color = "green", price = "$40")
print(porche.color)

# if there are no super() then will get
# MESSAGE : AttributeError: 'Convertible' object has no attribute 'color'
# because the 
