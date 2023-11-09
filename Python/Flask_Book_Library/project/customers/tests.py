import unittest
from project.customers.models import Customer

def make_customer(name, city):
    Customer(name, city, "39")

class TestNameValidation(unittest.TestCase):
    @unittest.expectedFailure
    def test_name_re_err(self):
        make_customer("<script></script>", "City")
        make_customer("anything<a />", "City")

    @unittest.expectedFailure
    def test_name_len_err(self):
        make_customer("", "City")
        make_customer("123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890", "City")

    def test_name_re_ok(self):
        make_customer("Name", "City")
        make_customer("Alph4Num3ric5 and friends'.-,", "City")

    def test_name_len_ok(self):
        make_customer("1234567890123456789012345678901234567890123456789012345678901234", "City")


class TestCityValidation(unittest.TestCase):
    @unittest.expectedFailure
    def test_city_re_err(self):
        make_customer("Name", "<br>")
        make_customer("Name", "Robert'); DROP TABLE Books;--")
        make_customer("Name", "<script></script>")

    @unittest.expectedFailure
    def test_city_len_err(self):
        make_customer("Name", "")
        make_customer("Name", "123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890")

    def test_city_re_ok(self):
        make_customer("Name", "City")
        make_customer("Name", "Alph4Num3ric5 and friends'.-,")

    def test_city_len_ok(self):
        make_customer("Name", "1234567890123456789012345678901234567890123456789012345678901234")

if __name__ == "__main__":
    unittest.main()
