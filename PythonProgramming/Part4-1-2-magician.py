# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# ## 4.2 避免缩进错误

# %%
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# %% [markdown]
# ### 4.2.2  忘记缩进而外的代码行

# %%
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was great trick!")
print("I can't wait to see your next trick," + magician.title() + ".\n")


# %%
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was great trick!")
    print("I can't wait to see your next trick," + magician.title() + ".\n")

# %% [markdown]
# ### 4.2.3 不必要的缩进

# %%
message = "Hello Python world!"
print(message)

# %% [markdown]
# ### 4.2.4 循环后不必要的缩进

# %%
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ",that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
    print("Thank you everyone, that was a great magic show!")


# %%
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ",that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Thank you everyone, that was a great magic show!")

# %% [markdown]
# ### 4.2.5 遗漏了冒号

# %%
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# %% [markdown]
# ### 4-1 动手试一试

# %%
pizzas = ["neapolitan_pizza", "chicago_pizza", "sicilian_pizza"]
for pizza in pizzas:
    print(pizza)


# %%
pizzas = ["neapolitan_pizza", "chicago_pizza", "sicilian_pizza"]
for pizza in pizzas:
    print("I like " + pizza.title() + ".\n")


# %%
pizzas = ["neapolitan_pizza", "chicago_pizza", "sicilian_pizza"]
for pizza in pizzas:
    print("I like " + pizza + " very much!" + ".\n")
print("I really love pizza!")


# %%
poultrys = ['chicken', 'duck', 'goose']
for poultry in poultrys:
    print(poultry)


# %%
poultrys = ['chicken', 'duck', 'goose']
for poultry in poultrys:
    print("A" + poultry + " would make a great animals")


# %%
poultrys = ['chicken', 'duck', 'goose']
for poultry in poultrys:
    print("A" + poultry + " would make a great animals" + ".\n")
print("Any of these poultry also would make a great animals!")

# %% [markdown]
# ## 4.3 创建数值列表
# %% [markdown]
# ### 4.3.1 使用函数range()

# %%



