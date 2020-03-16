"""
Finder will return all strings from the list that contain the exact same\
characters as the string passed into it.

Assumptions:
    * Return string from list of strings that contains characters from input
        string in any order.
    * Return string if input string char exist multiple time in list of string.
    eg: find = 'aabc'
        string_list = ['aabbc', 'abc']
        output = ['aabbc', 'abc']

Testing:
    * Using pytest for testing
    $ pytest --benchmark-disable -s -v test_finder.py

Performance benchmarking
    * Using pytest for testing
    $ pytest -s -v test_finder.py -k TestFinderBenchmark

"""


class Finder:
    """Finder class."""

    def __init__(self, string_list):
        """Initialize with list of strings."""
        self.string_list = string_list

    def find(self, input_string):
        """Search for list con."""
        input_set = set(input_string)
        contains_string = []

        for string in self.string_list:
            if input_string in string:
                contains_string.append(string)

            elif not input_set - set(string):
                contains_string.append(string)

        return contains_string
