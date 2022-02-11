package gui;

import Model.expression.*;
import Model.statement.*;
import Model.type.BoolType;
import Model.type.IntType;
import Model.type.RefType;
import Model.type.StringType;
import Model.value.BoolValue;
import Model.value.IntValue;
import Model.value.StringValue;

public class Examples {
    public static IStmt[] getExamples() {
        // ex 1:  int v; v = 2; Print(v)
        IStmt ex1 = new CompStmt(new VarDecl("v", new IntType()),
                new CompStmt(new AssignStmt("v", new ValueExp(new IntValue(2))),
                        new PrintStmt(new VarExp("v"))));
        // ex 2: int a;int b; a=2+3*5;b=a+1;Print(b)
        IStmt ex2 = new CompStmt(new VarDecl("a", new IntType()), new CompStmt(new VarDecl("b", new BoolType()),
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

        return new IStmt[]{ex1, ex2, ex3, ex4, ex5, ex6, ex7, ex8, ex9, ex9,ex10};
    }
}
