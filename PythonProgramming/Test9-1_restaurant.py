# Date: June 15, 2021
# Copyright from Sharebee.cn Inc All Rights Reserved
# Author: Samuel
# Reference: https://www.dedao.cn/pwa/#/reader?id=V5R16yPmaYOMqGRAv82jkX4KDe175w7eomWrbx6pNgznl9VZPLJQyEBodb89mqoO

from Restaurant import Restaurant

restaurant = Restaurant('KFC', 'Hamburg')

print(restaurant.restaurant_name.title(), restaurant.cuisine_type)

print("I like " + restaurant.restaurant_name.title() + '`s' + ' ' + restaurant.cuisine_type.title()  + '.')

