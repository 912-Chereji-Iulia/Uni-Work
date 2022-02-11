package Model;

import Model.adt.IDict;
import Model.adt.IList;
import Model.adt.IStack;
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


    public PrgState(IStack<IStmt> s, IDict<String, IValue> table, IList<IValue> out, IStmt or_prg,IDict<StringValue, BufferedReader> ft){
        this.execution_stack=s;
        this.symTable=table;
        this.output=out;
        this.original_program=or_prg;
        this.file_table=ft;
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

    public String toString(){
        return "Execution stack: " + this.execution_stack.toString() + "\nSymbol Table: " + this.symTable.toString() + "\nOutput: " +
                this.output.toString() +"\nFileTable: "+this.file_table.toString()+ "\n";
    }

}
