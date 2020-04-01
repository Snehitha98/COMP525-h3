"""
data_analysis.py
(replace this with short statement about the purpose of the module)
(replace this with your name)
(replace this with two lines: created date and updated date)
"""


class DevStats():
    """
    (replace this with short statement about the purpose of the class)
    """
    @classmethod
    def count_developers_by_country(cls, filename):
        """
        (replace with complete docstring.
        It is an adaptation of  Activity 2 in StackOverflow Developers Survey)
        filename: string that has the name of the CSV text file
        Returns: dictionary in which keys are the country names and values are
            the number of devevelopeoprs in each counntry
        """

    @classmethod
    def average_salary_by_gender(cls, filename):
        """
        (replace with complete docstring.
        It is an adaptation of  Activity 5 in StackOverflow Developers Survey
        (add description of paramter)
        (add description of returns)
        """


def main():
    """
    (replace with short statement about the purpose of this function)
    """

    # simplest test case for count_develooperers_by_country is countdevel1.csv
    # that has only one country in the small dataset
    filename = 'countdevel1.csv'
    actual_result = DevStats.count_developers_by_country(filename)
    print(f'developers by country in {filename} are: {actual_result}')


if __name__ == '__main__':
    main()
