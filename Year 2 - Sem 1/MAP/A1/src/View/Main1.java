/*
1. Intr-o parcare exista masini, motociclete
si biciclete. Sa se afiseze toate vehiculele
de culoare rosie.
 */

package View;

import Controller.Controller;
import Model.Bike;
import Model.Car;
import Model.IVehicle;
import Model.Motor;
import Repo.Repo;

import java.util.Scanner;

public class Main1 {
    public static void main(String[] args){
        Repo repo=new Repo(100);
        Controller ctrl=new Controller(repo);
        menu(ctrl);
    }
    private static void menu(Controller ctrl){
        while(true)
        {   System.out.println("1. Add a car");
            System.out.println("2. Add a bike");
            System.out.println("3. Add a motor");
            System.out.println("4. Delete a vehicle");
            System.out.println("5. Filter by color");
            System.out.println("6. Print all vehicles");
            System.out.println("0. Exit");

            System.out.println("Choose an option >> ");
            Scanner scanner=new Scanner(System.in);
            String cmd=scanner.nextLine();

            if(cmd.equals("0")){
                break;

            }
            else
            {
                switch (cmd) {

                    case "1":
                        try {
                            String color;
                            System.out.println("Specify the color: ");
                            color = scanner.nextLine();

                            IVehicle v = new Car(color);
                            ctrl.add_vehicle_controller(v);


                        } catch (Exception e) {
                            System.out.println(e.getMessage());
                        }
                        break;
                    case "2":
                        try {
                            String color;
                            System.out.println("Specify the color: ");
                            color = scanner.nextLine();

                            IVehicle v = new Bike(color);
                            ctrl.add_vehicle_controller(v);

                        } catch (Exception e) {
                            System.out.println(e.getMessage());
                        }
                        break;
                    case "3":
                        try {
                            String color;
                            System.out.println("Specify the color: ");
                            color = scanner.nextLine();
                            try{
                                IVehicle v = new Motor(color);
                                ctrl.add_vehicle_controller(v);
                            }catch (Exception e) {
                                System.out.println(e.getMessage());}



                        } catch (Exception e) {
                            System.out.println(e.getMessage());
                        }
                        break;
                    case "4":
                        try {
                            System.out.print("Specify position: ");
                            int pos = Integer.parseInt(scanner.nextLine());
                            try {
                                ctrl.delete_vehicle_controller(pos);
                            } catch (Exception e) {
                                System.out.println(e.getMessage());
                                System.out.println();
                            }


                        } catch (Exception e) {
                            System.out.println(e.getMessage());
                        }
                        break;
                    case "5":
                        IVehicle[] filtered = ctrl.filter_by_color_controller();
                        for (IVehicle v : filtered) {
                            if(v!=null)
                                System.out.println(v.toString());

                        }
                        System.out.println();
                        break;
                    case "6":
                        for (IVehicle v : ctrl.get_all_controller()) {
                            if(v!=null)
                                System.out.println(v.toString());
                        }
                        System.out.println();
                        break;
                    default:
                        System.out.println("Wrong input\n");
                        break;
                }

            }





            }


        }
    }


