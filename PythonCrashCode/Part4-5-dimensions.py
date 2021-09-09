# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# ## 4.5 元组
# %% [markdown]
# ### 4.5.1 定义元组

# %%
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])


# %%
dimensions = (200, 50)
#dimensions[0] = 250

# %% [markdown]
# ### 4.5.2 遍历元组中的所有值

# %%
dimensions = (200,50)
for dimension in dimensions:
    print(dimension)

# %% [markdown]
# ### 4.5.3 修改元组变量

# %%
dimensions = (200,50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)


# %%
dimensions = (400, 100)
print("\nModified dimensions: ")
for dimension in dimensions:
    print(dimension)

# %% [markdown]
# ## 动手试一试

# %%
foods = ("potato", "vegetable", "pizza", "hamburger", "")
for food in foods:
    print(food)


# %%
foods[1] = ("fish")


# %%
foods = ("potato", "fish", "pizza", "beef")
for food in foods:
    print(food)

# %% [markdown]
# ## 4.6 设置代码格式
# %% [markdown]
# ### 4.6.1 格式设置指南

# %%



