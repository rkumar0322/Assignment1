#include <iostream>
#include "object.h"
#include "array.h"
#include "string.h" 


void test1() {
    String s1 = new String("Hello");
    String s2 = new String("World");
    String s3 = new String("Hello");
    t_true(s1->equals(s3));
    t_false(s1->equals(s2));
    OK("1");
    
}


void test2() {
    
    String s1 = new String("Hello");
    String s2 = new String("World");
    String s3 = new String("Earth");
    Array a = new Array();
    a->add(s1);
    a->add(s2);
    t_true(a->get(0)->equals(s1));
    t_true(a->get(1)->equals(s2));
    t_true(a->length() == 2); 
    a->assign(s3, 0);
    t_true(a->get(0)->equals(s3));
    a->clear();
    t_true(a->length() == 0);
    OK("2");
    
}

int main() {
    
    test1();
    test2();
    
    return 0;
}
