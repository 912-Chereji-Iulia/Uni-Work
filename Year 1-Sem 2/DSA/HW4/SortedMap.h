#pragma once
//DO NOT INCLUDE SORTEDMAPITERATOR

//DO NOT CHANGE THIS PART
typedef int TKey;
typedef int TValue;
#include <utility>
typedef std::pair<TKey, TValue> TElem;
#define NULL_TVALUE -111111
#define NULL_TPAIR pair<TKey, TValue>(-111111, -111111);
#define PRIME 50021
class SMIterator;
typedef bool(*Relation)(TKey, TKey);
typedef int(*TFunction)(int);


struct Node
{
    TElem info;
    Node* next;

};

struct HashTable
{
    int cap; //capacity

    Node** T; // dynamic array of SLLs of Nodes

    double max_load_factor;
};

class SortedMap {
	friend class SMIterator;
    private:
		HashTable* elems;
		Relation rel;
		int length;
        int hash_function(TKey k) const; //hash function

    public:

    // implicit constructor
    SortedMap(Relation r);

    SortedMap(const SortedMap& m);

	// adds a pair (key,value) to the map
	//if the key already exists in the map, then the value associated to the key is replaced by the new value and the old value is returned
	//if the key SMes not exist, a new pair is added and the value null is returned
	TValue add(TKey c, TValue v);

	//searches for the key and returns the value associated with the key if the map contains the key or null: NULL_TVALUE otherwise
	TValue search(TKey c) const;


	//removes a key from the map and returns the value associated with the key if the key existed ot null: NULL_TVALUE otherwise
	TValue remove(TKey c);

	//returns the number of pairs (key,value) from the map
	int size() const;

	//checks whether the map is empty or not
	bool isEmpty() const;

    // return the iterator for the map
    // the iterator will return the keys following the order given by the relation
    SMIterator iterator() const;

    // destructor
    ~SortedMap();

    void resize();

    int getKeyRange() const;
};
