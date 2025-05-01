import unittest
from projects.project3 import drink as Drink
from projects.project3 import menu as Menu


class TestDrink(unittest.TestCase):
    def test_price_calculation(self):
        drink = Drink("Cold Brew", "medium")
        expected_price = 3.00 + 0.50  # base + kind
        self.assertAlmostEqual(drink.get_price(), expected_price)

    def test_invalid_kind(self):
        with self.assertRaises(ValueError):
            Drink("Nonexistent", "small")

    def test_invalid_size(self):
        with self.assertRaises(ValueError):
            Drink("Cold Brew", "extra large")


class TestMenu(unittest.TestCase):
    def setUp(self):
        self.kinds = ["Cold Brew", "Bearcat Mocha"]
        self.sizes = ["small", "medium"]
        self.menu = Menu(self.kinds, self.sizes)

    def test_menu_structure(self):
        drink = self.menu.get_drink("Cold Brew", "small")
        self.assertIsInstance(drink, Drink)
        self.assertEqual(drink.kind, "Cold Brew")
        self.assertEqual(drink.size, "small")

    def test_invalid_drink_lookup(self):
        with self.assertRaises(ValueError):
            self.menu.get_drink("Nonexistent", "medium")

        with self.assertRaises(ValueError):
            self.menu.get_drink("Cold Brew", "extra large")

    def test_menu_string_output(self):
        output = str(self.menu)
        self.assertIn("Cold Brew", output)
        self.assertIn("Small", output)


if __name__ == '__main__':
    unittest.main()
