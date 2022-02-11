package Model.value;

import Model.type.BoolType;
import Model.type.IType;

public class BoolValue implements IValue{
    boolean val;

    public BoolValue(){
        this.val=false;
    }

    public BoolValue(boolean i){
        this.val=i;
    }

    public boolean getVal(){
        return this.val;
    }

    @Override
    public IType get_type() {
        return new BoolType();
    }

    @Override
    public IValue deep_copy() {
        return new BoolValue(this.val);
    }

    @Override
    public boolean equals(Object o){
        if(o == null || o.getClass() != this.getClass())
            return false;
        BoolValue o_val = (BoolValue) o;
        return o_val.val == this.val;
    }
    @Override
    public String toString(){
        if(this.val)
            return "true";
        else
            return "false";

    }
}
