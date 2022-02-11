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
import Model.value.BoolValue;
import Model.value.IValue;
import Model.value.IntValue;
import Repo.Repo;

import java.util.Scanner;

public class MainProgram {
    static Repo repo = new Repo();
    static Controller controller = new Controller(repo);
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


        System.out.println("1. Program 1.");
        System.out.println("2. Program 2.");
        System.out.println("3. Program 3.");
        System.out.println("0. Exit");

        boolean done = false;
        while(!done){
            System.out.println("Enter a command: ");
            Scanner ob = new Scanner(System.in);
            int cmd = ob.nextInt();
            switch (cmd){
                case 0:
                    done=true;
                    break;
                case 1:
                    IStack<IStmt> exestack = new MyStack<IStmt>();
                    exestack.push(ex1);
                    IDict<String, IValue> symTable = new MyDict<String, IValue>();
                    IList<IValue> out = new MyList<IValue>();
                    PrgState prg = new PrgState(exestack, symTable, out, ex1);
                    try {
                        controller.add_program(prg);
                        controller.allStep();
                    }catch (Exception e)
                    {
                        System.out.println(e.getMessage());
                    }
                    break;
                case 2:
                    IStack<IStmt> exestack1 = new MyStack<IStmt>();
                    exestack1.push(ex2);
                    IDict<String, IValue> symTable1 = new MyDict<String, IValue>();
                    IList<IValue> out1 = new MyList<IValue>();
                    PrgState prg1 = new PrgState(exestack1, symTable1, out1, ex2);
                    try {
                        controller.add_program(prg1);
                        controller.allStep();
                    }
                    catch (Exception e){
                        System.out.println(e.getMessage());
                    }
                    break;
                case 3:
                    IStack<IStmt> exestack2 = new MyStack<IStmt>();
                    exestack2.push(ex3);
                    IDict<String, IValue> symTable2 = new MyDict<String, IValue>();
                    IList<IValue> out2 = new MyList<IValue>();
                    PrgState prg2 = new PrgState(exestack2, symTable2, out2, ex3);
                    try {
                        controller.add_program(prg2);
                        controller.allStep();
                    }catch (Exception e){
                        System.out.println(e.getMessage());
                    }
                    break;
                default:
                    System.out.println("wrong command");
                    break;

            }
        }
    }
}
