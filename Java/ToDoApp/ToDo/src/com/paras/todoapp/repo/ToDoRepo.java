package com.paras.todoapp.repo;

import com.paras.todoapp.dto.ToDoDTO;
import com.paras.todoapp.utils.Constants;

import java.io.*;
import java.util.ArrayList;
import java.util.Scanner;

public class ToDoRepo implements IToDoRepo {
    private File file;
    private static ToDoRepo toDoRepo;

    private ToDoRepo() throws IOException {
        file = new File(Constants.PATH);
        file.createNewFile();
    }

    public static ToDoRepo getInstance() throws IOException {
        if (toDoRepo == null) {
            toDoRepo = new ToDoRepo();
        }
        return toDoRepo;


    }

    @Override
    public boolean addTask(ArrayList<ToDoDTO> tasks) throws IOException {
        FileOutputStream fo = null;
        ObjectOutputStream os = null;
        try {
            fo = new FileOutputStream(file);
            os = new ObjectOutputStream(fo);
            os.writeObject(tasks);
        } finally {
            if (os != null) os.close();
            if (fo != null) fo.close();
        }
        return true;
    }

    @Override
    public ArrayList<ToDoDTO> printTask() throws IOException, ClassNotFoundException {
        ArrayList<ToDoDTO> list = new ArrayList<>();
        try (FileInputStream fs = new FileInputStream(file)) {
            try (ObjectInputStream os = new ObjectInputStream(fs)) {
                list = (ArrayList<ToDoDTO>) os.readObject();

            }
            return list;
        }
    }

    @Override
    public ToDoDTO deleteTask(String name) throws IOException, ClassNotFoundException {
        ArrayList<ToDoDTO> list = printTask();
        for (int i = 0; i < list.size(); i++) {
            if (list.get(i).getName().equals(name)) {
                ToDoDTO x = list.get(i);
                list.remove(i);
                addTask(list);
                return x;
            }
        }


        return null;


    }

    public boolean updateTask(int id) throws IOException, ClassNotFoundException {
        ArrayList<ToDoDTO> list = printTask();
        try {
            list.get(id - 1).setStatus(Constants.COMPLETE);

            addTask(list);
            return true;
        } catch (Exception e) {
            System.out.println("Task ID not found");
        }
        return false;
    }
    public ToDoDTO searchTask(String name) throws IOException, ClassNotFoundException {
        ArrayList<ToDoDTO> list = printTask();
        for(ToDoDTO task : list){
            if (task.getName().equals(name)){
                return task;
            }
        }
        return null;
    }
}
