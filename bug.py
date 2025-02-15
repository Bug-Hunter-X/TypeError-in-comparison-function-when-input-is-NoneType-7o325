def my_function(a, b):
    if a > b:
        return a
    return b

result = my_function(5, 2)
print(result)  # Output: 5

result = my_function(2, 5)
print(result)  # Output: 5

result = my_function(-3, 0)
print(result)  # Output: 0

# Unexpected behavior:
result = my_function(None, 5)
print(result) # Output: TypeError: '>' not supported between instances of 'NoneType' and 'int'