"""
Variables hold arbitrary information in Python. They can hold numbers, text, or even functions. 
However, an important part of variables and their use is their scope. We shall explore
this in detail in this section.
"""

#Simple use 
a = 1

print(a)

#Variables can be self-referential. On the right hand side a still has the value of 1
a = a+1

print(a)

a = -1

print(a)

a+=1

print(a)

a = 5
b = 5

#Variables are composeable
c = a+b
print(c)

d = a*b

print(d)

#We will explore functions in greater detail soon
def incrementer(variable):
    return variable+1

a = incrementer(1)
print(a)

x = incrementer

a = x(1)
print(a)

#Variables are nestable, meaning that you can put variables inside of others as much as you want
#Triple nested dictionary
nest = {"a":{"a":{"a":"booooo"}}}
print(nest)
print(nest["a"]["a"]["a"])

#variables only exist within the scope in which they are defined. 
# All the variables we have defined so far exist in the so called global scope.
# These variables are always accessible and will never go away
# However, variables inside functions will cease existing once we are outside the function.

def create_var():
    y =1
create_var()

#This will throw an error
print(y)

#Variables inside a function can share the same name as those that are global.
#Avoid naming your variables the same thing to avoid confusion.

