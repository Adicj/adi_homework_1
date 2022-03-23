print('This is my 2\'nd homework!')


def my_complete_sum( b):
    a = 0
    return sum(x for x in range(a, b+1))


def my_even_sum(b):
    a = 0
    return sum(x for x in range(a, b+1) if x % 2 == 0)


def my_odd_sum(b):
    a = 0
    return sum(x for x in range(a, b+1) if x % 2 == 1)


print(f'My sum for all the numbers inside a range is: ', my_complete_sum(3))
print('My sum for even numbers inside a range is: ', my_even_sum(9))
print('My sum for even numbers inside a range is: ', my_odd_sum(10))

