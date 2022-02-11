package Model.type;

import Model.value.IValue;
import Model.value.RefValue;

public class RefType implements IType{
    IType inner;
    public RefType(IType in){
        this.inner=in;
    }

    public RefType() {}

    public IType getInner(){
        return this.inner;
    }
    public boolean equals(Object another){
        if(another instanceof RefType)
            return inner.equals(((RefType) another).getInner());
        else return false;
    }
    public String toString(){
        return "Ref("+inner.toString()+")";
    }
    @Override
    public IValue default_value() {
        return new RefValue(0,inner);
    }

    @Override
    public IType deep_copy() {
        return new RefType();
    }
}
