package Model.statement;

import Exceptions.FileNotExistsException;
import Model.PrgState;

public interface IStmt {
    PrgState execute_stmt(PrgState state) throws Exception, FileNotExistsException;
    String toString();


}
