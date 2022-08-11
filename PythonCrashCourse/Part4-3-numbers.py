# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# ## 4.3 创建数值列表
# %% [markdown]
# ### 4.3.1 使用函数range()

# %%
for value in range(1,5):
    print(value)


# %%
for value in range(1, 6):
    print(value)

# %% [markdown]
# ### 4.3.2 使用range()创建数字列表

# %%
numbers = list(range(1,6))
print(numbers)


# %%
even_numbers = list(range(2,11,2))
print(even_numbers)


# %%
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)


# %%
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

# %% [markdown]
# ### 4.3.3对数字列表执行简单的统计计算

# %%
digits = [1,2,3,4,5,6,7,8,9,0]
min(digits)


# %%
max(digits)


# %%
sum(digits)

# %% [markdown]
# ### 4.3.4 列表解析

# %%
squares = [value**2 for value in range(1,11)]
print(squares)

# %% [markdown]
# ## 动手试一试

# %%
for numbers in range(1, 21):
    print(numbers)


# %%
millions = []
for million in range(1, 1000001):
    millions.append(million)
print(millions)


# %%
print(min(millions))
print(max(millions))
print(sum(millions))


# %%
odd_numbers = [x for x in range(1,21) if x%2==1 ]
print(odd_numbers)


# %%
multiple_3 = [i for i in range(3, 31) if i%3==0]
print(multiple_3)


# %%
cubic_3 = [i**3 for i in range(1,10)]
print(cubic_3)

# %% [markdown]
# ## 4.4 使用列表的一部分

# %%



