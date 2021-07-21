def decorator(func):
    def decorated(a, b):
        if a >= 0 and b >= 0:
            return func(a, b)
        else:
            raise ValueError('Input must be positive value')
    return decorated

@decorator
def rect_area(a, b):
    return a * b

@decorator
def tri_area(a, b):
    return a * b / 2

rect_area(-10, 10)
tri_area(20, 30)
