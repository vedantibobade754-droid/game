# object = A "bundle" of related attributes (variable) ad methods (functions)
# ex. phone, cup, book
# you need a "class" to create many object

from car import Car

car1 = Car("Mustang", 2026, "yellow", False)
car2 = Car("Lamborgini", 2027, "red", True)
car3 = Car("Farrari",2028, "white", True)

car1.drive()
car2.stop()
car3.describe()


