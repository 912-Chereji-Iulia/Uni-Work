package Model.statement;

import Exceptions.myExceptions;
import Model.PrgState;
import Model.adt.IDict;
import Model.type.IType;

public class NOPStmt implements IStmt{

    @Override
    public PrgState execute_stmt(PrgState state) throws Exception {
        return null;
    }

    @Override
    public IDict<String, IType> typecheck(IDict<String, IType> typeEnv) throws myExceptions {
        return typeEnv;
    }
}
