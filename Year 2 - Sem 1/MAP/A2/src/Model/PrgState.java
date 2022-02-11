package Model;

import Model.adt.IDict;
import Model.adt.IList;
import Model.adt.IStack;
import Model.statement.IStmt;
import Model.value.IValue;

public class PrgState {
    IStack<IStmt> execution_stack;
    IDict<String, IValue> symTable;
    IList<IValue> output;
    IStmt original_program;

    public PrgState(IStack<IStmt> s, IDict<String, IValue> table, IList<IValue> out, IStmt or_prg){
        this.execution_stack=s;
        this.symTable=table;
        this.output=out;
        this.original_program=or_prg;
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

    public String toString(){
        return "Execution stack: " + this.execution_stack.toString() + "\nSymbol Table: " + this.symTable.toString() + "\nOutput: " +
                this.output.toString() + "\n";
    }

}
