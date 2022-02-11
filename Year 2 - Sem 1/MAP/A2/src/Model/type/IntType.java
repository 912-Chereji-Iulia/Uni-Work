package Model.type;

import Model.value.IValue;
import Model.value.IntValue;

public class IntType implements IType{

    @Override
    public IValue default_value() {
        return new IntValue(0);
    }

    @Override
    public IType deep_copy() {
        return new IntType();
    }
    @Override
    public boolean equals(Object o){
        return o != null && o.getClass() == this.getClass();
    }

    @Override
    public String toString(){

        return "int";
    }

}
