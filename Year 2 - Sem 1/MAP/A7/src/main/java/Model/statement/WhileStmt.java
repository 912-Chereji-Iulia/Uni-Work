package Model.statement;

import Exceptions.myExceptions;
import Model.PrgState;
import Model.adt.IDict;
import Model.adt.IHeap;
import Model.adt.IStack;
import Model.expression.Expression;
import Model.type.BoolType;
import Model.type.IType;
import Model.value.BoolValue;
import Model.value.IValue;

public class WhileStmt implements IStmt{
    private Expression exp;
    private IStmt stmt;
    public WhileStmt(Expression e, IStmt s){
        this.exp=e;
        this.stmt=s;
    }
    @Override
    public PrgState execute_stmt(PrgState state) throws Exception {
        IStack<IStmt> stack= state.get_executions_stack();
        IDict<String, IValue> symbolTable = state.get_SymTable();
        IHeap<Integer,IValue> heapTable = state.get_heap();
        IValue expressionResult;

        expressionResult = exp.evaluate(symbolTable, heapTable);

        if(expressionResult.get_type().equals(new BoolType()))
        {

            BoolValue boolValue = (BoolValue) expressionResult;
            if(boolValue.getVal())
            {
                stack.push(this);
                stack.push(stmt);
            }
        }
        else throw new Exception("condition expression is not a boolean");

        return null;
    }

    public String toString(){
        return "WHILE( " + exp.toString() + ") { " + stmt.toString() + " }";
    }

    @Override
    public IDict<String, IType> typecheck(IDict<String, IType> typeEnv) throws myExceptions {
        IType typeExp=this.exp.typecheck(typeEnv);
        if(typeExp.equals(new BoolType()))
            return typeEnv;
        else throw new myExceptions("condition expression is not a boolean");
    }

    @Override
    public IStmt deepCopy() {
        return new WhileStmt(exp,stmt);
    }


}
