package Repo;

import Exceptions.myExceptions;
import Model.PrgState;
import Model.adt.IList;

import java.io.IOException;
import java.util.List;

public interface IRepo {
    //PrgState get_current_program();
    void add_program(PrgState new_program);
    void logPrgStateExec(PrgState prgState) throws myExceptions, IOException;
    List<PrgState> getProgramStateList();
    void setProgramStateList(List<PrgState> newProgramStateList);
}
