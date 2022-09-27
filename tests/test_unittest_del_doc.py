import unittest
from parameterized import parameterized
from main import delete_doc


class UnitTestMainDeleteDoc(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @parameterized.expand([
        ("123 ABC", ("123 ABC", False)),
        ("2207 876234", ("2207 876234", True)),
        ("11-2", ("11-2", True)),
        ("10006", ("10006", True))
    ])
    def test_delete_doc(self, input_data, result):
        self.assertEqual(delete_doc(input_data), result)
