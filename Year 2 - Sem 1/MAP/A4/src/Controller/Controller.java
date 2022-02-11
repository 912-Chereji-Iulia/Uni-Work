package Controller;

import Exceptions.myExceptions;
import Model.PrgState;
import Model.adt.IStack;
import Model.statement.IStmt;
import Model.value.IValue;
import Model.value.RefValue;
import Repo.IRepo;

import java.util.Collection;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

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
        repo.logPrgStateExec();
        System.out.println(prg.toString());
        try{
            while(!prg.get_executions_stack().isEmpty())
            {
                oneStep(prg);
                repo.logPrgStateExec();
                prg.get_heap().setContent(garbage_collector(get_usedAddr(prg.get_SymTable().getDictionary().values(),prg.get_heap().getContent().values()),prg.get_heap().getContent()));
                repo.logPrgStateExec();
                System.out.println(prg.toString());
            }
        } catch (Exception e)
        {
            System.out.println(e.getMessage());
        }

    }
    private Map<Integer, IValue> garbage_collector(List<Integer> used_addresses, Map<Integer, IValue> heap)
    {
        //remove addresses that are not refferred from Symtable and from other Heap table entries
        return heap.entrySet().stream()
                .filter(e -> used_addresses.contains(e.getKey()))
                .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));
    }

    List<Integer> get_usedAddr(Collection<IValue> symTableValues,Collection<IValue> heapTableValues){
        List<Integer> symbols_table_addresses= symTableValues.stream()
                .filter(v-> v instanceof RefValue)
                .map(v-> {RefValue v1 = (RefValue)v;
                    return v1.get_address();})
                .collect(Collectors.toList());
        List<Integer> heap_table_addresses = heapTableValues.stream()
                .filter(v -> v instanceof RefValue)
                .map(value->{RefValue value2 = (RefValue) value;
                    return value2.get_address();})
                .collect(Collectors.toList());

        symbols_table_addresses.addAll(heap_table_addresses);
        return symbols_table_addresses;

    }
}
