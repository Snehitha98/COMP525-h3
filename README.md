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
