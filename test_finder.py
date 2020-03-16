import unittest

import pytest


from finder import Finder


class TestFinder(unittest.TestCase):
    def test_string_exists_in_string_list(self):
        finder = Finder(string_list=["asd", "asdd", "fre", "glk", "lkm"])
        self.assertEqual(["asd", "asdd"], finder.find("asd"))

    def test_string_not_exists_in_string_list(self):
        finder = Finder(string_list=["asd", "asdd", "fre", "glk", "lkm"])
        self.assertEqual([], finder.find("apple"))

    def test_string_list_is_empty(self):
        finder = Finder(string_list=[])
        self.assertEqual([], finder.find("asd"))

    def test_input_string_duplicate_char(self):
        finder = Finder(string_list=["pineapple", "apple", "aple", "app"])
        self.assertEqual(["pineapple", "apple", "aple"], finder.find("apple"))


class TestFinderBenchmark(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def setUpBenchamrk(self, benchmark):
        self.benchmark = benchmark

    def test_benchmark_string_exist_for_50K(self):
        finder = Finder(string_list=["pineapple", "apple", "testasas"] * 50000)
        result = self.benchmark(finder.find, "app")
        self.assertEqual(["pineapple", "apple"] * 50000, result)

    def test_benchmark_string_exist_for_1(self):
        finder = Finder(string_list=["app"])
        result = self.benchmark(finder.find, "app")
        self.assertEqual(["app"], result)
