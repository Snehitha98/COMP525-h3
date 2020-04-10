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
        file_ref = open(filename, 'r')
        count_developers_by_country = {}
        for line in file_ref.readlines()[1:]:
            lst = line.split('|')
            country_name = lst[1]
            if country_name in count_developers_by_country:
                count_developers_by_country[country_name] += 1
            else:
                count_developers_by_country[country_name] = 1
        file_ref.close()
        return count_developers_by_country

    @classmethod
    def average_salary_by_gender(cls, filename):
        """
        Create a dictionary keyed by gender and values are the
        average salary of each gender type.
        filename: string that has the name of the CSV text file
        Returns: dictionary
           keys are gender
           values are average salary of each gender
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
