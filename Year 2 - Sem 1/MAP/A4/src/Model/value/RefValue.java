package Model.value;

import Model.type.IType;
import Model.type.RefType;

public class RefValue implements IValue{
    int address;
    IType location_type;

    public RefValue(int add, IType lt){
        this.address=add;
        this.location_type=lt;
    }

    public int get_address(){
        return this.address;
    }

    public IType get_location_type() {
        return this.location_type;
    }


    @Override
    public IType get_type() {
        return new RefType(location_type);
    }


    @Override
    public IValue deep_copy() {
        return new RefValue(address,location_type);
    }

    @Override
    public String toString(){
        return "("+address+","+location_type.toString()+")";
    }
}
