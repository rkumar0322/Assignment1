//
// Created by Rahul Kumar on 1/24/20.
//

#include <cstddef>
#include "object.h"

#ifndef ASSIGNMENT1PARTW_ARRAY_H
#define ASSIGNMENT1PARTW_ARRAY_H

#endif //ASSIGNMENT1PARTW_ARRAY_H


class Array: public Object {
public:

    Object* array;
    size_t size;
    size_t MAX_SIZE;

    //Constructor:
    //initializing an empty array with input size
    Array(size_t limit) {
        Object[] l = new Object[limit];
        array = *l;
        size = 0;
        MAX_SIZE = limit;
    }
    
    ~Array() {
        delete[] l;
        delete array;
    }
    

    //assign the element at index with input object
    void assign(Object element, size_t index) {

    }
    
    //returns the element at index 
    Object get(size_t index) {
        
    }
    
    //appends e to the end of the array 
    void push_back(Object o) {
        
    }
    
    //inserts o at index
    void add(Object o, size_t index) {
        
    }
    
    //removes all elements in the array 
    void clear() {
        
    }
    
    //compares o with this array for equality 
    bool equals(Object o) {
        
    }

    //returns the number of elements in the array
    size_t length() {

    }

};
