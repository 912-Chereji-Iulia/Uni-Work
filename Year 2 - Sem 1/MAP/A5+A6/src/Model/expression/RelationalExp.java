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

public class RelationalExp extends Expression{
    private String operator;
    private Expression e1,e2;

    public RelationalExp(Expression f,Expression s, String op){
        this.e1=f;
        this.e2=s;
        this.operator=op;

    }

    @Override
    public IValue evaluate(IDict<String, IValue> symTable, IHeap<Integer,IValue> heap) throws Exception {
        IValue v1 = e1.evaluate(symTable,heap);

        if (v1.get_type().equals(new IntType())) {
            IValue v2 = e2.evaluate(symTable,heap);
            if (v2.get_type().equals(new IntType())) {
                IntValue nr1 = (IntValue)v1;
                IntValue nr2 = (IntValue)v2;

                switch (operator) {
                    case ">":
                        return new BoolValue(nr1.getVal()> nr2.getVal());
                    case "<":
                        return new BoolValue(nr1.getVal() < nr2.getVal());
                    case "<=":
                        return new BoolValue(nr1.getVal() <= nr2.getVal());
                    case ">=":
                        return new BoolValue(nr1.getVal() >= nr2.getVal());
                    case "==":
                        return new BoolValue(nr1.getVal() == nr2.getVal());
                    case "!=" :
                        return new BoolValue(nr1.getVal() != nr2.getVal());

                }
            }
            else {
                throw new myExceptions("Operand 2 is not an integer.\n");
            }
        } else {
            throw new myExceptions("Operand 1 is not an integer.\n");
        }
        return null;
    }


    @Override
    public String toString() {
        return e1.toString()+operator+e2.toString();
    }

    public IType typecheck(IDict<String,IType> typeEnv) throws myExceptions{
        IType t1,t2;
        t1=e1.typecheck(typeEnv);
        t2=e1.typecheck(typeEnv);
        if (t1.equals(new IntType())){
            if (t2.equals(new IntType())){
                return new BoolType();
            }else throw new myExceptions("second is not int");
        }else throw new myExceptions("first is not int");
    }
}
