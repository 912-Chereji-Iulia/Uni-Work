package Model.statement;

import Exceptions.DeclarationException;
import Exceptions.myExceptions;
import Model.PrgState;
import Model.adt.IDict;
import Model.expression.Expression;
import Model.type.IType;
import Model.value.IValue;

import java.lang.reflect.Type;

public class AssignStmt implements IStmt{
    private Expression expression;
    private String id;
    public AssignStmt(String i, Expression e){
        this.id=i;
        this.expression=e;
    }

    @Override
    public PrgState execute_stmt(PrgState state) throws Exception {
        IDict<String, IValue> symTable=state.get_SymTable();
        if(symTable.containsKey(this.id)){
            IValue v=this.expression.evaluate(symTable, state.get_heap());
            IType type_id= symTable.get_val(this.id).get_type();
            if(v.get_type().equals(type_id)){
                symTable.update(this.id,v);

            }
            else
                throw new DeclarationException("types dont match");

        }
        else
            throw new DeclarationException("variable not declared before");
        return null;
    }

    public String toString(){
        return this.id+'='+this.expression.toString();
    }

    @Override
    public IDict<String, IType> typecheck(IDict<String, IType> typeEnv) throws myExceptions {
        IType typeVar= typeEnv.get_val(id);
        IType typeExp=expression.typecheck(typeEnv);
        if(typeVar.equals(typeExp)){
            return typeEnv;
        } else throw new myExceptions("types dont match");
    }
}
