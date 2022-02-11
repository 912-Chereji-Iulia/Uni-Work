package Model.statement;

import Model.PrgState;
import Model.adt.IDict;
import Model.adt.IList;
import Model.adt.IStack;
import Model.expression.Expression;
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
        return state;
    }

    public String toString(){
        return "print(" +expression.toString()+")";
    }
}
