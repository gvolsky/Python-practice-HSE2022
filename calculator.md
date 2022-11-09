# Calculator class

+ [Calculator class of comlex number](#calculator class of comlex number)
+ [Tests for Calculator class](#tests for Calculator class)

## Calculator class of comlex number

Класс вычислений с комплексными числами

```python 
from math import sqrt
class Calculator:
    def __init__(self, real, image):
        self.real = real
        self.image = image

    def __add__(self, __o: object):
        return Calculator(self.real + __o.real, self.image + __o.image)

    def __mul__(self, __o: object):
        return Calculator(self.real * __o.real - self.image * __o.image,
                          self.real * __o.image + self.image * __o.real)

    def __sub__(self, __o: object):
        return Calculator(self.real - __o.real, self.image - __o.image)

    def __truediv__(self, __o: object):
        numerator1 = self.real * __o.real + self.image * __o.image
        numerator2 = self.image * __o.real + self.real * __o.image
        denominator = (__o.real)**2 + (__o.image)**2
        return Calculator(numerator1 / denominator, numerator2 / denominator)

    def __eq__(self, __o: object) -> bool:
        return (self.real == __o.real) and (self.image == __o.image)

    def __str__(self):
        if self.image == 0:
            return '%.2f' % self.real
        if self.real == 0:
            return '%.2f' % self.image
        if self.image < 0:
            return '%.2f - %.2fi' % (self.real, -self.image)
        if self.image > 0:
            return '%.2f + %.2fi' % (self.real, self.image)

    def mod(self):
        return sqrt(self.real**2 + self.image**2)

```
## Tests for Calculator class
