package Model.adt;

import Exceptions.ADTException;

import java.util.ArrayList;
import java.util.List;

public class MyList<T> implements IList<T>{
    private List<T> l;

    public MyList(){
        this.l=new ArrayList<T>();
    }

    @Override
    public void add(T val) {
        this.l.add(val);
    }

    @Override
    public T get(int index) {
        return this.l.get(index);
    }

    @Override
    public int size() {
        return this.l.size();

    }
    @Override
    public String toString(){

        return this.l.toString();
    }

    @Override
    public T pop() throws Exception {
       if(isEmpty())
           throw new ADTException("Empty list!");
       return this.l.remove(this.l.size()-1);
    }

    @Override
    public boolean isEmpty() {
        return this.l.isEmpty();
    }

    @Override
    public List<T> getList() {
        return this.l;
    }
}
