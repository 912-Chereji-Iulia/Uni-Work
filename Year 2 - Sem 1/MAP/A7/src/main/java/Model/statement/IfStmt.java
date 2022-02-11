package Model.statement;

import Exceptions.myExceptions;
import Model.PrgState;
import Model.adt.IDict;
import Model.adt.IStack;
import Model.expression.Expression;
import Model.type.BoolType;
import Model.type.IType;
import Model.value.BoolValue;
import Model.value.IValue;

public class IfStmt implements IStmt{

    private Expression expression;
    private IStmt first;
    private IStmt else_stmt;

    public IfStmt(Expression e,IStmt i1, IStmt i2){
        this.expression=e;
        this.first=i1;
        this.else_stmt=i2;
    }
    @Override
    public PrgState execute_stmt(PrgState state) throws Exception {
        IStack<IStmt> stack=state.get_executions_stack();
        IDict<String, IValue> symTable= state.get_SymTable();
        IValue v=this.expression.evaluate(symTable, state.get_heap());
        if(v.get_type().equals(new BoolType()))
        {
            BoolValue b=(BoolValue) v;
            boolean bool_val=b.getVal();
            if(bool_val)
                stack.push(first);
            else stack.push(else_stmt);

        }
        else throw new myExceptions("Condition exp is not bool");
        return null;

    }
    public String toString(){
        return "(IF("+ expression.toString()+") THEN(" +first.toString()  +")ELSE("+else_stmt.toString()+"))";
    }

    @Override
    public IDict<String, IType> typecheck(IDict<String, IType> typeEnv) throws myExceptions {
        IType typeExp=expression.typecheck(typeEnv);
        if(typeExp.equals(new BoolType())){
            first.typecheck(typeEnv.deepCopy());
            else_stmt.typecheck(typeEnv.deepCopy());
            return typeEnv;
        }else throw new myExceptions("Condition exp is not bool");
    }

    @Override
    public IStmt deepCopy() {
        return new IfStmt(expression,first,else_stmt);
    }
}
