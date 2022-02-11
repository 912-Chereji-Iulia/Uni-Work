package Model.expression;

import Model.adt.IDict;
import Model.adt.IHeap;
import Model.type.RefType;
import Model.value.IValue;
import Model.value.RefValue;

public class HeapReading extends Expression{
    private Expression expression;

    public HeapReading(Expression e){
        this.expression=e;
    }

    @Override
    public IValue evaluate(IDict<String, IValue> symTable, IHeap<Integer, IValue> heap) throws Exception {
        IValue val=this.expression.evaluate(symTable,heap);
        IValue valuefromHeap;
        if(val.get_type() instanceof RefType){

            RefValue refValue= (RefValue) val;
            int addr=refValue.get_address();
            if(heap.isDefined(addr)){
                valuefromHeap=heap.getValue(addr);
            } else throw new Exception("the address does not exist in the heap");

        }else throw new Exception("Not ref type");
        return valuefromHeap;
    }

    @Override
    public String toString() {
        return "readHeap(" + this.expression.toString() + ")";
    }
}
