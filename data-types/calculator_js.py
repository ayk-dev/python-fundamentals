def calculate(x, y, operation):
    result = eval(x + operation + y)
    return result


a = input()
b = input()
operator = input()

print(calculate(a, b, operator))

