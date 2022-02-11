package Model.statement;

import Model.PrgState;
import Model.adt.IStack;

public class CompStmt implements IStmt{

    private IStmt i1,i2;
    public CompStmt(IStmt f, IStmt s){
        this.i1=f;
        this.i2=s;
    }


    @Override
    public PrgState execute_stmt(PrgState state) throws Exception {
        IStack<IStmt> stack=state.get_executions_stack();
        stack.push(i2);
        stack.push(i1);
        return state;
    }

    public String toString(){
        return "("+this.i1.toString()+";"+this.i2.toString()+")";
    }
}
