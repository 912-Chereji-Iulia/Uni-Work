package Model.adt;

import java.util.Collection;

import java.util.Map;

public interface IDict<T1,T2> {
    Collection<T2> values();
    void add(T1 v1, T2 v2);
    void remove(T1 v1) throws Exception;
    T2 get_val(T1 id);
    boolean containsKey(T1 id);
    void update(T1 id, T2 value);
    String toString();
    Map<T1,T2> getDictionary();
}
