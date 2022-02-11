package Model.statement;

import Model.PrgState;

public interface IStmt {
    PrgState execute_stmt(PrgState state) throws Exception;
    String toString();
}
