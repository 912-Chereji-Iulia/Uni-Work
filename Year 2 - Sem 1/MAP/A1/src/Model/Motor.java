package Model;

public class Motor implements IVehicle{

    private final String color;

    public Motor(String _color){
        color=_color;
    }
    @Override
    public boolean is_red(String color) {
        return color.equals("red");
    }

    @Override
    public String get_color() {
        return color;
    }

    @Override
    public String toString(){
        return "Motor [ Color  = "+color+" ]";
    }
}
