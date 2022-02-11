package Model.statement;

import Exceptions.myExceptions;
import Model.PrgState;
import Model.adt.IDict;
import Model.adt.IStack;
import Model.type.IType;

public class CompStmt implements IStmt{

    private IStmt i1,i2;
    public CompStmt(IStmt f, IStmt s){
        this.i1=f;
        this.i2=s;
    }

    public IStmt getFirstStatement() { return this.i1; }
    public IStmt getSecondStatement() { return this.i2; }
    @Override
    public PrgState execute_stmt(PrgState state) throws Exception {
        IStack<IStmt> stack=state.get_executions_stack();
        stack.push(i2);
        stack.push(i1);
        return null;
    }

    public String toString(){
        return "("+this.i1.toString()+";"+this.i2.toString()+")";
    }

    @Override
    public IDict<String, IType> typecheck(IDict<String, IType> typeEnv) throws myExceptions {
        return i2.typecheck(i1.typecheck(typeEnv));
    }
}
