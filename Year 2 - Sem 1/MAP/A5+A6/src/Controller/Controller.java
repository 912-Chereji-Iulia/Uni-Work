package Controller;

import Exceptions.myExceptions;
import Model.PrgState;
import Model.adt.IList;
import Model.adt.IStack;
import Model.adt.MyList;
import Model.statement.IStmt;
import Model.type.RefType;
import Model.value.IValue;
import Model.value.RefValue;
import Repo.IRepo;

import java.io.IOException;
import java.util.Collection;
import java.util.List;
import java.util.Map;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.stream.Collectors;

public class Controller {
    private IRepo repo;
    ExecutorService executor;

    public Controller(IRepo r){

        this.repo=r;
    }

    public void add_program(PrgState prg){
        this.repo.add_program(prg);
    }

    /*
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

    }*/


    public List<PrgState> removeCompletedPrg(List<PrgState> inPrgList){
        return inPrgList.stream()
                .filter(p -> p.isNotCompleted())
                .collect(Collectors.toList());

    }

    public static List<Integer> getAddrFromTable(Collection<IValue> tableValues) {
        return tableValues.stream()
                .filter(v -> v.get_type() instanceof RefType)
                .map(v -> { RefValue v1 = (RefValue) v; return v1.get_address();})
                .collect(Collectors.toList());
    }

    private Map<Integer, IValue> garbage_collector(List<Integer> used_addresses, Map<Integer, IValue> heap)
    {
        List<Integer> heapAddr = getAddrFromTable(heap.values());

        return heap.entrySet().stream()
                .filter(e -> used_addresses.contains(e.getKey()) || heapAddr.contains(e.getKey()))
                .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));
    }

    /*
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

    }*/



    //RUN concurrently one step for each of the existing PrgStates
    void oneStepForAll(List<PrgState> prgList) throws InterruptedException, myExceptions, IOException {
        //prepare the list of callables
        List<Callable<PrgState>> callList = prgList.stream()
                .map((PrgState p) -> (Callable<PrgState>)(() -> { return p.oneStep(); }))
                .collect(Collectors.toList());

        //start the execution of the callables
        // it returns the list of new created PrgStates (namely threads)
        List<PrgState> newPrgList = executor.invokeAll(callList).stream()
                .map(future -> {
                    try { return future.get(); }
                    catch (Exception e) {
                        return null;
                    }
                })
                .filter(p -> p != null)
                .collect(Collectors.toList());

        //add the new created threads to the list of existing threads
        ////after the execution, print the PrgState List into the log file
        prgList.addAll(newPrgList);
        for(PrgState prg : prgList) {
            repo.logPrgStateExec(prg);
        }
        //Save the current programs in the repository
        IList<PrgState> copyPrgList = new MyList<>(prgList);
        repo.setProgramStateList(copyPrgList);
    }

    public void allSteps() throws Exception {
        executor = Executors.newFixedThreadPool(2);

        //remove the completed programs
        IList<PrgState> list = repo.getProgramStateList();
        List<PrgState> prgList = removeCompletedPrg(list.getList());


        while (prgList.size() > 0) {

            for (PrgState prg : prgList) {
                prg.get_heap().setContent(garbage_collector(
                        getAddrFromTable(prg.get_SymTable().values()),
                        prg.get_heap().getContent()));
            }

            oneStepForAll(prgList);

            list = repo.getProgramStateList();
            prgList = removeCompletedPrg(list.getList());

        }
        executor.shutdownNow();

        // update the repository state
        IList<PrgState> copyPrgList = new MyList<>(prgList);
        repo.setProgramStateList(copyPrgList);
    }
    }

