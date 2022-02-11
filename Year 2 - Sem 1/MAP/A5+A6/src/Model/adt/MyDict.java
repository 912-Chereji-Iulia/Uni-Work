package Model.adt;

import Exceptions.myExceptions;

import java.util.Collection;
import java.util.Dictionary;
import java.util.HashMap;
import java.util.Map;

public class MyDict<T1,T2> implements IDict<T1,T2> {

    private Map<T1,T2> d;
    public MyDict(){
        this.d=new HashMap<T1,T2>();
    }
    @Override
    public Collection<T2> values() {
        return this.d.values();
    }

    @Override
    public void add(T1 v1, T2 v2) {
        this.d.put(v1,v2);
    }

    @Override
    public void remove(T1 v1) throws Exception {
        if(containsKey(v1))
            this.d.remove(v1);
        else throw new myExceptions("Undefined variable");
    }

    @Override
    public T2 get_val(T1 id) {
        return this.d.get(id);
    }

    @Override
    public boolean containsKey(T1 id) {
        return this.d.containsKey(id);
    }


    @Override
    public void update(T1 id, T2 value) {
        this.d.replace(id,value);
    }


    @Override
    public String toString(){

        return this.d.toString();
    }

    @Override
    public Map<T1, T2> getDictionary() {
        return this.d;
    }

    @Override
    public IDict<T1, T2> deepCopy() {
        IDict<T1, T2> copyDictionary = new MyDict<T1, T2>();

        for(T1 elem: d.keySet())
            copyDictionary.add(elem, d.get(elem));

        return copyDictionary;
    }

}
