def my_function(x, y, z=1.5):
    if z > 1:
        return z * (x + y)
    else:
        return z / (x + y)


print(my_function(10, 20, z=0.7))
print(my_function(x=32, y=56, z=0.8))

a = []


def func():
    for i in range(10):
        a.append(i)


func()
print(a)
