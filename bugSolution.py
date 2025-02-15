def my_function(a, b):
    try:
        if a > b:
            return a
        return b
    except TypeError:
        if a is None:
            return b
        elif b is None:
            return a
        else:
            return None  # Or raise a more informative exception

result = my_function(5, 2)
print(result)  # Output: 5

result = my_function(2, 5)
print(result)  # Output: 5

result = my_function(-3, 0)
print(result)  # Output: 0

result = my_function(None, 5)
print(result)  # Output: 5

result = my_function(5, None)
print(result) # Output: 5

result = my_function(None, None)
print(result) # Output: None