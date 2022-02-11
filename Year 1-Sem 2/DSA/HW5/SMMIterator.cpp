#include "SMMIterator.h"
#include "SortedMultiMap.h"

SMMIterator::SMMIterator(const SortedMultiMap& d) : map(d){
	this->list_inorder=new DA[d.size()];
	this->size=0;
	if(this->map.nr_keys != 0)
	    inorder(d);
    this->current_element=this->list_inorder[0];
    this->pos_in_da=0;
    this->current_pos=0;

}//BC: Theta(1), when we don't have any key
//WC:Theta(nr_elems), when we have at least 1 key
//Total: O(nr_elems)

void SMMIterator::first(){
    this->current_element=this->list_inorder[0];
    this->pos_in_da=0;
    this->current_pos=0;

}//Theta(1)

void SMMIterator::inorder(const SortedMultiMap& d)
{
    int index=0;
    int* stack_of_pos=new int[d.size()];
    int pos_in_stack=0;

    while(index != -1)
    {
        stack_of_pos[pos_in_stack]=index;
        pos_in_stack++;
        index=this->map.bst.left[index];

    }
    while(pos_in_stack!=0)
    {
        pos_in_stack--;
        index=stack_of_pos[pos_in_stack];
        DA current_elem=this->map.bst.info[index];
        this->list_inorder[this->size++]=current_elem;
        index=this->map.bst.right[index];
        while(index != -1)
        {
            stack_of_pos[pos_in_stack]=index;
            pos_in_stack++;
            index=this->map.bst.left[index];
        }
    }

} //Theta(nr_elems)


void SMMIterator::next(){
	if(!this->valid())
	    throw exception();
	if(this->pos_in_da < this->current_element.length - 1)
	    this->pos_in_da++;
	else
    {
	    this->current_pos++;
	    this->current_element=this->list_inorder[this->current_pos];
	    this->pos_in_da=0;
    }
}//Theta(1)

bool SMMIterator::valid() const{
	return this->current_pos!=this->size;

}//Theta(1)

TElem SMMIterator::getCurrent() const{
	if(!this->valid())
	    throw exception();
	TElem result;
    result.first=this->current_element.key;
    result.second=this->current_element.values[this->pos_in_da];
	return result;
}//Theta(1)




