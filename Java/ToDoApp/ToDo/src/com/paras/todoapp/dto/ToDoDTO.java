package com.paras.todoapp.dto;

import com.paras.todoapp.utils.Constants;

import java.io.Serializable;
import java.util.Date;

public class ToDoDTO implements Serializable {
    static int i=1;
    private String name;
    private String dec;
    private Date date;
    private String status;

    private ToDoDTO(){
        date = new Date();
        status = Constants.PENDING;
    }

    public ToDoDTO(String name, String dec) {
        this();
        this.name = name;
        this.dec = dec;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getDec() {
        return dec;
    }

    public void setDec(String dec) {
        this.dec = dec;
    }

    public Date getDate() {
        return date;
    }

    public void setDate(Date date) {
        this.date = date;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    @Override
    public String toString() {
        return
                "Title = " + name + '\'' +
                ", Description ='" + dec + '\'' +
                ", Date=" + date +
                ", Status='" + status + '\'' +
                '}';
    }
}
