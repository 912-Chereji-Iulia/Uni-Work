package Repo;

import Model.IVehicle;

public interface IRepo {
    void add_vehicle(IVehicle v) throws Exception;
    void delete_vehicle(int pos) throws Exception;
    public IVehicle[] filter_by_color();
    IVehicle[] get_all();

}
