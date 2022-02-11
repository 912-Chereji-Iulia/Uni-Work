package Model.statement;

import Exceptions.FileNotExistsException;
import Exceptions.myExceptions;
import Model.PrgState;
import Model.adt.IDict;
import Model.expression.Expression;
import Model.type.IntType;
import Model.type.StringType;
import Model.value.IValue;
import Model.value.IntValue;
import Model.value.StringValue;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class ReadFile implements IStmt{
    private String vname;
    private Expression exp;
    public ReadFile(Expression e, String name){
        this.exp=e;
        this.vname=name;
    }
    @Override
    public PrgState execute_stmt(PrgState state) throws Exception {
        IDict<StringValue, BufferedReader> ft=state.get_fileTable();
        IDict<String, IValue> symTable= state.get_SymTable();
        if(symTable.containsKey(vname)){
            IValue v=symTable.get_val(vname);
            if(v.get_type().equals(new IntType())){
                IValue cond=exp.evaluate(symTable,state.get_heap());
                if(cond.get_type().equals(new StringType())){
                    StringValue val= (StringValue) cond;
                    if(ft.containsKey(val)){
                        BufferedReader reader=ft.get_val(val);
                        String line=reader.readLine();
                        if(line==null){
                            symTable.update(vname,new IntValue(0));
                        }
                        else
                            symTable.update(vname,new IntValue(Integer.parseInt(line)));
                    }else throw new FileNotExistsException("");
                }else throw new myExceptions(" expression not of type string.");
            }else throw  new myExceptions("not int");

        }else throw new myExceptions("Undefined variable");

        return state;
    }
    @Override
    public String toString() {
        return "(read_file' " + this.exp +"')";
    }
}
