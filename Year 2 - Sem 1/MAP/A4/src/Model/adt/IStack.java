package Model.adt;

import Exceptions.myExceptions;

import java.util.Stack;

public interface IStack<T> {
    T pop() throws Exception;
    void push(T v);
    boolean isEmpty();
    String toString();
    Stack<T> getStack();
}
