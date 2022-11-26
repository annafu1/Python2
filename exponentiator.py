# def exponentiate (x, y):
#     x = int(2)
#     y = int(2)
#     return x ** y

# def raise_to_fourth_power(y2):
#     y2 = int(4)
#     return exponentiate ** y2

def raise_to_fourth_power(exponent):
    def raise_x(x):
        return x ** exponent ** exponent
    return raise_x

def exponentiate(exponent):
    def raise_x(x):
        return x ** exponent
    return raise_x

square = exponentiate(2)
square(2)

cube = exponentiate(3)
cube(2)
cube(3)

square = raise_to_fourth_power(2)
square(2)