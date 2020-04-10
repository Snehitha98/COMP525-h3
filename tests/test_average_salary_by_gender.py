"""
test_average_salary_by_gender.py
Snehitha Mamidi
April 9, 2020
"""

import unittest
from problems.data_analysis import DevStats


class TestCountDevelopersByCountry(unittest.TestCase):
    """
    Tests for average_salary_by_gender() method
    """
    def setUp(self):
        """
        Define attribute dev_stats to hold object of type Problems
        """
        self.dev_stats = DevStats()

    def test_one_entry(self):
        """
        Test case for one entry
        """
        actual_result = self.dev_stats.average_salary_by_gender(
            'avgsalary1.csv'
        )
        expected_result = {'Female': 73433.0}
        self.assertDictEqual(actual_result, expected_result)

    def test_three_entries(self):
        """
        Test case for three entries
        """
        actual_result = self.dev_stats.average_salary_by_gender(
            'avgsalary2.csv'
        )
        expected_result = {'Male': 124333.33333333333}
        self.assertDictEqual(actual_result, expected_result)

    def test_multiple_entries(self):
        """
        Test case for three entries
        """
        actual_result = self.dev_stats.average_salary_by_gender('stats.csv')
        expected_result = {
            'Male': 98162.43537047053, 'Female': 142321.104,
            'Female;Non-binary, genderqueer, or gender non-conforming':
            104164.0,
            'Non-binary, genderqueer, or gender non-conforming':
            60349.36363636364,
            'Male;Non-binary, genderqueer, or gender non-conforming': 50005.0,
            'Female;Transgender': 61402.4, 'Male;Transgender':
            62660.333333333336,
            'Female;Transgender;Non-binary, genderqueer, or gender non-conforming':
            31788.0,
            'Female;Male': 3756.0, 'Transgender': 40000.0,
            'Female;Male;Transgender;Non-binary, genderqueer, or gender non-conforming':
            9600.0
        }
        self.assertDictEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
