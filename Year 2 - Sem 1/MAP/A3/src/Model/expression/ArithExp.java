package Model.expression;

import Exceptions.DivisionByZero;
import Exceptions.myExceptions;
import Model.adt.IDict;
import Model.type.IntType;
import Model.value.IValue;
import Model.value.IntValue;

public class ArithExp extends Expression {

    private char operation;
    private Expression exp1,exp2;
    public ArithExp(char op, Expression e1, Expression e2){
        this.operation=op;
        this.exp1=e1;
        this.exp2=e2;
    }
    @Override
    public IValue evaluate(IDict<String, IValue> symTable) throws Exception {
       IValue v1=exp1.evaluate(symTable);
       if(v1.get_type().equals(new IntType())){
           IValue v2=exp2.evaluate(symTable);
           if(v2.get_type().equals(new IntType())){
               IntValue i1=(IntValue) v1;
               IntValue i2=(IntValue) v2;
               int n1=i1.getVal(),n2=i2.getVal();
               switch (operation){
                   case '+':
                       return new IntValue(n1+n2);
                   case '-':
                       return new IntValue(n1-n2);
                   case '*':
                       return new IntValue(n1*n2);
                   case '/':
                       if(n2==0) throw new DivisionByZero("Division by 0!");
                       return new IntValue(n1/n2);

               }

           }else
               throw new myExceptions("second is not int");
       }else
           throw new myExceptions("first is not int");
    return null;
    }

    @Override
    public String toString() {
        return exp1.toString() + " " + operation + " " + exp2.toString();
    }
}
