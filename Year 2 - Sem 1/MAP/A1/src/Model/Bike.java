package Model;

public class Bike implements IVehicle{
    private String color;

    public Bike(String _color){
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
        return "Bike [ Color  = "+color+" ]";
    }
}
