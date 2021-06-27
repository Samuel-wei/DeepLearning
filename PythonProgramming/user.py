# Date: June 15, 2021
# Copyright from Sharebee.cn Inc All Rights Reserved
# Author: Samuel
# Reference: https://www.dedao.cn/pwa/#/reader?id=V5R16yPmaYOMqGRAv82jkX4KDe175w7eomWrbx6pNgznl9VZPLJQyEBodb89mqoO

# Create the classes
class User():

	# Initialization the attribute
	def __init__(self, first, last, sex, age):
		
		# Setup the attribut
		self.first_name = first
		self.last_name = last
		self.sex = sex
		self.age = age

	def describe_user(self):

		# Print user's messages
		print(self.first_name.title(), self.last_name.title(), self.sex.title(), self.age.title())

	def greet_user(self):

		# Send a greet words to user
		print('Hello, ' + self.last_name.title() + ' ' + ' welcome to Sharebee corporations!')


		

