#include <iostream>
#include "object.h"
#include "array.h"

void test1() {
    
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
    t_true(
    
}





int main() {
    std::cout << "Hello, World!" << std::endl;
    
    return 0;
}
