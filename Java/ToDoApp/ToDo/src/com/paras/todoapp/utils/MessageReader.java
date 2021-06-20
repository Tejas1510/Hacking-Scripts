package com.paras.todoapp.utils;
import java.util.ResourceBundle;


public interface MessageReader {
    ResourceBundle rb = ResourceBundle.getBundle(Constants.MSSG_FILE);
    public static String getValue(String key){
        return rb.getString(key);
    }
}
