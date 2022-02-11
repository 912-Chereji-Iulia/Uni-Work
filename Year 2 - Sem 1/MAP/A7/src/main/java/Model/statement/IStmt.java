package Model.statement;

import Exceptions.FileNotExistsException;
import Exceptions.myExceptions;
import Model.PrgState;
import Model.adt.IDict;
import Model.type.IType;

public interface IStmt {
    PrgState execute_stmt(PrgState state) throws Exception, FileNotExistsException;
    String toString();
    IDict<String,IType> typecheck(IDict<String, IType> typeEnv) throws myExceptions;
    IStmt deepCopy();
}
