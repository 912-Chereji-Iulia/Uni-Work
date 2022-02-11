package Model.expression;

import Exceptions.myExceptions;
import Model.adt.IDict;
import Model.adt.IHeap;
import Model.type.IType;
import Model.value.IValue;

public class VarExp extends Expression{
    private String id;

    public VarExp(String i){
        this.id=i;
    }
    @Override
    public IValue evaluate(IDict<String, IValue> symTable, IHeap<Integer,IValue> heap) throws Exception {
        return symTable.get_val(id);
    }

    @Override
    public String toString() {
        return this.id;
    }

    public IType typecheck(IDict<String,IType> typeEnv) throws myExceptions {
        return typeEnv.get_val(id);
    }
}
