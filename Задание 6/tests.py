from math import sqrt
from complex import Complex
import unittest


class TestComplexNumber(unittest.TestCase):


    def setUp(self) -> None:
        self.one = Complex(1, 2)
        self.two = Complex(2, 1)
        self.three = Complex(1, 2)

    def test_add(self):
        result = self.one + self.two
        self.assertEqual(result.real, self.one.real + self.two.real)
        self.assertEqual(result.image, self.one.image + self.two.image)

    def test_mul(self):
        result = self.one * self.two
        self.assertEqual(result.real, self.one.real * self.two.real 
                                        - self.one.image * self.two.image)
        self.assertEqual(result.image, self.one.real * self.two.image 
                                        + self.one.image * self.two.real)

    def test_sub(self):
        result = self.one - self.two
        self.assertEqual(result.real, self.one.real - self.two.real)
        self.assertEqual(result.image, self.one.image - self.two.image)

    def test_mod(self):
        self.assertEqual(self.one.mod(), sqrt(self.one.real ** 2 + self.one.image ** 2))

    def test_equiv(self):
        self.assertEqual(self.one == self.two, False)
        self.assertEqual(self.one == self.three, True)

    def test_div(self):
        numerator1 = self.one.real * self.two.real + self.one.image * self.two.image
        numerator2 = self.one.image * self.two.real + self.one.real * self.two.image
        denominator = (self.two.real) ** 2 + (self.two.image) ** 2
        result = self.one / self.two
        self.assertEqual(result.real, numerator1 / denominator)
        self.assertEqual(result.image, numerator2 / denominator)

    def test_str(self):
        self.assertEqual('1.00 + 2.00i', str(self.one))


if __name__ == '__main__':
    unittest.main()
