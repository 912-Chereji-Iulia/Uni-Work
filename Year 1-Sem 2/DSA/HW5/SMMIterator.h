#pragma once

#include "SortedMultiMap.h"


class SMMIterator{
	friend class SortedMultiMap;
private:
	DA* list_inorder;
	int size;
	DA current_element;
	int current_pos;
	int pos_in_da;
	const SortedMultiMap& map;
	SMMIterator(const SortedMultiMap& map);



public:
	void first();
	void next();
	bool valid() const;
   	TElem getCurrent() const;

    void inorder(const SortedMultiMap &d);
};



