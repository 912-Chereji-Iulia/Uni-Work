package Model.statement;

import Model.PrgState;

public class NOPStmt implements IStmt{

    @Override
    public PrgState execute_stmt(PrgState state) throws Exception {
        return state;
    }
}
