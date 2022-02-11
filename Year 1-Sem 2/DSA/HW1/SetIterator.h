#pragma once
#include "Set.h"
#include <exception>

class SetIterator
{
	//DO NOT CHANGE THIS PART
	friend class Set;
private:
	//DO NOT CHANGE THIS PART
	const Set& set;
	SetIterator(const Set& s);
    int current; //position of the current element from the elements array

public:
	void first();
	void next();
	TElem getCurrent();
	bool valid() const;
};


