#include "object.h"
#include <iostream>

class String : public Object {

        public:
                int length;
                char* buffer;

                String() {
                        length = 0;
                        buffer = 0;
                }

                String(char* c) {
                        length = strlen(c);
                        buffer = new char[length];
                        for(int i = 0; i < length; i++) {
                                buffer[i] = c[i];
                        }
		}

	bool equals(String* s) {
		
	}
	
	int size() {
		
	}
};
