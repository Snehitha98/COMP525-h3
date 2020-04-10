"""
data_analysis.py
Practice datasets,dictionaries,text files
Snehitha Mamidi
created date : April 3,2020
updated date : April 10,2020
"""

class DevStats():
    """
    Data processing functionality
    """
    @classmethod
    def count_developers_by_country(cls, filename):
        """
        Create a dictionary keyed by country names and values are the
        number of developers in each country
        filename: string that has the name of the CSV text file
        Returns: dictionary
           keys are country names
           values are the number of developers in each country
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
    main function
    """
    filename = 'countdevel1.csv'
    actual_result = DevStats.count_developers_by_country(filename)
    print(f'developers by country in {filename} are: {actual_result}')

    filename = 'countdevel2.csv'
    actual_result = DevStats.count_developers_by_country(filename)
    print(f'developers by country in {filename} are: {actual_result}')

    filename = 'stats.csv'
    actual_result = DevStats.count_developers_by_country(filename)
    print(f'developers by country in {filename} are: {actual_result}')


if __name__ == '__main__':
    main()
