#include "Set.h"
#include "SetIterator.h"
#include "ExtendedTest.h"
#include "ShortTest.h"
#include <stack>
#include <iostream>
#include <assert.h>
using namespace std;


void test_new_functionality()
{
    Set s1,s2;

    assert(s1.isEmpty() == true);
    assert(s1.size() == 0);
    assert(s1.add(5)==true);
    assert(s1.add(1)==true);
    assert(s1.add(3)==true);

    assert(s2.add(2)==true);
    assert(s2.add(8)==true);

    s1.Union(s2);

    assert(s1.search(2)==true);
    assert(s1.search(8)==true);

    assert(s1.size()==5);
    cout<<"Tested Union"<<endl;

}

int main() {

	testAll();
	testAllExtended();
	test_new_functionality();


	cout << "That's all!" << endl;
	system("pause");

}



