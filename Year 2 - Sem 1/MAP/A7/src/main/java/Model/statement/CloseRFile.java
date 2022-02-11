package Model.statement;

import Exceptions.myExceptions;
import Model.PrgState;
import Model.adt.IDict;
import Model.expression.Expression;
import Model.type.IType;
import Model.type.StringType;
import Model.value.IValue;
import Model.value.StringValue;

import java.io.BufferedReader;

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
    public IDict<String, IType> typecheck(IDict<String, IType> typeEnv) throws myExceptions {
        IType typeExp=this.exp.typecheck(typeEnv);
        if(typeExp.equals(new StringType()))
            return typeEnv;
        else throw new myExceptions(" expression not of type string.");
    }

    @Override
    public IStmt deepCopy() {
        return new CloseRFile(exp);
    }

    @Override
    public PrgState execute_stmt(PrgState state) throws Exception {
        IDict<StringValue, BufferedReader> ft=state.get_fileTable();
        IDict<String, IValue> symTable= state.get_SymTable();
        IValue cond=exp.evaluate(symTable, state.get_heap());
        if(cond.get_type().equals(new StringType())){
            StringValue val= (StringValue) cond;
            if(ft.containsKey(val)){
                BufferedReader reader=ft.get_val(val);
                reader.close();
                ft.remove(val);
            }else throw new myExceptions("unknown entry");
        }else throw new myExceptions(" expression not of type string.");
        return null;
    }
}
