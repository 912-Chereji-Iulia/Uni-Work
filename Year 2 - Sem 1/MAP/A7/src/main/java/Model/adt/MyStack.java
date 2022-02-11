package Model.adt;

import Exceptions.ADTException;

import java.util.Stack;

public class MyStack<T> implements IStack<T>{

    private Stack<T> s;
    public MyStack(){
        this.s=new Stack<T>();
    }

    @Override
    public T pop() throws Exception {
       if(s.isEmpty())
           throw new ADTException("Empty stack!");
       return this.s.pop();
    }

    @Override
    public void push(T v) {
        this.s.push(v);
    }

    @Override
    public boolean isEmpty() {
        return this.s.isEmpty();
    }

    @Override
    public String toString(){

        return this.s.toString();
    }

    @Override
    public Stack<T> getStack() {
        return this.s;
    }

    @Override
    public void setContent(Stack<T> content) {
        this.s =  content;
    }

}
