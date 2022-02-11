package gui;

import Controller.Controller;
import Exceptions.myExceptions;
import Model.PrgState;
import Model.adt.MyDict;
import Model.statement.IStmt;
import Repo.IRepo;
import Repo.Repo;
import javafx.collections.FXCollections;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Alert;
import javafx.scene.control.Button;
import javafx.scene.control.ButtonType;
import javafx.scene.control.ListView;
import javafx.scene.layout.Region;

import java.net.URL;
import java.util.ResourceBundle;

import static gui.Examples.getExamples;


public class ListController implements Initializable {

    private ProgramController programController;
    @FXML
    private Button displayButton;
    @FXML
    private ListView<IStmt> statements;

    public ListController(){}


    public void setProgramController(ProgramController pg){
        this.programController=pg;
    }

    @FXML
    public void initialize(URL url, ResourceBundle resourceBundle) {
        statements.setItems(FXCollections.observableArrayList(getExamples()));
        displayButton.setOnAction(actionEvent -> {
                int index= statements.getSelectionModel().getSelectedIndex();
                if(index<0) return;

                IStmt stmt = getExamples()[index];
                PrgState prgState = new PrgState(stmt);
                IRepo repository = new Repo(String.format("log%s.txt", index+1));
                repository.add_program(prgState);
                Controller controller = new Controller(repository);
                try {
                    stmt.typecheck(new MyDict<>());
                    programController.setController(controller);
                } catch (myExceptions e) {
                    Alert alert = new Alert(Alert.AlertType.ERROR, e.getMessage(), ButtonType.OK);
                    alert.getDialogPane().setMinHeight(Region.USE_PREF_SIZE);
                    alert.showAndWait();
                    }
                }

                );
    }
}
