module gui {
    requires javafx.controls;
    requires javafx.fxml;


    exports gui;
    opens gui to javafx.fxml;
}