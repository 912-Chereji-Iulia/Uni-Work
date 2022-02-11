package Model.expression;

import Model.adt.IDict;
import Model.value.IValue;

public abstract class Expression {
    public abstract IValue evaluate(IDict<String,IValue> symTable) throws Exception;
    public abstract String toString();
}
