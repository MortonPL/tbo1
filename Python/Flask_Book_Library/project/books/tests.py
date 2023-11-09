import unittest
from project.books.models import Book


def make_book(name, author):
    Book(name, author, "1999", "")

class TestNameValidation(unittest.TestCase):
    @unittest.expectedFailure
    def test_name_re_err(self):
        make_book("<script></script>", "Author")
        make_book("anything<a />", "Author")

    @unittest.expectedFailure
    def test_name_len_err(self):
        make_book("", "Author")
        make_book("123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890", "Author")

    def test_name_re_ok(self):
        make_book("Name", "Author")
        make_book("(Almost) Any Book Name Is Allowed 1246796 🔥🔥🔥🔥", "Author")

    def test_name_len_ok(self):
        make_book("1234567890123456789012345678901234567890123456789012345678901234", "Author")


class TestAuthorValidation(unittest.TestCase):
    @unittest.expectedFailure
    def test_author_re_err(self):
        make_book("Name", "<br>")
        make_book("Name", "Robert'); DROP TABLE Books;--")
        make_book("Name", "<script></script>")

    @unittest.expectedFailure
    def test_author_len_err(self):
        make_book("Name", "")
        make_book("Name", "123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890")

    def test_author_re_ok(self):
        make_book("Name", "Author")
        make_book("Name", "Alph4Num3ric5 and friends'.-,")

    def test_author_len_ok(self):
        make_book("Name", "1234567890123456789012345678901234567890123456789012345678901234")

if __name__ == "__main__":
    unittest.main()
