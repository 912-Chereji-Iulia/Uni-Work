package Model.expression;

import Model.adt.Heap;
import Model.adt.IDict;
import Model.adt.IHeap;
import Model.value.IValue;
import Model.value.IntValue;

public abstract class Expression {

    public abstract IValue evaluate(IDict<String,IValue> symTable, IHeap<Integer, IValue> heap) throws Exception;
    public abstract String toString();
}
