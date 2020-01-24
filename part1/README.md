
We use Python for the implementation of A1 and we import python pandas dataframe to build our columnar represenation of the data.

Basically, we scan through the file and separate the fields by "><" to parse each row as a list of strings. We determine the schema by keeping track of each row's length when reading each line of the file to find the longest row. After finding the schema, we build the columnar represenatation by using pd.Dataframe().transpose.

We define the type of each column as the field type in largest schema row. To find the type of each field, we have a infer_type() function which tranfer every field to representation in its corresponding type. When building the columnar representation by using dataframe, 
we check if the field matches the type of column first. If it matches the type, we appened its value; if not, we replace its value by "NONE", so it will be shown as missing in the table. As a result, "<>", blank and any field which doesn't match the column's type will be shown as "NONE" in the table, which are the missing values.

With the pandas dataframe, we can easily allocate each field by giving its column and row numbers. 


