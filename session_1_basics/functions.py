"""Functions are one of the most fundamental building blocks in any programming languages.
They are self contained packets of logic. In Python it is optional if they return a value or not."""

a = 1
b = 1

def print_variable(variable):
    print(variable+1)

def incrementer(variable):
    return variable+1

print_variable(a)
a = incrementer(a)
print(a)

#Functions are composeable, meaning that you can call feed the return of one function into another

def multiplier(variable1, variable2):
    return variable1*variable2

def decrementer(variable):
    return variable-1

result = incrementer(
    multiplier(2,
    decrementer(a)))
print(result)
#If something is between two (,[, or {, then we can write it over multiple lines
#Try to separate independent logic into its own function, and then call it in a larger function

def big_function(variable):
    decrease = decrementer(variable)
    triple = multiplier(3, decrease)
    increment = incrementer(triple)
    return increment

print(big_function(a))