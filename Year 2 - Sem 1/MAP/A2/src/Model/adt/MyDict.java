package Model.adt;

import java.util.Collection;
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
}
