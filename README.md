### count_developers_by_country()
```
def count_developers_by_country(cls, filename):
      """
      Create a dictionary keyed by country names and values are the
      number of developers in each country
      filename: string that has the name of the CSV text file
      Returns: dictionary
         keys are country names
         values are the number of developers in each country
      """
```
* **file_ref** holds a reference to the file object returned by open
* Use the accumulation pattern
* **accumulator**
    * of type dictionary
    * initialized with {}
    * named `count_developers_by_country`
    * keys are the country names
    * values are the number of developers in each country
* use a for loop with loop variable named `line` to iterate over `file_ref.readlines()` from second line
    * split the line by `|` and store it in variable named `lst`
    * Assign first index of `lst` to `country_name`
    * at each iteration check if `country_name` is in `count_developers_by_country`
       * if it is, increment value by `1` corresponding to key `country_name` using the increment pattern
    * else
       * store the value `1` in `count_developers_by_country` keyed by `country_name`
* close the opened file `file_ref`
* Returns `count_developers_by_country` after iteration is over
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### average_salary_by_gender()
```
def average_salary_by_gender(cls, filename):
      """
      Create a dictionary keyed by gender and values are the
      average salary of each gender type.
      filename: string that has the name of the CSV text file
      Returns: dictionary
         keys are gender
         values are average salary of each gender
      """
```
* **file_ref** holds a reference to the file object returned by open
* Use the accumulation pattern
* **accumulator**
    * of type dictionary
    * initialized with {}
    * named `lst_salary_by_gender`
    * keys are the gender
    * values are the list of salaries of each gender
* use a for loop with loop variable named `line` to iterate over `file_ref.readlines()` from second line
    * split the line by `|` and store it in variable named `lst`
    * Assign sixth index of `lst` to `gender_name`
    * Assign fourth index of `lst` to `converted_salary`
    * at each iteration check if `gender_name` is in `lst_salary_by_gender`
        * if it is, add `converted_salary` of type list, to `lst_salary_by_gender` keyed by `gender_name` and assign it to `lst_salary_by_gender[gender_name]`
    * else
        * store the value `converted_salary` of type list in `lst_salary_by_gender` keyed by `gender_name`
 * Use the accumulation pattern
* **accumulator**
    * of type dictionary
    * initialized with {}
    * named `average_salary_by_gender`
    * keys are the gender
    * values are the a average salary of each gender
* use a for loop with loop variable named `key` to iterate over `lst_salary_by_gender`
    * convert the list of salaries of type string to float and then store it in **str_to_int**
    * calculate the mean of `str_to_int` and store it in `avg_salary`
    * store the value `avg_salary` in `average_salary_by_gender` keyed by `key`
* close the opened file `file_ref`
* Returns `average_salary_by_gender` after iteration is over
