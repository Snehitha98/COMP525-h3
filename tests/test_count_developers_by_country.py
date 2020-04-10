"""
test_count_developers_by_country.py
Snehitha Mamidi
April 9, 2020
"""

import unittest
from problems.data_analysis import DevStats


class TestCountDevelopersByCountry(unittest.TestCase):
    """
    Tests for count_developers_by_country() method
    """
    def setUp(self):
        """
        Define attribute dev_stats to hold object of type Problems
        """
        self.dev_stats = DevStats()

    def test_one_country(self):
        """
        Test case for one entry
        """
        actual_result = self.dev_stats.count_developers_by_country(
            'countdevel1.csv'
        )
        expected_result = {'United Kingdom': 1}
        self.assertDictEqual(actual_result, expected_result)

    def test_three_countries(self):
        """
        Test case for three entries
        """
        actual_result = self.dev_stats.count_developers_by_country(
            'countdevel2.csv'
        )
        expected_result = {'United Kingdom': 1, 'Argentina': 1, 'Germany': 1}
        self.assertDictEqual(actual_result, expected_result)

    def test_multiple_countries(self):
        """
        Test case for three entries
        """
        actual_result = self.dev_stats.count_developers_by_country('stats.csv')
        expected_result = {
            'United Kingdom': 169, 'Argentina': 9, 'Germany': 133,
            'United States': 612, 'Japan': 11, 'Brazil': 46,
            'Netherlands': 42, 'Turkey': 13, 'Belgium': 16, 'Estonia': 3,
            'Canada': 78, 'Ukraine': 22, 'Australia': 59, 'Switzerland': 19,
            'France': 64, 'Mexico': 13, 'Philippines': 8, 'Norway': 17,
            'Qatar': 2, 'Spain': 33, 'Sri Lanka': 6, 'Sweden': 37,
            'Russian Federation': 48,
            'The former Yugoslav Republic of Macedonia': 1,
            'Italy': 22, 'India': 128, 'Israel': 10, 'New Zealand': 9,
            'Bangladesh': 12, 'Lithuania': 5, 'Serbia': 7, 'Austria': 19,
            'Denmark': 11, 'Poland': 50, 'Pakistan': 12, 'Finland': 12,
            'China': 11, 'Iran, Islamic Republic of...': 15,
            'Georgia': 1, 'Romania': 16, 'South Africa': 9, 'Portugal': 11,
            'Belarus': 10, 'Bulgaria': 7, 'Czech Republic': 15, 'Ireland': 13,
            'Hong Kong (S.A.R.)': 4, 'Singapore': 6, 'Indonesia': 4,
            'Chile': 1, 'Taiwan': 2, 'Colombia': 10, 'Thailand': 3,
            'Egypt': 3, 'Azerbaijan': 2, 'Bosnia and Herzegovina': 5,
            'Latvia': 2, 'Slovakia': 3, 'Hungary': 8, 'Greece': 7,
            'Dominican Republic': 4, 'Malaysia': 5, 'Croatia': 5,
            'Iceland': 2, 'Jordan': 2,
            'Venezuela, Bolivarian Republic of...': 2, 'Armenia': 1,
            'Nigeria': 5, 'Uruguay': 2, 'Malta': 3, 'Cuba': 1,
            'Maldives': 1, 'Lebanon': 3, 'Slovenia': 1,
            'United Republic of Tanzania': 1, 'Myanmar': 1,
            'Libyan Arab Jamahiriya': 2, 'Ecuador': 3, 'Peru': 1,
            'Ethiopia': 2, 'South Korea': 3, 'Viet Nam': 3,
            'Other Country (Not Listed Above)': 3, 'Algeria': 2, 'Albania': 1,
            'Liechtenstein': 1, 'Paraguay': 1, 'El Salvador': 1,
            'Costa Rica': 1, 'Nepal': 3, 'Ghana': 1, 'Saudi Arabia': 2,
            'Gambia': 1, 'Morocco': 1, 'Kenya': 2, 'Cyprus': 1
        }

        self.assertDictEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
