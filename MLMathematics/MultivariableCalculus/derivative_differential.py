# INT-8
# Copyright from Sharebee.cn Inc, All rights reserved.
# Author: Samuel
# Reference:https://gitbook.cn/gitchat/column/5ddcf0b079b8c11c31370e76/topic/5de6175a2e9f5b62b090977c

def function(x):
    return x*x

def numerical_diff(f, x):
    h = 1e-4
    return (f(x+h) - f(x))/h

def numerical_diff_1(f,x):
    h = 1e-4
    return (f(x+h/2) - f(x-h/2))/h

print('theoretical value= {}'.format(2*4))
print('value={},error={}'.format(numerical_diff(function, 4),abs(numerical_diff(function, 4)-8)))
print('value={},error={}'.format(numerical_diff_1(function, 4),abs(numerical_diff_1(function, 4)-8)))
