#include <iostream>
using namespace std;

class Person
{
public:
    int age;
    Person(int age){
        this->age = age;
    }
    void no_this(){
        cout << "using no this" << endl;
    }
    void no_current(){
        cout << "using no current" << endl;
    }
};


int main(){
    Person p = Person(5);
    p.no_this();
    p.no_this();
    p.no_current();
    return 0;
}