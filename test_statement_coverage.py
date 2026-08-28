import unittest
from loop import process_even_numbers


class TestStatementCoverage(unittest.TestCase):
    """
    Các ca kiểm thử nhằm đạt 100% Statement Coverage (Bao phủ tất cả các lệnh/dòng code).
    Giải quyết Issue #2.
    """

    def test_statement_coverage_none(self):
        # Đảm bảo dòng 'if numbers is None: return []' được thực thi
        result = process_even_numbers(None)
        self.assertEqual(result, [])

    def test_statement_coverage_with_even_number(self):
        # Đảm bảo các dòng tạo list, vòng lặp for, điều kiện if num % 2 == 0 (true),
        # dòng append và dòng return được thực thi
        result = process_even_numbers([2])
        self.assertEqual(result, [2])


if __name__ == '__main__':
    unittest.main()
