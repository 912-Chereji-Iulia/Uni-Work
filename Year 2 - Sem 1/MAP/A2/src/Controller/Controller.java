package Controller;

import Exceptions.myExceptions;
import Model.PrgState;
import Model.adt.IStack;
import Model.statement.IStmt;
import Repo.IRepo;

public class Controller {
    private IRepo repo;
    public Controller(IRepo r){

        this.repo=r;
    }

    public void add_program(PrgState prg){
        this.repo.add_program(prg);
    }

    public void oneStep(PrgState state) throws Exception {
        IStack<IStmt> stack = state.get_executions_stack();
        if(stack.isEmpty())
            throw new myExceptions("Program state stack is empty");
        IStmt current_statement = stack.pop();
        current_statement.execute_stmt(state);
    }

    public void allStep() throws Exception {
        PrgState prg = this.repo.get_current_program();
        System.out.println(prg.toString());
        try{
            while(!prg.get_executions_stack().isEmpty())
            {
                oneStep(prg);
                System.out.println(prg.toString());
            }
        } catch (Exception e)
        {
            System.out.println(e.getMessage());
        }

    }

}
