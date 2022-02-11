package Model.expression;

import Exceptions.myExceptions;
import Model.adt.IDict;
import Model.type.BoolType;
import Model.type.IntType;
import Model.value.IValue;

public class ValueExp extends Expression {
    private final IValue val;

    public ValueExp(IValue _val) {
        this.val = _val;
    }

    @Override
    public IValue evaluate(IDict<String, IValue> symTable) throws Exception {
        if (val.get_type().equals(new IntType()) || val.get_type().equals(new BoolType())) {
            return val;
        }
        throw new myExceptions("Unknown type specified.\n");
    }

    @Override
    public String toString() {

        return this.val.toString();
    }
}
