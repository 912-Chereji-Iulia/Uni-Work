package View;

import Controller.Controller;

import Exceptions.myExceptions;
import Model.PrgState;
import Model.adt.*;

import Model.expression.*;
import Model.statement.*;
import Model.type.*;
import Model.value.BoolValue;
import Model.value.IValue;
import Model.value.IntValue;
import Model.value.StringValue;
import Repo.IRepo;
import Repo.Repo;

import java.io.BufferedReader;
import java.util.Scanner;

public class MainProgram {

    public static void main(String[] args) throws Exception {

        // ex 1:  int v; v = 2; Print(v)
        IStmt ex1 = new CompStmt(new VarDecl("v", new IntType()),
                new CompStmt(new AssignStmt("v", new ValueExp(new IntValue(2))),
                        new PrintStmt(new VarExp("v"))));
        // ex 2: int a;int b; a=2+3*5;b=a+1;Print(b)
        IStmt ex2 = new CompStmt(new VarDecl("a", new IntType()), new CompStmt(new VarDecl("b", new IntType()),
                new CompStmt(new AssignStmt("a", new ArithExp('+', new ValueExp(new IntValue(2)), new ArithExp('*',
                        new ValueExp(new IntValue(3)), new ValueExp(new IntValue(5))))), new CompStmt(
                        new AssignStmt("b", new ArithExp('+', new VarExp("a"), new ValueExp(new IntValue(1)))),
                        new PrintStmt(new VarExp("b"))))));

        // ex 3: bool a; int v; a=true;(If a Then v=2 Else v=3); Print(v)
        IStmt ex3 = new CompStmt(new VarDecl("a", new BoolType()), new CompStmt(new VarDecl("v",
                new IntType()), new CompStmt(new AssignStmt("a", new ValueExp(new IntValue())),
                new CompStmt(new IfStmt(new VarExp("a"), new AssignStmt("v", new ValueExp(new IntValue(2))),
                        new AssignStmt("v", new ValueExp(new IntValue(3)))), new PrintStmt(new
                        VarExp("v"))))));

        IStmt ex4 = new CompStmt(new VarDecl("varf", new StringType()),
                new CompStmt(new AssignStmt("varf", new ValueExp(new StringValue("test.txt"))),
                        new CompStmt(new OpenRFile(new VarExp("varf")),
                                new CompStmt(new VarDecl("varc", new IntType()),
                                        new CompStmt(new ReadFile(new VarExp("varf"), "varc"),
                                                new CompStmt(new PrintStmt(new VarExp("varc")),
                                                        new CompStmt(new ReadFile(new VarExp("varf"), "varc"),
                                                                new CompStmt(new PrintStmt(new VarExp("varc")),
                                                                        new CloseRFile(new VarExp("varf"))))))))));

        //int v; v=4; (while (v>0) print(v);v=v-1);print(v)
        IStmt ex5 = new CompStmt(new VarDecl("v", new IntType()),
                new CompStmt(new AssignStmt("v", new ValueExp(new IntValue(4))),
                        new CompStmt(new WhileStmt(new RelationalExp(new VarExp("v"),new ValueExp(new IntValue(0)),">"),
                                new CompStmt(new PrintStmt(new VarExp("v")),
                                        new AssignStmt("v", new ArithExp('-',
                                                new VarExp("v"), new ValueExp(new IntValue(1)))))),
                                new PrintStmt(new VarExp("v")))));

        // Ref int v;new(v,20);Ref Ref int a; new(a,v);print(v);print(a)
        IStmt ex6=new CompStmt(new VarDecl("v", new RefType(new IntType())),
                new CompStmt(new HeapAllocation("v", new ValueExp(new IntValue(20))),
                        new CompStmt(new VarDecl("a", new RefType(new RefType(new IntType()))),
                                new CompStmt(new HeapAllocation("a", new VarExp("v")),
                                        new CompStmt(new PrintStmt(new VarExp("v")),
                                                new PrintStmt(new VarExp("a")))))));

        // Ref int v;new(v,20);Ref Ref int a; new(a,v);print(rH(v));print(rH(rH(a))+5)
        IStmt ex7 = new CompStmt(new VarDecl("v", new RefType(new IntType())),
                new CompStmt(new HeapAllocation("v", new ValueExp(new IntValue(20))),
                        new CompStmt(new VarDecl("a", new RefType(new RefType(new IntType()))),
                                new CompStmt(new HeapAllocation("a", new VarExp("v")),
                                        new CompStmt(new PrintStmt(new HeapReading(new VarExp("v"))),
                                                new PrintStmt(new ArithExp('+',
                                                        new HeapReading(new HeapReading(new VarExp("a"))),
                                                        new ValueExp(new IntValue(5)))))))));

        // Ref int v;new(v,20);print(rH(v)); wH(v,30);print(rH(v)+5);
        IStmt ex8 = new CompStmt(new VarDecl("v", new RefType(new IntType())),
                new CompStmt(new HeapAllocation("v", new ValueExp(new IntValue(20))),
                        new CompStmt(new PrintStmt(new HeapReading(new VarExp("v"))),
                                new CompStmt(new HeapWriting("v", new ValueExp(new IntValue(30))),
                                        new PrintStmt(new ArithExp('+',
                                                new HeapReading(new VarExp("v")),
                                                new ValueExp(new IntValue(5))))))));

        // Ref int v;new(v,20);Ref Ref int a; new(a,v); new(v,30);print(rH(rH(a)));
        IStmt ex9 = new CompStmt(new VarDecl("v", new RefType(new IntType())),
                new CompStmt(new HeapAllocation("v", new ValueExp(new IntValue(20))),
                        new CompStmt(new VarDecl("a", new RefType(new RefType(new IntType()))),
                                new CompStmt(new HeapAllocation("a", new VarExp("v")),
                                        new CompStmt(new HeapAllocation("v", new ValueExp(new IntValue(30))),
                                                new PrintStmt(new HeapReading(new HeapReading(new VarExp("a")))))))));

        // int v; Ref int a; v=10;new(a,22);fork(wH(a,30);v=32;print(v);print(rH(a)));print(v);print(rH(a))
        IStmt ex10= new CompStmt(new VarDecl("v", new IntType()),
                new CompStmt(new VarDecl("a", new RefType(new IntType())),
                        new CompStmt(new AssignStmt("v", new ValueExp(new IntValue(10))),
                                new CompStmt(new HeapAllocation("a", new ValueExp(new IntValue(22))),
                                        new CompStmt(new ForkStmt(new CompStmt(new HeapWriting("a", new ValueExp(new IntValue(30))),
                                                new CompStmt(new AssignStmt("v", new ValueExp(new IntValue(32))),
                                                        new CompStmt(new PrintStmt(new VarExp("v")),
                                                                new PrintStmt(new HeapReading(new VarExp("a"))))))),
                                                new CompStmt(new PrintStmt(new VarExp("v")),
                                                        new PrintStmt(new HeapReading(new VarExp("a")))))))));


        TextMenu menu= new TextMenu();
        menu.addCommand(new ExitCommand("0","exit"));

        IStack<IStmt> exestack = new MyStack<IStmt>();
        exestack.push(ex1);
        IDict<String, IValue> symTable = new MyDict<String, IValue>();
        IList<IValue> out = new MyList<IValue>();
        IDict<StringValue, BufferedReader> ft=new MyDict<StringValue, BufferedReader>();
        IHeap<Integer,IValue>h=new Heap<Integer,IValue>();
        try{
            IDict<String, IType> typeEnv1= new MyDict<String, IType>();
            ex1.typecheck(typeEnv1);
            PrgState prg = new PrgState(exestack, symTable, out, ex1,ft,h);
            IRepo repo1=new Repo("log1.txt");
            repo1.add_program(prg);
            Controller ctr1=new Controller(repo1);
            menu.addCommand(new RunExample("1", ex1.toString(),ctr1));
        }
        catch (myExceptions e){
            System.out.println(e.getMessage());
            System.exit(1);
        }

        IStack<IStmt> exestack1 = new MyStack<IStmt>();
        exestack1.push(ex2);
        IDict<String, IValue> symTable1 = new MyDict<String, IValue>();
        IList<IValue> out1 = new MyList<IValue>();
        IDict<StringValue, BufferedReader> ft1=new MyDict<StringValue, BufferedReader>();
        IHeap<Integer,IValue>h1=new Heap<Integer,IValue>();
        try{
            IDict<String, IType> typeEnv2= new MyDict<String, IType>();
            ex2.typecheck(typeEnv2);
            PrgState prg1 = new PrgState(exestack1, symTable1, out1, ex2,ft1,h1);
            IRepo repo2=new Repo("log2.txt");
            repo2.add_program(prg1);
            Controller ctr2=new Controller(repo2);
            menu.addCommand(new RunExample("2", ex2.toString(), ctr2));
        }
        catch (myExceptions e){
            System.out.println(e.getMessage());
            System.exit(1);
        }


        IStack<IStmt> exestack2 = new MyStack<IStmt>();
        exestack2.push(ex3);
        IDict<String, IValue> symTable2 = new MyDict<String, IValue>();
        IList<IValue> out2 = new MyList<IValue>();
        IDict<StringValue, BufferedReader> ft2=new MyDict<StringValue, BufferedReader>();
        IHeap<Integer,IValue>h2=new Heap<Integer,IValue>();
        try{
        IDict<String, IType> typeEnv3= new MyDict<String, IType>();
        ex3.typecheck(typeEnv3);
            PrgState prg2 = new PrgState(exestack2, symTable2, out2, ex3,ft2,h2);
            IRepo repo3=new Repo("log3.txt");
            repo3.add_program(prg2);
            Controller ctr3=new Controller(repo3);
            menu.addCommand(new RunExample("3", ex3.toString(), ctr3));
        }
        catch (myExceptions e){
            System.out.println(e.getMessage());
            System.exit(1);
        }




        IStack<IStmt> exestack3 = new MyStack<IStmt>();
        exestack3.push(ex4);
        IDict<String, IValue> symTable3 = new MyDict<String, IValue>();
        IList<IValue> out3 = new MyList<IValue>();
        IDict<StringValue, BufferedReader>ft3=new MyDict<StringValue, BufferedReader>();
        IHeap<Integer,IValue>h3=new Heap<Integer,IValue>();
        try{
            IDict<String, IType> typeEnv4= new MyDict<String, IType>();
            ex4.typecheck(typeEnv4);
            PrgState prg3 = new PrgState(exestack3, symTable3, out3, ex4,ft3,h3);
            IRepo repo4=new Repo("log4.txt");
            repo4.add_program(prg3);
            Controller ctr4=new Controller(repo4);
            menu.addCommand(new RunExample("4", ex4.toString(), ctr4));
        }
        catch (myExceptions e){
            System.out.println(e.getMessage());
            System.exit(1);
        }


        IStack<IStmt> exestack4 = new MyStack<IStmt>();
        exestack4.push(ex5);
        IDict<String, IValue> symTable4 = new MyDict<String, IValue>();
        IList<IValue> out4 = new MyList<IValue>();
        IDict<StringValue, BufferedReader>ft4=new MyDict<StringValue, BufferedReader>();
        IHeap<Integer,IValue>h4=new Heap<Integer,IValue>();
        try{
            IDict<String, IType> typeEnv5= new MyDict<String, IType>();
            ex5.typecheck(typeEnv5);
            PrgState prg4 = new PrgState(exestack4, symTable4, out4, ex5,ft4,h4);
            IRepo repo5=new Repo("log5.txt");
            repo5.add_program(prg4);
            Controller ctr5=new Controller(repo5);
            menu.addCommand(new RunExample("5", ex5.toString(), ctr5));
        }
        catch (myExceptions e){
            System.out.println(e.getMessage());
            System.exit(1);
        }


        IStack<IStmt> exestack5 = new MyStack<IStmt>();
        exestack5.push(ex6);
        IDict<String, IValue> symTable5 = new MyDict<String, IValue>();
        IList<IValue> out5 = new MyList<IValue>();
        IDict<StringValue, BufferedReader>ft5=new MyDict<StringValue, BufferedReader>();
        IHeap<Integer,IValue>h5=new Heap<Integer,IValue>();
        try{
            IDict<String, IType> typeEnv6= new MyDict<String, IType>();
            ex6.typecheck(typeEnv6);
            PrgState prg5 = new PrgState(exestack5, symTable5, out5, ex6,ft5,h5);
            IRepo repo6=new Repo("log6.txt");
            repo6.add_program(prg5);
            Controller ctr6=new Controller(repo6);
            menu.addCommand(new RunExample("6", ex6.toString(), ctr6));
        }
        catch (myExceptions e){
            System.out.println(e.getMessage());
            System.exit(1);
        }




        IStack<IStmt> exestack6 = new MyStack<IStmt>();
        exestack6.push(ex7);
        IDict<String, IValue> symTable6 = new MyDict<String, IValue>();
        IList<IValue> out6 = new MyList<IValue>();
        IDict<StringValue, BufferedReader>ft6=new MyDict<StringValue, BufferedReader>();
        IHeap<Integer,IValue>h6=new Heap<Integer,IValue>();
        try{
            IDict<String, IType> typeEnv7= new MyDict<String, IType>();
            ex7.typecheck(typeEnv7);
            PrgState prg6 = new PrgState(exestack6, symTable6, out6, ex7,ft6,h6);
            IRepo repo7=new Repo("log7.txt");
            repo7.add_program(prg6);
            Controller ctr7=new Controller(repo7);
            menu.addCommand(new RunExample("7", ex7.toString(), ctr7));
        }
        catch (myExceptions e){
            System.out.println(e.getMessage());
            System.exit(1);
        }


        IStack<IStmt> exestack7 = new MyStack<IStmt>();
        exestack7.push(ex8);
        IDict<String, IValue> symTable7 = new MyDict<String, IValue>();
        IList<IValue> out7 = new MyList<IValue>();
        IDict<StringValue, BufferedReader>ft7=new MyDict<StringValue, BufferedReader>();
        IHeap<Integer,IValue>h7=new Heap<Integer,IValue>();
        try{
            IDict<String, IType> typeEnv8= new MyDict<String, IType>();
            ex8.typecheck(typeEnv8); PrgState prg7 = new PrgState(exestack7, symTable7, out7, ex8,ft7,h7);
            IRepo repo8=new Repo("log8.txt");
            repo8.add_program(prg7);
            Controller ctr8=new Controller(repo8);
            menu.addCommand(new RunExample("8", ex8.toString(), ctr8));

        }
        catch (myExceptions e){
            System.out.println(e.getMessage());
            System.exit(1);
        }


        IStack<IStmt> exestack8 = new MyStack<IStmt>();
        exestack8.push(ex9);
        IDict<String, IValue> symTable8 = new MyDict<String, IValue>();
        IList<IValue> out8 = new MyList<IValue>();
        IDict<StringValue, BufferedReader>ft8=new MyDict<StringValue, BufferedReader>();
        IHeap<Integer,IValue>h8=new Heap<Integer,IValue>();
        try{
            IDict<String, IType> typeEnv9= new MyDict<String, IType>();
            ex9.typecheck(typeEnv9);
            PrgState prg8 = new PrgState(exestack8, symTable8, out8, ex9,ft8,h8);
            IRepo repo9=new Repo("log9.txt");
            repo9.add_program(prg8);
            Controller ctr9=new Controller(repo9);
            menu.addCommand(new RunExample("9", ex9.toString(), ctr9));

        }
        catch (myExceptions e){
            System.out.println(e.getMessage());
            System.exit(1);
        }


        IStack<IStmt> exestack9 = new MyStack<IStmt>();
        exestack9.push(ex10);
        IDict<String, IValue> symTable9 = new MyDict<String, IValue>();
        IList<IValue> out9 = new MyList<IValue>();
        IDict<StringValue, BufferedReader>ft9=new MyDict<StringValue, BufferedReader>();
        IHeap<Integer,IValue>h9=new Heap<Integer,IValue>();
        try{
            IDict<String, IType> typeEnv10= new MyDict<String, IType>();
            ex10.typecheck(typeEnv10);
            PrgState prg9 = new PrgState(exestack9, symTable9, out9, ex10,ft9,h9);
            IRepo repo10=new Repo("log10.txt");
            repo10.add_program(prg9);
            Controller ctr10=new Controller(repo10);

            menu.addCommand(new RunExample("10", ex10.toString(), ctr10));
        }
        catch (myExceptions e){
            System.out.println(e.getMessage());
            System.exit(1);
        }



        menu.show();

    }
}
