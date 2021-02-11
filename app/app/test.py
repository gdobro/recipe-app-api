from django.test import TestCase

from app.calc import add, subtract


class CalcTests(TestCase):
    """example Test Class"""
    def test_add_numbers(self):
        """test the add function"""

        # setup startproject
        # nothing to do in this case

        # assert
        self.assertEqual(add(3, 8), 11)

    def test_subtract_numbers(self):
        """test that numbers are subtracted and returned"""

        self.assertEqual(subtract(7, 4), -3)
