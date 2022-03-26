# Să se scrie o funcție care primește un număr nedefinit de parametrii și să se calculeze suma parametrilor care reprezintă
#numere întregi sau reale.


def parameter_sum(*args, **kwargs):
    z = []
    for x in args:
        try:
            if x == int(x):
                z.append(x)
        except ValueError:
            pass
        except TypeError:
            pass
    return 0 + sum(z)


# Să se scrie o funcție recursivă care primește ca parametru un număr întreg și returnează:
# suma tuturor numerelor de la [0, n]
# suma numerelor pare de la [0, n]
# suma numerelor impare de la [0. n]


def sum_of_even_no(n):
    if n == 0:
        return 0
    if n % 2 == 1:
        return sum_of_even_no(n - 1)
    else:
        return n + sum_of_even_no(n - 1)


def sum_odd_no(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return sum_odd_no(n - 1)
    else:
        return n + sum_odd_no(n - 1)


def sum_all_numbers(n):
    if n == 0:
        return 0
    return n + sum_all_numbers(n - 1)


# Să se scrie o funcție care citește de la tastatură și returnează valoarea
# dacă aceasta este un număr întreg, altfel returnează
# valoarea 0.


def valid_number():
    number = input('Insert number: ')
    try:
        number = int(number)
    except ValueError:
        number = 0
    return number


print('Multiple args: ', parameter_sum(1, 5, -3, 'abc', [12, 56, 'cad']))
print('Multiple args, kwargs: ', parameter_sum(2, 4, 'abc', param_1=2))
print('No args, kwargs: ', parameter_sum())
print('Sum of even numbers recursive function: ', sum_of_even_no(7))
print('Sum of odd numbers recursive function: ', sum_odd_no(7))
print('Sum of all numbers recursive function: ' , sum_all_numbers(7))
print('User input validation as int: ', valid_number())