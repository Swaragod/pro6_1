import unittest
from parameterized import parameterized
from main import check_document_existance, get_doc_owner_name, add_new_shelf


class UnitTestMain(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @parameterized.expand([
        ("123 ABC", False),
        ("2207 876234", True),
        ("11-2", True),
        ("10006", True)
    ])
    def test_check_document_existance(self, input_data, result):
        self.assertEqual(check_document_existance(input_data), result)

    @parameterized.expand([
        ["123 ABC", None],
        ["2207 876234", "Василий Гупкин"],
        ["11-2", "Геннадий Покемонов"],
        ["10006", "Аристарх Павлов"]
    ])
    def test_get_doc_owner_name(self, input_data, result):
        self.assertEqual(get_doc_owner_name(input_data), result)

    @parameterized.expand([
        ['125', ('125', True)],
        ['A1', ('A1', True)],
        ['2', ('2', False)]
    ])
    def test_add_new_shelf(self, input_data, result):
        self.assertEqual(add_new_shelf(input_data), result)
