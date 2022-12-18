from math import sqrt
from complex import Complex
import unittest


class TestComplexNumber(unittest.TestCase):


    def numbers(self) -> None:
        self.one = Complex(1, 2)
        self.two = Complex(2, 1)
        self.three = Complex(1, 2)

    def add(self):
            result = self.one + self.two
            self.assertEqual(result.real, self.one.real + self.two.real)
            self.assertEqual(result.image, self.one.image + self.two.image)
    def mul(self):
        result = self.one * self.two
        self.assertEqual(result.real, self.one.real * self.two.real 
                                        - self.one.image * self.two.image)
        self.assertEqual(result.image, self.one.real * self.two.image 
                                        + self.one.image * self.two.real)

    def sub(self):
        result = self.one - self.two
        self.assertEqual(result.real, self.one.real - self.two.real)
        self.assertEqual(result.image, self.two.image - self.two.image)

    def mod(self):
        self.assertEqual(self.one.mod(), sqrt(self.one.real ** 2 + self.one.image ** 2))

    def equiv(self):
        self.assertEqual(self.one == self.two, False)
        self.assertEqual(self.one == self.three, True)


if __name__ == '__main__':
    unittest.main()
