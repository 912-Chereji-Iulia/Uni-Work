package Repo;

import Exceptions.myExceptions;
import Model.PrgState;
import Model.adt.*;
import Model.statement.IStmt;
import Model.type.StringType;
import Model.value.IValue;
import Model.value.StringValue;

import java.io.*;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.ListIterator;
import java.util.Map;

public class Repo implements IRepo {

    private String logFilePath;
    private MyList<PrgState> program_states;


    public Repo(String logFile){
        this.program_states=new MyList<PrgState>();
        this.logFilePath=logFile;

    }

    @Override
    public PrgState get_current_program() {
        return this.program_states.get(this.program_states.size()-1);
    }

    @Override
    public void add_program(PrgState new_program) {
        this.program_states.add(new_program);
    }

    @Override
    public void logPrgStateExec() throws myExceptions, IOException {
        PrintWriter logfile;
        logfile=new PrintWriter(new BufferedWriter(new FileWriter(logFilePath, true)));
        IStack<IStmt> stack= get_current_program().get_executions_stack();
        IDict<String, IValue> symTable=get_current_program().get_SymTable();
        IList<IValue> output=get_current_program().get_output();
        IDict<StringValue, BufferedReader> fileTable= get_current_program().get_fileTable();
        logfile.println("ExeStack:");
        ArrayList<IStmt> a=new ArrayList<IStmt>(stack.getStack());
        ListIterator<IStmt> li=a.listIterator(a.size());
        while(li.hasPrevious())
        {
            logfile.println("->"+li.previous().toString());

        }
        logfile.println("SymTable:");
        for(Map.Entry<String, IValue> e : symTable.getDictionary().entrySet())
        {
            logfile.println("-> " + "Key: " + e.getKey().toString() + ", Value: " + e.getValue().toString());
        }
        logfile.println("Out:");
        for(IValue e : output.getList())
        {
            logfile.println("-> " + e.toString());
        }

        logfile.println("FileTable:");
        for(Map.Entry<StringValue, BufferedReader> e : fileTable.getDictionary().entrySet())
        {
            logfile.println("-> " + "Key: " + e.getKey().toString() + ", Value: " + e.getValue().toString());
        }


        logfile.println("------------------------------------------");
        logfile.close();

    }
}
