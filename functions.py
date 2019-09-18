import re


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

# binding a variable
a1 = None


def bind_a_variable():
    global a1
    a1 = []


bind_a_variable()
print(a)


def f():
    a = 5
    b = 6
    c = 7
    return {'a': a, 'b': b, 'c': c}


print(f())

states = ['   Alabama ', 'Georgia!', 'Georgia', 'georgia', 'FlOrIda', 'south   carolina##', 'West virginia?']


def clean_strings(strings):
    result = []
    for value in strings:
        value = value.strip()  # strip will eliminate spaces
        value = re.sub('[!#?@$]', '', value)
        value = value.title()
        result.append(value)
    return result


print(clean_strings(states))


def rec_Function(n):
    if n != 0:
        print(n)
        return rec_Function(n - 1)
    else:
        return print('The value is 0!')


rec_Function(5)


def remove_punctuation(value):
    return re.sub('[!@#$%]', '', value)


clean_ops = [str.strip, remove_punctuation, str.title]


def clean_strings(strings, ops):
    result = []
    for value in strings:
        for function in ops:
            value = function(value)
        result.append(value)
    return result


print(clean_strings(states, clean_ops))


def valid_paranthisis(str_paran):
    tmp_str = str_paran
    for s in str_paran:
        print(s)
    return


valid_paranthisis("{[()]}")


def lambda_func():
    for x in map(remove_punctuation, states):
        print(x.strip().title())
    return


lambda_func()


def lambda_func1(x):
    return x * 2


print(print(lambda_func1(2)))


def apply_to_list(some_list, f):
    return [f(x) for x in some_list]


ints = [4, 0, 1, 2, 3]
print(apply_to_list(ints, lambda x: x * 2))


def add_numbers(x, y):
    return x + y


add_five = lambda y: add_numbers(5, y)
print(add_five)
from functools import partial

add_five = partial(add_numbers, 5)
print(add_five)
