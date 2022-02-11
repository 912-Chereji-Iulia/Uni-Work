package Model.value;

import Model.type.IType;
import Model.type.IntType;

public class IntValue implements IValue {
    int val;
    public IntValue(){
        this.val=0;
    }

    public IntValue(int i){
        this.val=i;
    }

    public int getVal(){
        return this.val;
    }

    @Override
    public IType get_type() {
        return new IntType();
    }

    @Override
    public IValue deep_copy() {
        return new IntValue(this.val);
    }

    @Override
    public boolean equals(Object o){
        if (o == null || o.getClass() != this.getClass())
            return false;
        IntValue new_val = (IntValue) o;
        return new_val.val == this.val;
    }

    @Override
    public String toString(){

        return Integer.toString(this.val);
    }

}
