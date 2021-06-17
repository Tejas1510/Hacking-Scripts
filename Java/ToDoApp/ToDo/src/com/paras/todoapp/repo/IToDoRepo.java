package com.paras.todoapp.repo;

import com.paras.todoapp.dto.ToDoDTO;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.ArrayList;

public interface IToDoRepo {
    public boolean addTask(ArrayList<ToDoDTO> todo) throws IOException;
    ArrayList<ToDoDTO> printTask() throws IOException, ClassNotFoundException;
    ToDoDTO deleteTask(String name) throws IOException, ClassNotFoundException;
    boolean updateTask(int id) throws IOException, ClassNotFoundException;
    ToDoDTO searchTask(String name) throws IOException, ClassNotFoundException;
}