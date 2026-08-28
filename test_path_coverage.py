import unittest
from loop import process_even_numbers


class TestPathCoverage(unittest.TestCase):
    """
    Các ca kiểm thử nhằm đạt 100% Path Coverage (Bao phủ tất cả các đường đi trong chương trình).
    Giải quyết Issue #3.
    """

    def test_path_1_none_input(self):
        """Đường đi 1: Input là None -> nhánh if numbers is None thực thi -> return []"""
        self.assertEqual(process_even_numbers(None), [])

    def test_path_2_empty_list(self):
        """Đường đi 2: Input là mảng rỗng [] -> vòng lặp for không chạy lần nào -> return []"""
        self.assertEqual(process_even_numbers([]), [])

    def test_path_3_only_odd_numbers(self):
        """Đường đi 3: Mảng chỉ có số lẻ -> vòng lặp for chạy, nhưng điều kiện (num % 2 == 0) luôn False -> return []"""
        self.assertEqual(process_even_numbers([1, 3, 5]), [])

    def test_path_4_only_even_numbers(self):
        """Đường đi 4: Mảng chỉ có số chẵn -> vòng lặp for chạy, điều kiện (num % 2 == 0) luôn True -> return mảng chẵn"""
        self.assertEqual(process_even_numbers([2, 4, 6]), [2, 4, 6])

    def test_path_5_mixed_numbers(self):
        """Đường đi 5: Mảng xen kẽ số chẵn và số lẻ -> kiểm thử kết hợp cả 2 nhánh True và False trong nhiều vòng lặp"""
        self.assertEqual(process_even_numbers([1, 2, 3, 4, 5, 6]), [2, 4, 6])


if __name__ == '__main__':
    unittest.main()
