package Model.type;

import Model.value.IValue;
import Model.value.StringValue;

public class StringType implements IType{

    @Override
    public IValue default_value() {
        return new StringValue(" ");
    }

    @Override
    public IType deep_copy() {
        return new StringType();
    }

    @Override
    public boolean equals(Object o){
        return o != null && o.getClass() == this.getClass();
    }

    @Override
    public String toString(){

        return "string";
    }
}
