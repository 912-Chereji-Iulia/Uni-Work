package Model.expression;

import Exceptions.myExceptions;
import Model.adt.Heap;
import Model.adt.IDict;
import Model.adt.IHeap;
import Model.type.BoolType;
import Model.type.IType;
import Model.type.IntType;
import Model.value.BoolValue;
import Model.value.IValue;
import Model.value.IntValue;

public class LogicExp extends Expression{
    private String operation;
    private Expression exp1,exp2;

    public LogicExp(String op,Expression e1, Expression e2){
        this.operation=op;
        this.exp1=e1;
        this.exp2=e2;
    }

    @Override
    public IValue evaluate(IDict<String, IValue> symTable, IHeap<Integer,IValue> heap) throws Exception {
        IValue v1=exp1.evaluate(symTable,heap);
        if(v1.get_type().equals(new BoolType())){
            IValue v2=exp2.evaluate(symTable,heap);
            if(v2.get_type().equals(new BoolType())){
                BoolValue i1=(BoolValue) v1;
                BoolValue i2=(BoolValue) v2;
                boolean n1=i1.getVal(),n2=i2.getVal();
                if(operation.equals("and"))
                    return new BoolValue(n1 && n2);
                else if (operation.equals("or"))
                    return new BoolValue(n1 || n2);

            }
            else throw new myExceptions("the second is not boolean!");
        }
        else throw new myExceptions("the first is not boolean!");
        return null;
    }



    @Override
    public String toString() {
        return this.exp1.toString()+this.operation+this.exp2.toString();
    }

    public IType typecheck(IDict<String,IType> typeEnv) throws myExceptions{
        IType t1,t2;
        t1=exp1.typecheck(typeEnv);
        t2=exp1.typecheck(typeEnv);
        if (t1.equals(new BoolType())){
            if (t2.equals(new BoolType())){
                return new BoolType();
            }else throw new myExceptions("second is not boolean");
        }else throw new myExceptions("first is not boolean");
    }
}
