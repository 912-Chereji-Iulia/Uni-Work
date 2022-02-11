package gui;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.net.URL;


public class main extends Application {

    @Override
    public void start(Stage stage) throws Exception {

        URL location=getClass().getResource("listc.fxml");
        FXMLLoader listLoader=new FXMLLoader(location);
        stage.setTitle("Select a program!");
        Parent listWindow=listLoader.load();
        ListController listcontroller=listLoader.getController();
        stage.setScene(new Scene(listWindow));


        FXMLLoader programLoader=new FXMLLoader();
        programLoader.setLocation(getClass().getResource("program.fxml"));
        Parent programWindow =programLoader.load();
        ProgramController programController=programLoader.getController();

        listcontroller.setProgramController(programController);
        Stage secondStage=new Stage();
        secondStage.setTitle("Interpreter");
        Scene programScene=new Scene(programWindow);
        secondStage.setScene(programScene);

        secondStage.show();
        stage.show();

    }
    public static void main(String args[]){
        launch(args);
    }
}
