# Date: June 15, 2021
# Copyright from Sharebee.cn Inc All Rights Reserved
# Author: Samuel
# Reference: https://www.dedao.cn/pwa/#/reader?id=V5R16yPmaYOMqGRAv82jkX4KDe175w7eomWrbx6pNgznl9VZPLJQyEBodb89mqoO

class Restaurant():

	# 初始化
	def __init__(self, name, type):

		# 设置两个属性
		self.restaurant_name = name
		self.cuisine_type = type

	def describe_restaurant(self):
		print(self.restaurant_name.title() , self.cuisine_type.title())

	def open_restaurant(self):
		print("The " + self.restaurant_name.tetle() + " is opening!")

#






