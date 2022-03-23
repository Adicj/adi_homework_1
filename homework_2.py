print('This is my 2\'nd homework!')


def my_complete_sum(a, b):
    a = 0
    return sum(x for x in range(a, b))


def my_even_sum(a, b):
    a = 0
    return sum(x for x in range(a, b) if x % 2 == 0)


def my_odd_sum(a, b):
    a = 0
    return sum(x for x in range(a, b) if x % 2 == 1)


print('My sum for all the numbers inside a range is: ', my_complete_sum(99, 11))
print('My sum for even numbers inside a range is: ', my_even_sum(1, 5))
print('My sum for even numbers inside a range is: ', my_odd_sum(1000000, 10))
