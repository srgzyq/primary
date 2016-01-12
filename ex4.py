# -*- coding: utf-8 -*- #
# 车辆数目 100
cars = 100
# 每辆车车装载人数 4人
space_in_a_car = 4.0
# 司机人数
drivers = 30
# 乘客人数
passengers = 90
# 无法驾驶的车辆，没有司机
cars_not_driven = cars - drivers
# 能驾驶的车辆
cars_driven = drivers
# 运载能力 乘客数量
carpool_capacity = cars_driven * space_in_a_car
# 每辆车平均装载乘客数
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars avaailable."
print "There are only", drivers, "drivers avaailable."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpooll today."
print "We need to put about", average_passengers_per_car, "in each car."
