package Model.expression;

import Exceptions.myExceptions;
import Model.adt.IDict;
import Model.adt.IHeap;
import Model.type.BoolType;
import Model.type.IType;
import Model.type.IntType;
import Model.type.StringType;
import Model.value.IValue;

public class ValueExp extends Expression {
    private final IValue val;

    public ValueExp(IValue _val) {
        this.val = _val;
    }

    @Override
    public IValue evaluate(IDict<String, IValue> symTable, IHeap<Integer,IValue> heap) throws Exception {
        if (val.get_type().equals(new IntType()) || val.get_type().equals(new BoolType())|| val.get_type().equals(new StringType())) {
            return val;
        }
        throw new myExceptions("Unknown type specified.\n");
    }
    @Override
    public String toString() {

        return this.val.toString();
    }

    public IType typecheck(IDict<String, IType> typeEnv) throws myExceptions{
        return val.get_type();
    }
}
