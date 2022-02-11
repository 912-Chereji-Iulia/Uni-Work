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

public class OpenRFile implements IStmt {
    private Expression exp;
    public OpenRFile(Expression e){
        this.exp=e;

    }
    @Override
    public String toString() {
        return "(open_file '" + this.exp +"')";
    }

    @Override
    public PrgState execute_stmt(PrgState state) throws Exception {
        IDict<StringValue, BufferedReader> ft=state.get_fileTable();
        IDict<String, IValue> symTable= state.get_SymTable();
        IValue cond=exp.evaluate(symTable, state.get_heap());
        if(cond.get_type().equals(new StringType())){
            StringValue val= (StringValue) cond;
            if(!ft.containsKey(val)){
                BufferedReader reader=null;
                try{
                    reader=new BufferedReader(new FileReader(val.getVal()));

                }catch (IOException e) {
                    throw new FileNotExistsException(e.getMessage());
                }
                ft.add(val,reader);
            }else throw new myExceptions("File Descriptor exists.");
        }else throw new myExceptions(" expression not of type string.");
        return state;
    }
}
