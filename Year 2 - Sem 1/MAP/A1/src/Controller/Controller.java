package Controller;

import Model.IVehicle;
import Repo.IRepo;

public class Controller {
    private IRepo repo;
    public Controller(IRepo _repo){
        this.repo=_repo;
    }
    public void add_vehicle_controller(IVehicle v) throws Exception{
        repo.add_vehicle(v);

    }
    public void delete_vehicle_controller(int pos) throws Exception{
        repo.delete_vehicle(pos);

    }

    public IVehicle[] filter_by_color_controller(){
        return repo.filter_by_color();
    }

    public IVehicle[] get_all_controller(){

        return repo.get_all();
    }
}
