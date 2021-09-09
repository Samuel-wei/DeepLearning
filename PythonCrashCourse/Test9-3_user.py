# Date: June 15, 2021
# Copyright from Sharebee.cn Inc All Rights Reserved
# Author: Samuel
# Reference: https://www.dedao.cn/pwa/#/reader?id=V5R16yPmaYOMqGRAv82jkX4KDe175w7eomWrbx6pNgznl9VZPLJQyEBodb89mqoO

from user import User

user1 = User('Samuel', 'wei', 'male', '38')
user2 = User('Wanda', 'wang', 'female', '30')

messages1 = user1.describe_user()
messages2 = user2.describe_user()

greet1 = user1.greet_user()
greet2 = user2.greet_user()

print(messages1, messages2)
print(greet1, greet2)


