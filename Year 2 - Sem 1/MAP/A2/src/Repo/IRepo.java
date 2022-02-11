package Repo;

import Model.PrgState;

public interface IRepo {
    PrgState get_current_program();
    void add_program(PrgState new_program);
}
