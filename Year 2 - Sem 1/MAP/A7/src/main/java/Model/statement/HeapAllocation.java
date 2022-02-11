package Model.statement;

import Exceptions.myExceptions;
import Model.PrgState;
import Model.adt.IDict;
import Model.adt.IHeap;
import Model.expression.Expression;
import Model.type.IType;
import Model.type.RefType;
import Model.value.IValue;
import Model.value.RefValue;


public class HeapAllocation implements IStmt{
    private String var_name;
    private Expression expression;
    public HeapAllocation(String vn, Expression e){
        this.expression=e;
        this.var_name=vn;
    }

    @Override
    public PrgState execute_stmt(PrgState state) throws Exception {
        IDict<String, IValue> symTable=state.get_SymTable();
        IHeap<Integer,IValue> heap=state.get_heap();
        if(symTable.containsKey(var_name)){
            if( symTable.get_val(var_name).get_type() instanceof RefType){
                IValue v=expression.evaluate(symTable,heap);
                RefType refvar= (RefType) symTable.get_val(var_name).get_type();
                if(v.get_type().equals(refvar.getInner())){
                    heap.add(v);
                    RefValue new_refval=new RefValue(heap.getAddress(v),v.get_type());
                    symTable.update(var_name,new_refval);

                }
                else throw new Exception("The type of the variable and the type of the expression do not match");

            } else
                throw new Exception("The type of the variable is not reference type");

        }
        else
            throw new Exception("The variable name is not defined in the symbol table");

        return null;
    }
    @Override
    public String toString() {
        return "new(" + this.var_name + "," + this.expression.toString() + ")";
    }

    @Override
    public IDict<String, IType> typecheck(IDict<String, IType> typeEnv) throws myExceptions {
        IType typeVar=typeEnv.get_val(this.var_name);
        IType typeExp= expression.typecheck(typeEnv);
        if(typeVar.equals(new RefType(typeExp)))
            return typeEnv;
        else throw new myExceptions("The type of the variable is not reference type");

    }

    @Override
    public IStmt deepCopy() {
        return new HeapAllocation(var_name,expression);
    }
}
