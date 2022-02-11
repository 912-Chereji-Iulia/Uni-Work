package Model.statement;

import Exceptions.FileNotExistsException;
import Exceptions.myExceptions;
import Model.PrgState;
import Model.adt.IDict;
import Model.expression.Expression;
import Model.type.StringType;
import Model.value.IValue;
import Model.value.StringValue;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class CloseRFile implements IStmt{
    private Expression exp;
    public CloseRFile(Expression e){
        this.exp=e;

    }
    @Override
    public String toString() {
        return "(close file '" + this.exp +"')";
    }

    @Override
    public PrgState execute_stmt(PrgState state) throws Exception {
        IDict<StringValue, BufferedReader> ft=state.get_fileTable();
        IDict<String, IValue> symTable= state.get_SymTable();
        IValue cond=exp.evaluate(symTable);
        if(cond.get_type().equals(new StringType())){
            StringValue val= (StringValue) cond;
            if(ft.containsKey(val)){
                BufferedReader reader=ft.get_val(val);
                reader.close();
                ft.remove(val);
            }else throw new myExceptions("unknown entry");
        }else throw new myExceptions(" expression not of type string.");
        return state;
    }
}
