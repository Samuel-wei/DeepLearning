# Date: June 15, 2021
# Copyright from Sharebee.cn Inc All Rights Reserved
# Author: Samuel
# Reference: https://www.dedao.cn/pwa/#/reader?id=V5R16yPmaYOMqGRAv82jkX4KDe175w7eomWrbx6pNgznl9VZPLJQyEBodb89mqoO

from car import Car
from electric_car import ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('telsa', 'roadster', 2016)
print(my_tesla.get_descriptive_name())

#