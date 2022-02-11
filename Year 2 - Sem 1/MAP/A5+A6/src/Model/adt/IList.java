package Model.adt;

import Exceptions.myExceptions;

import java.util.ArrayList;
import java.util.List;

public interface IList<T> {
    void add(T val);
    T get(int index);
    int size();
    String toString();
    T pop() throws Exception;
    boolean isEmpty();
    List<T> getList();
}
