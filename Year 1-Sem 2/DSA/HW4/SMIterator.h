#pragma once
#include "SortedMap.h"

//DO NOT CHANGE THIS PART
class SMIterator{
	friend class SortedMap;
private:
	const SortedMap& map;
	SMIterator(const SortedMap& mapionar);

	SortedMap copy{map};
	int first_position,current_position;

public:

	void first();
	void next();
	bool valid() const;
    TElem getCurrent() const;

};

