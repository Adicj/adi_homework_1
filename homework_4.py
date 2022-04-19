def reduce_fraction(m, n):
    while m % n != 0:
        old_m = m
        old_n = n

        m = old_n
        n = old_m % old_n
    return n


class Fraction:
    def __init__(self, n, d):
        self.num = int(n / reduce_fraction(abs(n), abs(d)))
        self.den = int(d / reduce_fraction(abs(n), abs(d)))
        if self.den < 0:
            self.den = abs(self.den)
            self.num = -1*self.num
        elif self.den == 0:
            raise ZeroDivisionError

    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den + self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        return Fraction(new_num, new_den)

    def __sub__(self, other_fraction):
        new_num = self.num * other_fraction.den - self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        return Fraction(new_num, new_den)

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def invert(self):
        return Fraction(self.den, self.num)


x1 = Fraction(5, 18)
x2 = Fraction(2, 3)
x3 = x1 + x2
x4 = x1 - x2
x5 = Fraction.invert(x1)

print('First fraction is: ', x1, 'Second fraction is: ', x2)
print('Sum of fraction is: ', x3)
print('Subtract of fraction is: ', x4)
print('Inverted first fraction is: ', x5)
