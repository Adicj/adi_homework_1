def reduce(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n


class Fraction:
    def __init__(self, n, d):
        self.num = int(n / reduce(abs(n), abs(d)))
        self.denom = int(d / reduce(abs(n), abs(d)))
        if self.denom < 0:
            self.denom = abs(self.denom)
            self.num = -1*self.num
        elif self.denom == 0:
            raise ZeroDivisionError

    def __add__(self, otherfraction):

        newnum = self.num * otherfraction.denom + self.denom * otherfraction.num
        newden = self.denom * otherfraction.denom
        return Fraction(newnum, newden)

    def __sub__(self, otherfraction):
        newnum = self.num * otherfraction.denom - self.denom * otherfraction.num
        newden = self.denom * otherfraction.denom
        return Fraction(newnum, newden)

    def __str__(self):
        if type(self) is tuple:
            if self[1] < 0:
                return '%s/%s' % (self[0], -1 * self[1])
            else:
                return '%s/%s' % (self[0], self[1])
        elif self.denom == 1:
            return str(self.num)
        else:
            return '%s/%s' % (self.num, self.denom)

    def invert(self):
        return Fraction(self.denom, self.num)


x1 = Fraction(4, 3)
x2 = Fraction(2, 3)
x3 = x1 + x2
x4 = x1 - x2
x5 = Fraction.invert(x1)

print('First fraction is: ', x1, 'Second fraction is: ', x2)
print('Sum of fraction is: ', x3)
print('Substract of fraction is: ', x4)
print('Inverted first fraction is: ', x5)



