package Repo;

import Exceptions.myExceptions;
import Model.PrgState;

import java.io.IOException;

public interface IRepo {
    PrgState get_current_program();
    void add_program(PrgState new_program);
    void logPrgStateExec() throws myExceptions, IOException;
}
