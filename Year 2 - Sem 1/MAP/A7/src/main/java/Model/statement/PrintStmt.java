package Model.statement;

import Exceptions.myExceptions;
import Model.PrgState;
import Model.adt.IDict;
import Model.adt.IList;
import Model.expression.Expression;
import Model.type.IType;
import Model.value.IValue;

public class PrintStmt implements IStmt{

    private Expression expression;
    public PrintStmt(Expression e){
        this.expression=e;
    }

    @Override
    public PrgState execute_stmt(PrgState state) throws Exception {
        IList<IValue> output= state.get_output();
        IDict<String,IValue> symTable=state.get_SymTable();
        IValue v=this.expression.evaluate(symTable, state.get_heap());
        output.add(v);
        return null;
    }

    public String toString(){
        return "print(" +expression.toString()+")";
    }

    @Override
    public IDict<String, IType> typecheck(IDict<String, IType> typeEnv) throws myExceptions {
        expression.typecheck(typeEnv);
        return typeEnv;
    }

    @Override
    public IStmt deepCopy() {
        return new PrintStmt(expression);
    }
}
