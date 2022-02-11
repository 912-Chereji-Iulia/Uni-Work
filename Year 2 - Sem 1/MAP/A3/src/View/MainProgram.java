package View;

import Controller.Controller;

import Exceptions.myExceptions;
import Model.PrgState;
import Model.adt.*;

import Model.expression.ArithExp;
import Model.expression.ValueExp;
import Model.expression.VarExp;
import Model.statement.*;
import Model.type.BoolType;
import Model.type.IntType;
import Model.type.StringType;
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
                new IntType()), new CompStmt(new AssignStmt("a", new ValueExp(new BoolValue(true))),
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

        IStack<IStmt> exestack = new MyStack<IStmt>();
        exestack.push(ex1);
        IDict<String, IValue> symTable = new MyDict<String, IValue>();
        IList<IValue> out = new MyList<IValue>();
        IDict<StringValue, BufferedReader> ft=new MyDict<StringValue, BufferedReader>();
        PrgState prg = new PrgState(exestack, symTable, out, ex1,ft);
        IRepo repo1=new Repo("log1.txt");
        repo1.add_program(prg);
        Controller ctr1=new Controller(repo1);


        IStack<IStmt> exestack1 = new MyStack<IStmt>();
        exestack1.push(ex2);
        IDict<String, IValue> symTable1 = new MyDict<String, IValue>();
        IList<IValue> out1 = new MyList<IValue>();
        IDict<StringValue, BufferedReader> ft1=new MyDict<StringValue, BufferedReader>();
        PrgState prg1 = new PrgState(exestack1, symTable1, out1, ex2,ft1);
        IRepo repo2=new Repo("log2.txt");
        repo2.add_program(prg1);
        Controller ctr2=new Controller(repo2);

        IStack<IStmt> exestack2 = new MyStack<IStmt>();
        exestack2.push(ex3);
        IDict<String, IValue> symTable2 = new MyDict<String, IValue>();
        IList<IValue> out2 = new MyList<IValue>();
        IDict<StringValue, BufferedReader> ft2=new MyDict<StringValue, BufferedReader>();
        PrgState prg2 = new PrgState(exestack2, symTable2, out2, ex3,ft2);
        IRepo repo3=new Repo("log3.txt");
        repo3.add_program(prg2);
        Controller ctr3=new Controller(repo3);

        IStack<IStmt> exestack3 = new MyStack<IStmt>();
        exestack3.push(ex4);
        IDict<String, IValue> symTable3 = new MyDict<String, IValue>();
        IList<IValue> out3 = new MyList<IValue>();
        IDict<StringValue, BufferedReader>ft3=new MyDict<StringValue, BufferedReader>();
        PrgState prg3 = new PrgState(exestack3, symTable3, out3, ex4,ft3);
        IRepo repo4=new Repo("log4.txt");
        repo4.add_program(prg3);
        Controller ctr4=new Controller(repo4);

        TextMenu menu= new TextMenu();
        menu.addCommand(new ExitCommand("0","exit"));
        menu.addCommand(new RunExample("1", ex1.toString(),ctr1));
        menu.addCommand(new RunExample("2", ex2.toString(), ctr2));
        menu.addCommand(new RunExample("3", ex3.toString(), ctr3));
        menu.addCommand(new RunExample("4", ex4.toString(), ctr4));
        menu.show();

    }
}
