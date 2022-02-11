package Model.value;

import Model.type.IType;
import Model.type.StringType;

import java.util.Objects;

public class StringValue implements IValue{
    String val;
    public StringValue(String i){
        this.val=i;
    }

    public String getVal(){
        return this.val;
    }

    @Override
    public IType get_type() {
        return new StringType();
    }

    @Override
    public IValue deep_copy() {
        return new StringValue(this.val);
    }

    @Override
    public boolean equals(Object o){
        if (o == null || o.getClass() != this.getClass())
            return false;
        StringValue new_val = (StringValue)  o;
        return Objects.equals(new_val.val, this.val);
    }
    public boolean equals(StringValue s) {
        return this.val.equals(s.getVal());
    }
    @Override
    public String toString() {
        return "'" + this.val + "'";
    }

}
