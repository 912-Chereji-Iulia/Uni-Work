package Repo;

import Model.IVehicle;

public class Repo implements IRepo{

    private int size;
    private IVehicle[] vehicles;
    private int current_index;


    public Repo(int size){
        this.size=size;
        this.vehicles=new IVehicle[size];
        this.current_index=0;
    }

    @Override
    public void add_vehicle(IVehicle v)  throws Exception {
        if (this.current_index>=this.size)
            throw new Exception("Array is full! Maximum size is "+ this.size);
        char[] chars= v.get_color().toCharArray();
        for(char c:chars)
            if(Character.isDigit(c))
                throw new Exception("Invalid color");

        vehicles[current_index]=v;
        current_index++;

    }

    @Override
    public void delete_vehicle(int pos) throws Exception {
        if(this.current_index<=0)
            throw new Exception("Nothing to remove");
        if(pos<0 || this.current_index-1<pos)
            throw new Exception("Wrong index");
        this.vehicles[pos]=null;
        this.current_index--;

    }

    @Override
    public IVehicle[] filter_by_color() {
        IVehicle[] result=new IVehicle[this.current_index];
        int nr=0;
        for(int i=0;i<this.current_index;i++){
            if(this.vehicles[i]!=null && this.vehicles[i].is_red(this.vehicles[i].get_color())){
                result[nr++]=this.vehicles[i];
            }
        }
        return result;
    }


    @Override
    public IVehicle[] get_all() {
        return this.vehicles;
    }
}
