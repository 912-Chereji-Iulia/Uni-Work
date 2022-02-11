#include "SortedBag.h"
#include "SortedBagIterator.h"
#include <iostream>
#include "ShortTest.h"
#include "ExtendedTest.h"

using namespace std;

int main() {

    test_add_occurence();
	testAll();
	testAllExtended();

	
	cout << "Test over" << endl;
	system("pause");
}
