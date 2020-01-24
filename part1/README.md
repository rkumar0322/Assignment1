
We use Python for the implementation of A1 and we import python pandas dataframe to build our columnar represenation of the data.

Basically, we scan through the file and separate the fields by "><" to make each row a list of strings. We determine the schema by keeping
track of each row's length when reading each line of the file to find the longest row. After finding the 
