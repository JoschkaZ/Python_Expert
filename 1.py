

# some behaviour that I want to implement -> write some __function__
# also called "dundermethods" or "datamodelmethods"
# common pattern: top-level function or top level syntax -> corresponding __function
# x+y -> __add__
# init x __init__
# repr(x) -> __repr__
# x() -> __call__

# python data model is a means by which protocols can be implemented.
# protocols have some abstract meaning depending on the object
# for each case: a protocol exist, there is some __ method to implement it
# there is some top level function (like len) or syntax (like +) that allows to invoce that protocol

# there are 4 core patterns in object orientation in python
# protocol view, built in inheritance protocol, caveats around object orientation



class Polynomial:
    def __init__(self, *coeffs):
        self.coeffs = coeffs

    def __repr__(self):
        return 'Polynomial(*{!r})'.format(self.coeffs)

    def __add__(self, other):
        return Polynomial(*(x + y for x, y in zip(self.coeffs, other.coeffs)))

    def __len__(self):
        return len(self.coeffs)

    def __call__(self):
        pass



p1 = Polynomial(1, 2, 3)
p2 = Polynomial(3, 4, 3)


print(p1)
print(p2)
print(p1+p2)
print(len(p1))
