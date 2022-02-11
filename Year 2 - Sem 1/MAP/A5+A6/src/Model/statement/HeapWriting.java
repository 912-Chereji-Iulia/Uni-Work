package Model.statement;

import Exceptions.FileNotExistsException;
import Exceptions.myExceptions;
import Model.PrgState;
import Model.adt.Heap;
import Model.adt.IDict;
import Model.adt.IHeap;
import Model.expression.Expression;
import Model.type.IType;
import Model.type.RefType;
import Model.value.IValue;
import Model.value.RefValue;

public class HeapWriting implements IStmt {
    private String var_name;
    private Expression expression;

    public HeapWriting(String vn,Expression e){
        this.expression=e;
        this.var_name=vn;
    }

    @Override
    public PrgState execute_stmt(PrgState state) throws Exception {
        IDict<String, IValue> symTable=state.get_SymTable();
        IHeap<Integer,IValue> heap=state.get_heap();
        if(symTable.containsKey(var_name)){
            if( symTable.get_val(var_name).get_type() instanceof RefType){
                RefValue val_var_name= (RefValue) symTable.get_val(var_name);
                int addr=val_var_name.get_address();
                if(heap.isDefined(addr)) {
                    IValue v = this.expression.evaluate(symTable, heap);
                    RefType referenceType = (RefType)symTable.get_val(var_name).get_type() ;
                    IType innerType= referenceType.getInner();
                    if(v.get_type().equals(innerType))
                    {
                        heap.update(addr, v);
                    } else throw new Exception("The type of the variable and the type of the expression do not match");
                }else
                    throw new Exception("the address doesn't exist");

                }else
                throw new Exception("The type of the variable is not reference type");

        } else throw new Exception("the variable is not defined in the symbol table");


        return null;
    }

    @Override
    public String toString() {
        return "writeHeap(" + this.var_name + "," + this.expression.toString() + ")";
    }

    @Override
    public IDict<String, IType> typecheck(IDict<String, IType> typeEnv) throws myExceptions {
       IType typeVar= typeEnv.get_val(var_name);
       IType typeExp=this.expression.typecheck(typeEnv);
       if(typeVar.equals(new RefType(typeExp)))
           return typeEnv;
       else throw new myExceptions("The type of the variable is not reference type");
    }
}
