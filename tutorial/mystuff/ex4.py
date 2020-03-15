cars = 100
space_in_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_car
average_passengers_per_car = passengers / cars_driven
#the variables with integers can be printed with strings if separated by commas.
print("there are",cars,"cars available.")
print("there are only", drivers, "drivers available.")
print("there will be",cars_not_driven,"empty cars today")
print("we will transport",carpool_capacity,"which is the cap")
print("passengers today are",passengers,"today")
print("average transit of people today is",average_passengers_per_car)
