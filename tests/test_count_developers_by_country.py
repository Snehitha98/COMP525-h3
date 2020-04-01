"""
(replace with module docstring; see data_analysis.py instructions)
"""

import unittest
from problems.data_analysis import DevStats


class TestCountDevelopersByCountry(unittest.TestCase):
    """
    (add your docstring; see lab5 example)
    """
    def setUp(self):
        """
        (add your docstring; see lab5 example)
        (not sure whether we need this method)
        """

    def test_one_country(self):
        """
        (add your docstring)
        """
        # Remove these two statements below. Were added to remove pylint errors.
        DevStats.count_developers_by_country('fake.csv')
        self.assertDictEqual({}, {})

        # define and initialize test_case
        # define and initialize actual_result by calling method with test_case
        # argument
        # define and initalize expected_result wiht data obtained through
        # other means than calling the method
        # call self.assertDictEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
