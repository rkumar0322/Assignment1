
We use classes Object and Array. 

Both Array and String are instances of Objects, so we make them as child class of class Object.

In class Object, we have a method called equals() to compare two objects and see if they are in equality. We will implement
this methods in child classes later. 

An Array is an array of Objects. It has two fields: a pointer to the start of the array and a size_t which records the number
of elements. We have methods which are quite similar to those methods on StrList in previous assignments, to easily allocate 
and make change to each element in the array. 
