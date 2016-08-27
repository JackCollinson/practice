# set value 100 to variable 'car'
cars = 100
# set value 4 to variable 'space_in_a_car'
space_in_a_car = 4
# set value 30 to variable 'drivers'
drivers = 30
# set value 90 to variable 'passengers'
passengers = 90
# set variable cars_not_driven to the  difference of the values
# assigned to cars and drivers
cars_not_driven = cars - drivers
# set variable cars_driven equal to value stored in variable drivers
cars_driven = drivers
# set variable carpool_capacity to the product of the values
# stored in variables cars_driven and space_in_a_car
carpool_capacity = cars_driven * space_in_a_car
# set variable average_passengers_per_car to the quotient of
# passengers and cars_driven
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
