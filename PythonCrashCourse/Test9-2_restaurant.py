# Date: June 15, 2021
# Copyright from Sharebee.cn Inc All Rights Reserved
# Author: Samuel
# Reference: https://www.dedao.cn/pwa/#/reader?id=V5R16yPmaYOMqGRAv82jkX4KDe175w7eomWrbx6pNgznl9VZPLJQyEBodb89mqoO

from Restaurant import Restaurant

KFC = Restaurant('KFC', 'Hamburg')
McDonald = Restaurant('McDonald', 'The fire chicken')
PizzaHut = Restaurant('PizzaHut', 'pizza')

print(KFC.describe_restaurant())
print(McDonald.describe_restaurant())
print(PizzaHut.describe_restaurant())


