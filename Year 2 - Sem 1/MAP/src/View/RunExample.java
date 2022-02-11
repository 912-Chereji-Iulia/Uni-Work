package View;

import Controller.Controller;

public class RunExample extends Command{
    private Controller ctr;
    public RunExample(String key, String description, Controller c) {
        super(key, description);
        this.ctr=c;
    }

    @Override
    public void execute() {
        try{
            ctr.allStep();
        }
        catch (Exception e){
            System.out.println(e.getMessage());
        }

    }
}
