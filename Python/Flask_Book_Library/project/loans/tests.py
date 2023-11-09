import unittest
from project.loans.models import Loan

def make_loan(customer, book):
    Loan(customer, book, "1999-01-01", "1999-01-02", "unused", "unused", "unused")

class TestCustomerValidation(unittest.TestCase):
    @unittest.expectedFailure
    def test_customer_re_err(self):
        make_loan("<script></script>", "Book")
        make_loan("anything<a />", "Book")

    @unittest.expectedFailure
    def test_customer_len_err(self):
        make_loan("", "Book")
        make_loan("123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890", "Book")

    def test_customer_re_ok(self):
        make_loan("Customer", "Book")
        make_loan("Alph4Num3ric5 and friends'.-,", "Book")

    def test_customer_len_ok(self):
        make_loan("1234567890123456789012345678901234567890123456789012345678901234", "Book")


class TestBookValidation(unittest.TestCase):
    @unittest.expectedFailure
    def test_book_re_err(self):
        make_loan("Customer", "<br>")
        make_loan("Customer", "Robert'); DROP TABLE Books;--")
        make_loan("Customer", "<script></script>")

    @unittest.expectedFailure
    def test_book_len_err(self):
        make_loan("Customer", "")
        make_loan("Customer", "123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890")

    def test_book_re_ok(self):
        make_loan("Customer", "Book")
        make_loan("Customer", "Alph4Num3ric5 and friends'.-,")

    def test_book_len_ok(self):
        make_loan("Customer", "1234567890123456789012345678901234567890123456789012345678901234")

if __name__ == "__main__":
    unittest.main()
