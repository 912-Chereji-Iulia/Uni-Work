#include "SMMIterator.h"
#include "SortedMultiMap.h"
#include <iostream>
#include <vector>
#include <exception>

using namespace std;

SortedMultiMap::SortedMultiMap(Relation r) {
	this->rel=r;
	this->nr_keys=0;
	this->bst.first_empty=0;
	this->bst.capacity=10;
	this->nr_elems=0;
	this->bst.info=new DA[this->bst.capacity];
	this->bst.left=new int [this->bst.capacity];
	this->bst.right=new int [this->bst.capacity];
	for(int i=0;i<this->bst.capacity-1;i++)
	    this->bst.left[i]=i+1;
	this->bst.left[this->bst.capacity-1]=-1;
	this->bst.root=-1;

}//Theta(1)

int SortedMultiMap::init_pos(TKey k, TValue v){
    //function that creates a new node given the information to be stored in it and returns its pos
    int new_pos=this->bst.first_empty;
    this->bst.info[this->bst.first_empty].key=k;
    this->bst.info[this->bst.first_empty].values=new TValue [10];
    this->bst.info[this->bst.first_empty].values[0]=v;
    this->bst.info[this->bst.first_empty].cap=10;
    this->bst.info[this->bst.first_empty].length=1;
    this->bst.first_empty=this->bst.left[new_pos];
    this->bst.left[new_pos]=-1;
    this->bst.right[new_pos]=-1;

    return new_pos;

}//Theta(1)

int SortedMultiMap::insert_recursive(int start, TKey k, TValue v) {

    if(start==-1 || this->nr_keys == 0)
        start=init_pos(k,v);
    else
    {
        if(! this->rel(this->bst.info[start].key,k))
            this->bst.left[start]=this->insert_recursive(this->bst.left[start],k,v);
        else
            this->bst.right[start]=this->insert_recursive(this->bst.right[start],k,v);
    }

    this->bst.root=start;
    return start;

}//BC: Theta(1) - when we have no keys yet in the smm or the starting position is -1
// WC: Theta(nr_elems) - when we have to search for the starting position,going through the left/right subtree
//Total complexity-O(nr_elems)



void SortedMultiMap::resize()
{
    int new_cap = 2 * this->bst.capacity;
    DA* new_info = new DA[new_cap];
    int* new_left = new int[new_cap];
    int* new_right = new int[new_cap];

    for (int i = 0; i < new_cap - 1; i++)
    {
        if (i < this->bst.capacity)
        {
            new_info[i] = this->bst.info[i];
            new_left[i] = this->bst.left[i];
            new_right[i] = this->bst.right[i];
        }
        else
        {
            new_left[i] = i + 1;
            new_right[i] = -1;
            new_info[i].cap = 0;
            new_info[i].values = NULL;
            new_info[i].length = 0;
        }
    }
    new_left[new_cap - 1] = -1;
    new_right[new_cap - 1] = -1;

    new_info[new_cap - 1].cap = 0;
    new_info[new_cap - 1].values = NULL;
    new_info[new_cap - 1].length = 0;
    delete[] this->bst.info;
    delete[] this->bst.left;
    delete[] this->bst.right;

    this->bst.first_empty = this->bst.capacity;
    this->bst.capacity = new_cap;
    this->bst.info = new_info;
    this->bst.left = new_left;
    this->bst.right = new_right;
}//Theta(capacity)

void SortedMultiMap::add(TKey c, TValue v) {
	if(!this->search(c).empty()) //if the key has values associated
    {
	    int current_pos=this->bst.root;
	    while(current_pos!=-1)
        {
	        if(this->bst.info[current_pos].key==c)
            {
	            if(this->bst.info[current_pos].length==this->bst.info[current_pos].cap)
                {
	                //resize array for elem
                    int new_cap=this->bst.info[current_pos].cap*2;
                    TValue* new_values=new TValue[new_cap];
                    for(int i=0;i<this->bst.info[current_pos].length;++i)
                        new_values[i]=this->bst.info[current_pos].values[i];
                    delete[] this->bst.info[current_pos].values;
                    this->bst.info[current_pos].values=new_values;
                    this->bst.info[current_pos].cap=new_cap;


                }
                this->bst.info[current_pos].values[this->bst.info[current_pos].length++]=v; //add the new value
                this->nr_elems++;
                return;

            }
	        else if(this->rel(this->bst.info[current_pos].key,c))
                current_pos=this->bst.right[current_pos];
            else
                current_pos=this->bst.left[current_pos];

        }
	    this->nr_elems++;

    }
	else  //if the key doesn't have some values associated
    {
	    if(this->nr_keys == this->bst.capacity)
        {
            this->resize();
        }
	    this->insert_recursive(0,c,v);

	    this->nr_keys++;
	    this->nr_elems++;
    }
}//BC: Theta(1) - when we have the root with a single descendant
// WC: Theta(height + capacity)- when we have a degenerate tree and we have to go at the last node and we have to resize
// Total complexity: O(height of the tree+ capacity)

vector<TValue> SortedMultiMap::search(TKey c) const {
    vector<TValue> result;
    if (this->nr_keys == 0)
        return vector<TValue>();
    int current_pos = this->bst.root;

    bool ok = false;
    while (current_pos != -1 && !ok) {
        if (this->bst.info[current_pos].key == c)
            ok = true;
        else {
            if (!this->rel(this->bst.info[current_pos].key, c))
                current_pos = this->bst.left[current_pos];
            else
                current_pos = this->bst.right[current_pos];
        }
    }
    if (!ok)
        return vector<TValue>();

    for (int i = 0; i < this->bst.info[current_pos].length; i++)
        result.push_back(this->bst.info[current_pos].values[i]);

    return result;

}// BC : Theta(1), when we don't have any keys
// WC: Theta(height of the tree+ nr of values of the key), when the searched elem is on the last position
//Total complexity: O(height of the tree + nr of values of the key)

bool SortedMultiMap::remove(TKey c, TValue v) {
	vector<TValue> values_of_c=this->search(c);
	if(values_of_c.empty()) //if the key has no associated values
	    return false;

    bool ok= false; // if the value v is not in the list_inorder of values ok the key c
    for(int i : values_of_c)
        if(i==v)
            ok=true;
    if(!ok)
        return false;

    int current_pos=0;
	int parent=this->find_parent_pos(c,current_pos);

	if (values_of_c.size()==1) //if the key has only one value associated
    {
        if (this->bst.right[current_pos] == -1 && this->bst.left[current_pos] == -1)
            //The node to be removed has no descendant
            //Set the corresponding child of the parent to NIL
        {
            if (this->bst.right[parent] == current_pos)
                this->bst.right[parent] = -1;
            else
                this->bst.left[parent] = -1;
            this->bst.left[current_pos] = this->bst.first_empty;
            this->bst.first_empty = current_pos;
        }
        else if (this->bst.right[current_pos] != -1 && this->bst.left[current_pos] == -1)
            //The node to be removed has one descendant
            //Set the corresponding child of the parent to the descendant
        {
            if (current_pos == 0)
            {
                int right_pos = this->bst.right[current_pos];
                this->bst.info[current_pos] = this->bst.info[right_pos];
                this->bst.left[current_pos] = this->bst.left[right_pos];
                this->bst.right[current_pos] = this->bst.right[right_pos];
                this->bst.left[right_pos] = this->bst.first_empty;
                this->bst.first_empty= right_pos;
            }
            else
            {
                if (this->bst.right[parent] == current_pos)
                    this->bst.right[parent] = this->bst.right[current_pos];
                else
                    this->bst.left[parent] = this->bst.right[current_pos];
                this->bst.left[current_pos] = this->bst.first_empty;
                this->bst.first_empty = current_pos;
            }
        }
        else if (this->bst.right[current_pos] == -1 && this->bst.left[current_pos] != -1)
            //The node to be removed has one descendant
            //Set the corresponding child of the parent to the descendant
        {
            if (current_pos== 0)
            {
                int left_pos = this->bst.left[current_pos];
                this->bst.info[current_pos] = this->bst.info[left_pos];
                this->bst.left[current_pos] = this->bst.left[left_pos];
                this->bst.right[current_pos] = this->bst.right[left_pos];
                this->bst.left[left_pos] = this->bst.first_empty;
                this->bst.first_empty = left_pos;
            }
            else
            {
                if (this->bst.right[parent] == current_pos)
                    this->bst.right[parent] = this->bst.left[current_pos];
                else
                    this->bst.left[parent] = this->bst.left[current_pos];
                this->bst.left[current_pos] = this->bst.first_empty;
                this->bst.first_empty = current_pos;
            }
        }
        else
            //The node to be removed has two descendants
            //Find the maximum of the left subtree, move it to the node tobe deleted, and delete the maximumOR
        {
            int max_pos=this->maximum(this->bst.left[current_pos]);
            DA arr=this->bst.info[max_pos];
            for (int i = 0; i < this->nr_keys; i++)
                this->remove(arr.key, arr.values[0]);
            this->bst.info[current_pos] =arr;
        }
        this->nr_keys--;

    }
	else //multiple values
    {
        //remove value from the list_inorder of values
        for(int i=0;i<this->bst.info[current_pos].length;++i)
        {
            if(this->bst.info[current_pos].values[i]==v)
                this->bst.info[current_pos].values[i]=this->bst.info[current_pos].values[i+1];
        }
        this->bst.info[current_pos].length--;

    }
    this->nr_elems--;
    return true;

}//BC: Theta(1) - when the key has no values or the value v is not in the list_inorder of values of c
// WC: Theta(height+nr_elems)- when we have a degenerate tree and we have to go at the last node
// Total complexity: O(height of the tree+nr_elems)

int SortedMultiMap::find_parent_pos(TKey c, int &current_pos){
    int parent=0;
    while(current_pos !=-1)
    {
        if(this->bst.info[current_pos].key==c)
            break;
        else if(this->rel(this->bst.info[current_pos].key,c))
        {
            parent=current_pos;
            current_pos=this->bst.right[current_pos];

        }
        else
        {
            parent=current_pos;
            current_pos=this->bst.left[current_pos];
        }
    }
    return parent;

}//BC: Theta(1), when the root has only 1 descendant
//WC: Theta(height), when we have to go through the last node
//Total complexity:O(height)

int SortedMultiMap::maximum(int pos) {
    if(pos==-1)
        return -1;
    while (this->bst.right[pos] != -1)
        pos = this->bst.right[pos];
    return pos;

}//BC: Theta(1), when the root has only 1 descendant
//WC: Theta(height), when we have to go through the last node
//Total complexity: O(height)

int SortedMultiMap::minimum(int pos) {
    if(pos==-1)
        return -1;

    while (this->bst.left[pos] != -1)
        pos = this->bst.left[pos];
    return pos;

}//BC: Theta(1), when the root has only 1 descendant
//WC: Theta(height), when we have to go through the last node
//Total complexity: O(height)


int SortedMultiMap::size() const {
	return this->nr_elems;
}
//Theta(1)

bool SortedMultiMap::isEmpty() const {
	return this->nr_elems == 0;

}
//Theta(1)

////returns the difference between the maximum and the minimum key
int SortedMultiMap::getKeyRange() {

    if(this->isEmpty())
        return -1;
    int pos_max=this->maximum(this->bst.root);
    int pos_min=this->minimum(this->bst.root);
    int key_min=this->bst.info[pos_min].key;
    int key_max=this->bst.info[pos_max].key;
    return abs(key_max-key_min);

}//BC: Theta(1), when the root has only 1 descendant
//WC: Theta(height), when we have to go through the last node
//Total complexity: O(height)

SMMIterator SortedMultiMap::iterator() const {
	return SMMIterator(*this);
}//Theta(1)


SortedMultiMap::~SortedMultiMap() {
    for(int i=0;i<this->bst.capacity;i++)
    {
        if(this->bst.info[i].length!=0)
            delete[] this->bst.info[i].values;
    }
	delete[] this->bst.info;
	delete[] this->bst.left;
	delete[] this->bst.right;

}//Theta(capacity)





