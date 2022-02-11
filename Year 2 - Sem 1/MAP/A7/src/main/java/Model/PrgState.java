package Model;

import Exceptions.myExceptions;
import Model.adt.*;
import Model.statement.IStmt;
import Model.value.IValue;
import Model.value.StringValue;

import java.io.BufferedReader;

public class PrgState {
    IStack<IStmt> execution_stack;
    IDict<String, IValue> symTable;
    IList<IValue> output;
    IStmt original_program;
    IDict<StringValue, BufferedReader>  file_table;
    IHeap<Integer,IValue> heap;
    private int id;
    private static int count=0;



    public PrgState(IStack<IStmt> s, IDict<String, IValue> table, IList<IValue> out, IStmt or_prg,IDict<StringValue, BufferedReader> ft, IHeap<Integer,IValue> h){
        this.execution_stack=s;
        this.symTable=table;
        this.output=out;
        this.original_program=or_prg;
        this.file_table=ft;
        this.heap=h;
        this.id=get_Threadid();

    }

    public PrgState(IStmt originalProgram) {
        execution_stack = new MyStack<>();
        symTable = new MyDict<>();
        file_table = new MyDict<>();
        heap = new Heap<>();
        output = new MyList<>();
        this.original_program = originalProgram.deepCopy();
        this.id=get_Threadid();
        execution_stack.push(originalProgram);
    }

    public synchronized static int get_Threadid(){
        count++;
        return count-1;
    }
    public IStack<IStmt> get_executions_stack() {

        return this.execution_stack;
    }
    public IDict<String, IValue> get_SymTable(){

        return this.symTable;
    }
    public IList<IValue> get_output(){

        return this.output;
    }

    public IDict<StringValue, BufferedReader>  get_fileTable(){
        return this.file_table;
    }

    public IHeap<Integer,IValue> get_heap(){return this.heap;}
    public Integer get_id(){return this.id;}


    public String toString(){
        return "Id: "+this.id+"\nExecution stack: " + this.execution_stack.toString() + "\nSymbol Table: " + this.symTable.toString() + "\nOutput: " +
                this.output.toString() +"\nFileTable: "+this.file_table.toString()+"\nHeap: "+this.heap.toString()+ "\n";
    }

    public void set_execution_stack(IStack<IStmt> stack) {
        this.execution_stack=stack;
    }

    public Boolean isNotCompleted(){
        return !execution_stack.isEmpty();
    }

    public PrgState oneStep() throws Exception {

        if(execution_stack.isEmpty())
            throw new myExceptions("Program state stack is empty");
        IStmt current_statement = execution_stack.pop();
        return current_statement.execute_stmt(this);
    }

}
