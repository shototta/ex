def chose_operation(n:int):
    def square(x):
        return x*x
    def cubic(x):
        return x*x*x
    if n == 2:
        return square
    if n == 3:
        return cubic
print(chose_operation(2)(5))