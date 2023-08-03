from project.shopping_cart import ShoppingCart
import unittest


class TestShoppingCart(unittest.TestCase):

    def setUp(self) -> None:
        self.tesco = ShoppingCart("Tesco", 500)
        """
        self.shop_name = Tesco
        self.budget = 500
        self.products = {}   {"Product Name": 10}   name/price
        """
        self.aldi = ShoppingCart("Aldi", 500)
        """
        self.name = Aldi
        self.budget = 500
        self.products = {}
        """

    def test__correct_initialization(self):
        self.assertEqual("Tesco", self.tesco.shop_name)
        self.assertEqual(500, self.tesco.budget)
        self.assertEqual({}, self.tesco.products)

    def test__shop_name_sets_correctly__raises_if_not(self):
        self.tesco.shop_name = "TescoExtra"
        self.assertEqual("TescoExtra", self.tesco.shop_name)

        # Test firs letter not upper
        with self.assertRaises(ValueError) as ve:
            self.tesco.shop_name = "tesco"
        expected_result = "Shop must contain only letters and must start with capital letter!"
        self.assertEqual(expected_result, str(ve.exception))

        # Test all characters are letters
        with self.assertRaises(ValueError) as ve:
            self.tesco.shop_name = "Tesco1"
        expected_result = "Shop must contain only letters and must start with capital letter!"
        self.assertEqual(expected_result, str(ve.exception))

        # Test no space between
        with self.assertRaises(ValueError) as ve:
            self.tesco.shop_name = "Tesc o"
        expected_result = "Shop must contain only letters and must start with capital letter!"
        self.assertEqual(expected_result, str(ve.exception))

    def test__add_to_cart_everything_valid__adds_to_cart(self):
        result = self.tesco.add_to_cart("Beer", 20)

        expected_result = {"Beer": 20}
        self.assertEqual(expected_result, self.tesco.products)
        self.assertEqual("Beer product was successfully added to the cart!", result)

    def test__add_to_cart_expensive_item__raises(self):
        # with self.assertRaises(ValueError) as ve:
        #     self.tesco.add_to_cart("Water", 100)
        # self.assertEqual("Product Water cost too much!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.tesco.add_to_cart("Water", 101)
        self.assertEqual("Product Water cost too much!", str(ve.exception))

    def test__remove_from_cart_data_correct__removes_product_returns_message(self):
        self.tesco.products = {"Water": 10, "Beer": 20}
        result = self.tesco.remove_from_cart("Water")

        self.assertEqual({"Beer": 20}, self.tesco.products)
        expected_string = "Product Water was successfully removed from the cart!"
        self.assertEqual(expected_string, result)

    def test__remove_from_cart_product_not_in_cart__raises(self):
        self.tesco.products = {"Water": 10}
        with self.assertRaises(ValueError) as ve:
            self.tesco.remove_from_cart("Beer")
        self.assertEqual("No product with name Beer in the cart!", str(ve.exception))

    def test__add_dunder_method__creates_new_shop_adds_carts_together(self):
        self.tesco.products = {"Water": 10}
        self.aldi.products = {"Beer": 20}

        result = self.tesco.__add__(self.aldi)

        self.assertEqual("ShoppingCart", result.__class__.__name__)
        self.assertEqual("TescoAldi", result.shop_name)
        self.assertEqual(1000, result.budget)
        self.assertEqual({"Water": 10, "Beer": 20}, result.products)

    def test__buy_product_correct_values__buys_products_returns_message(self):
        self.tesco.products = {"Water": 10, "Beer": 40}

        result = self.tesco.buy_products()
        expected_result = f'Products were successfully bought! Total cost: 50.00lv.'
        self.assertEqual(expected_result, result)

    def test__buy_product_price_over_budget__raises(self):
        self.tesco.products = {"Water": 500, "Beer": 10}

        with self.assertRaises(ValueError) as ve:
            self.tesco.buy_products()

        expected_result = "Not enough money to buy the products! Over budget with 10.00lv!"
        self.assertEqual(expected_result, str(ve.exception))









