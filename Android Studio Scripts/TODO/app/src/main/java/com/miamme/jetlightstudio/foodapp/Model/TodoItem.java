package com.miamme.jetlightstudio.foodapp.Model;

public class TodoItem {

    int id;
    String taskName;
    boolean status;
    String color;

    public TodoItem(int id, String taskName, boolean status, String color) {
        this.id = id;
        this.taskName = taskName;
        this.status = status;
        this.color = color;
    }

    //region getters and setters
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getTaskName() {
        return taskName;
    }

    public void setTaskName(String taskName) {
        this.taskName = taskName;
    }

    public boolean isStatus() {
        return status;
    }

    public void setStatus(boolean status) {
        this.status = status;
    }

    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
    //endregion
}
