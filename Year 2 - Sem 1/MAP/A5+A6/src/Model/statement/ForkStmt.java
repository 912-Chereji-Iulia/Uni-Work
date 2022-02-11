package Model.statement;

import Exceptions.FileNotExistsException;
import Exceptions.myExceptions;
import Model.PrgState;
import Model.adt.IDict;
import Model.adt.IStack;
import Model.adt.MyStack;
import Model.type.IType;

public class ForkStmt implements IStmt{
    private IStmt stmt;

    public ForkStmt(IStmt s){
        this.stmt=s;

    }

    @Override
    public PrgState execute_stmt(PrgState state) throws Exception {
        IStack<IStmt> newStack = new MyStack<>();
        newStack.push(stmt);

        return new PrgState(newStack,state.get_SymTable().deepCopy(),state.get_output(),this.stmt,state.get_fileTable(),state.get_heap());

    }
    @Override
    public String toString(){
        return "fork("+this.stmt+")";
    }

    @Override
    public IDict<String, IType> typecheck(IDict<String, IType> typeEnv) throws myExceptions {
        return this.stmt.typecheck(typeEnv);
    }
}
