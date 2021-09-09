# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# ## 4.4 使用列表的一部分
# %% [markdown]
# ### 4.4.1 切片

# %%
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])


# %%
print(players[1:4])


# %%
print(players[:4])


# %%
print(players[2:])


# %%
print(players[-3:])

# %% [markdown]
# ### 4.4.2 遍历切片

# %%
players = ['charles', 'martina', 'micheal', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# %% [markdown]
# ### 4.4.3 复制列表

# %%
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)

print("\nMy friends favorite foods are:")
print(friend_foods)


# %%
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friends favorite foods are:")
print(friend_foods)


# %%
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# %% [markdown]
# ## 动手试一试

# %%
players = ['samuel','charles', 'martina', 'michael', 'florence', 'eli','ana']
print("The first three items in the list are:")
print("\n", players[:3])


# %%
print("There items from the middle of the list are:")
print("\n", players[2:-2])


# %%
print("The last three items in the list are:")
print('\n', players[-3:])


# %%
my_pizzas = ["neapolitan_pizza", "chicago_pizza", "sicilian_pizza"]
friend_pizzas = my_pizzas[:]
my_pizzas.append('greek pizza')
print(my_pizzas)


# %%
friend_pizzas.append('detroit pizzas')
print(friend_pizzas)


# %%
print("My favorite pizzas are:")
for pizza in my_pizzas[:]:
    print(pizza)
    
print("\nMy friend's favorite pizzas are: ")
for pizza in friend_pizzas[:]:
    print(pizza)


# %%
my_pizzas = ["neapolitan_pizza", "chicago_pizza", "sicilian_pizza","detroit pizzas","greek pizza"]
for pizza in my_pizzas[:4]:
    print(pizza)
    
for pizza in my_pizzas[-2:]:
    print(pizza)


# %%



