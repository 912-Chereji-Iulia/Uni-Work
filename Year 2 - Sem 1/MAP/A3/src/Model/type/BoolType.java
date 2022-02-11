package Model.type;

import Model.value.BoolValue;
import Model.value.IValue;

public class BoolType implements IType {

    @Override
    public IValue default_value() {
        return new BoolValue(false);
    }

    @Override
    public IType deep_copy() {
        return new BoolType();
    }

    @Override
    public boolean equals(Object o)
    {
        return o != null && o.getClass() == this.getClass();
    }
    @Override
    public String toString(){

        return "bool";
    }

}
