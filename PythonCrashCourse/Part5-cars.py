# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # part 5  if 语句
# %% [markdown]
# ## 5.1 一个简单的示例

# %%
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# %% [markdown]
# ## 5.2 条件测试
# %% [markdown]
# ### 5.2.1 检查是否相等

# %%
car = 'bmw'
car == 'bmw'


# %%
car = 'audi'
car == 'bmw'

# %% [markdown]
# ### 5.2.2 检查是否相等时不考虑大小写

# %%
car = 'Audi'
car == 'audi'


# %%
car = "Audi"
car.lower() == 'audi'


# %%
print(car)

# %% [markdown]
# ### 5.2.3 检查是否不相等

# %%
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

# %% [markdown]
# ### 5.2.4 比较数字

# %%
age = 18
age == 18


# %%
answer = 17

if answer != 42:
    print("That is not the correct answer. Please try angin!")


# %%
age = 19


# %%
age < 21


# %%
age <= 21


# %%
age > 21


# %%
age >= 21

# %% [markdown]
# ### 5.2.5 检查多个条件

# %%
age_0 = 22
age_1 = 18


# %%
age_0 >= 21 and age_1 >= 21


# %%
age_1 = 22
age_0 >= 21 and age_1 >= 21 


# %%
(age_0 >= 21) and (age_1 >= 21)


# %%
age_0 = 22
age_1 = 18


# %%
(age_0 >= 21) or (age_1 >= 21)


# %%
age_0 = 18


# %%
(age_0 >= 21 or age_1 >= 21)

# %% [markdown]
# ### 5.2.6 检查特定值是否包含在列表中

# %%
requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings


# %%
'pepperoni' in requested_toppings

# %% [markdown]
# ### 5.2.7 检查特定值不包含在列表中

# %%
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.") 

# %% [markdown]
# ### 5.2.8 布尔表达式

# %%
game_active = True
can_edit = False

# %% [markdown]
# ## 动手试一试

# %%
car = 'subaru'
car == 'subaru'


# %%
car == 'audi'


# %%
car == 'toyota'


# %%
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')


# %%
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')


# %%
boss = 'samuel'
boss == 'samuel'


# %%
boss == 'Samuel'


# %%
boss.lower() == 'Samuel'


# %%
boss = 'Samuel'
boss.lower() == 'samuel'


# %%
age_1 = 18
age_0 = 22


# %%
age_1 <= 22


# %%
age_0 < 32


# %%
age_1 >= 33


# %%
age_1 >= 18 and age_0 <= 22


# %%
age_1 < 18 or age_0 > 18


# %%
cars = ['bmw', 'audi', 'subaru', 'toyota']
'byd' in cars


# %%
'byd' not in cars


# %%
if 'byd' not in cars:
    print('That is a good car')

# %% [markdown]
# ## 5.3 if语句
# %% [markdown]
#  ### 5.3.1 简单的if语句

# %%
age = 19 

if age >= 18:
    print('You are old enough to vote!')


# %%
print("You are old enough to vote!")
print("Have you registered to vote yet!")

# %% [markdown]
# ### 5.3.2 if-else语句

# %%
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

# %% [markdown]
# ### 5.3.3 if-elif-else结构

# %%
age = 12

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")


# %%
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print("Your admission cost is $" + str(price) +".")

# %% [markdown]
# ### 5.3.4 使用多个elif代码块

# %%
age = 60

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
    
print("Your admission cost is $" + str(price) + ".")

# %% [markdown]
# ### 5.3.5 省略else代码块

# %%
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10 
elif age >= 65:
    price = 5

print("Your admission cost is $" + str(price) + ".")

# %% [markdown]
# ### 5.3.6 测试多个条件

# %%
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
    
print("\nFinished making your pizza!")


# %%
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
    
print("\nFinished making your pizza!")

# %% [markdown]
# ## 动手试一试

# %%
alien_color = ['green', 'yellow', 'red']

if 'green' in alien_color:
    point = 5

print("Player point " + str(point) + ".")


# %%
alien_color = ['green', 'yellow', 'red']

if 'blue' in alien_color:
    print("Player point " + str(point) + ".")


# %%
alien_color = ['green', 'yellow', 'red']

if 'green' in str(alien_color):
    point = 5
    print("Player point " + str(point) + ".")


# %%
alien_colors = ['green', 'yellow', 'red']

player = 'blue'
if player in str(alien_colors):
    player = 5
    print("Player point " + str(player) + ".")
else:
    player = 10
    print("Player point " + str(player) + ".")


# %%
player = 'green'

if player == 'blue':
    player = 5
    print("Player point " + str(player) + ".")
elif player == 'yellow':
    player = 10
    print("Player point " + str(player) + ".")
else:
    player = 15
    print("Player point " + str(player) + ".")


# %%
age = 65

if age < 2:
    print("He was a baby!")
elif age < 4:
    print("He was a toddler!")
elif age < 13:
    print("He was a children!")
elif age < 20:
    print("He was a teenager!")
elif age <= 65:
    print("He was a adults!")
elif age > 65:
    print("He was a elderly!")
    


# %%
fruits = ['apples', 'bananas', 'oranges', 'watermelons', 'pineapples']

if 'watermelons' in fruits:
    print("I favorite fruit is watermelon!")
    


# %%
favorite_fruits = fruits[-3:]
print(favorite_fruits)


# %%
fruits = ['apples', 'bananas', 'oranges', 'watermelons', 'pineapples']

if 'apples' in fruits:
    print("You really like " + 'apples' + "!")
if 'bananas' in fruits:
    print("You really like " + 'bananas' + "!")
if 'watermelons' in fruits:
    print("You really like " + 'watermelons' + "!")
if 'oranges' in fruits:
    print("You really like " + 'oranges' + "!")
if 'pineapples' in fruits:
    print("You really like " + 'pineapples' + "!")

# %% [markdown]
# ## 5.4 使用if语句处理列表
# %% [markdown]
# ### 5.4.1 检查特殊元素

# %%
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print("Adding" + requested_topping + ".")

print("\nFinish making your pizza!")


# %%
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green pepper right now.")
    else:
        print("\nAdding" + requested_topping + ".")
        
print("\nFinish making your pizza!")

# %% [markdown]
# ### 5.4.2 确定列表不是空的

# %%
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding" + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza!")

# %% [markdown]
# ### 5.4.3 使用多个列表

# %%
available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'French fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding" + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("\nFinishded making your pizza!")

# %% [markdown]
# ## 动手试一试

# %%
users = ['admin', 'administration', 'samuel', 'wanda', 'alice']

for user in users:
    print("Hello " + user + ", welcome to sharebee.cn!")


# %%
users = ['admin', 'administration', 'samuel', 'wanda', 'alice']

for user in users:   
    if user == 'admin':
        print("Hello " + user + " , would you like to see a status report?")


# %%
users = ['admin', 'administration', 'samuel', 'wanda', 'alice']

for user in users:   
    if user == 'admin':
        print("Hello " + user + " , would you like to see a status report?")
    else:
        print("Hello " + user + ", thank you for logging in again!")


# %%
users = []

if users:
    for user in users:   
        print("Hello " + user + ", thank you for logging in again!")
else:
    print("We need to find some users!")


# %%
current_users = ['admin', 'administration', 'samuel', 'wanda', 'alice']
new_users = ['Admin', 'administration', 'dabing', 'arlington', 'andrew']

for new_user in new_users:
    if new_user.lower() in current_users:
        print("The " + new_user.lower() + " is existed, please use another name.")
    else:
        print("The " + new_user.lower() + " is supporting!")


# %%
numbers = [1,2,3,4,5,6,7,8,9]

for number in numbers:
    print(number)


# %%
numbers = [1,2,3,4,5,6,7,8,9]

for number in numbers:
    if number == 1:
        print(str(number) + 'st')
    elif number == 2:
        print(str(number) + 'nd')
    elif number == 3:
        print(str(number) + 'rd')
    else:
        print(str(number) + 'th')


# %%



