package Repo;

import Model.PrgState;
import Model.adt.MyList;

public class Repo implements IRepo {

    private MyList<PrgState> program_states;

    public Repo(){
        this.program_states=new MyList<PrgState>();
    }

    @Override
    public PrgState get_current_program() {
        return this.program_states.get(this.program_states.size()-1);
    }

    @Override
    public void add_program(PrgState new_program) {
        this.program_states.add(new_program);
    }
}
