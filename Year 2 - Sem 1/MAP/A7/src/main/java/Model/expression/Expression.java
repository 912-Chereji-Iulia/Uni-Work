package Model.expression;

import Exceptions.myExceptions;
import Model.adt.IDict;
import Model.adt.IHeap;
import Model.type.IType;
import Model.value.IValue;

public abstract class Expression {

    public abstract IValue evaluate(IDict<String,IValue> symTable, IHeap<Integer, IValue> heap) throws Exception;
    public abstract String toString();
    public abstract IType typecheck(IDict<String,IType> typeEnv) throws myExceptions;


}
