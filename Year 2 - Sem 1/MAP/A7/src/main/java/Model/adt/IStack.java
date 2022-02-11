package Model.adt;

import java.util.Stack;

public interface IStack<T> {
    T pop() throws Exception;
    void push(T v);
    boolean isEmpty();
    String toString();
    Stack<T> getStack();

    void setContent(Stack<T> content);
}
