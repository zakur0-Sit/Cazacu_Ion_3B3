def my_function(*args, **kwargs):
    return sum(1 for args_elem in args if args_elem in kwargs.values())

print(my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5))