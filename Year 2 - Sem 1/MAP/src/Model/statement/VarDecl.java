package Model.statement;

import Exceptions.DeclarationException;
import Model.PrgState;

import Model.adt.IDict;
import Model.adt.IStack;
import Model.type.IType;
import Model.value.IValue;

public class VarDecl implements IStmt{
    IType type;
    String varname;

    public VarDecl( String name,IType t){
        this.type=t;
        this.varname=name;
    }
    @Override
    public PrgState execute_stmt(PrgState state) throws Exception {

        IDict<String, IValue> symTable= state.get_SymTable();
        if(symTable.containsKey(this.varname))
            throw new DeclarationException("Variable is already declared.");
        else
        {
            IValue val=this.type.default_value();
            symTable.add(varname,val);

        }
        return state;
    }

    public String toString(){
        return this.type.toString()+" "+this.varname;
    }
}
