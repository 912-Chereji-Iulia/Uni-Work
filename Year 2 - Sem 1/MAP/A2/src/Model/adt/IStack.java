package Model.adt;

import Exceptions.myExceptions;

public interface IStack<T> {
    T pop() throws Exception;
    void push(T v);
    boolean isEmpty();
    String toString();
}
