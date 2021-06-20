package com.paras.todoapp.view;
import com.paras.todoapp.dto.ToDoDTO;
import com.paras.todoapp.repo.IToDoRepo;
import com.paras.todoapp.repo.ToDoRepo;

import java.io.EOFException;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;

import static com.paras.todoapp.utils.MessageReader.*;
import static com.paras.todoapp.utils.Constants.*;
public class ToDoView {
    private static Scanner scanner = new Scanner(System.in);
    private static void addTask(){
        scanner.nextLine();
        System.out.println(getValue("input.taskname"));
         String name = scanner.nextLine();

        System.out.println(getValue("input.taskdesc"));
        String desc = scanner.nextLine();
        ToDoDTO todo = new ToDoDTO(name,desc);
        String result = null;
        try {
        IToDoRepo repo = ToDoRepo.getInstance();

        ArrayList<ToDoDTO> tasks = null;

            try{
             tasks = repo.printTask();}
            catch (EOFException e){

            }
            if(tasks!=null){
                tasks.add(todo);
            }else{

//                System.out.println("File is empty add a new record");
                tasks = new ArrayList<>();
                tasks.add(todo);
            }
            result =  repo.addTask(tasks)?getValue("record.added"):getValue("record.notadded");
        } catch (Exception e) {
            e.printStackTrace();
        }
        System.out.println(result);
    }
    static void printAllTask(){
        System.out.println("Tasks:");
        try {
        ToDoRepo repo = ToDoRepo.getInstance();

            ArrayList<ToDoDTO> tasks = repo.printTask();
            for(ToDoDTO task : tasks){
                System.out.println(task );
            }
        } catch (IOException e) {
            e.printStackTrace();
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }
    }
    static void deleteTask(){
        try{
            ToDoRepo repo = ToDoRepo.getInstance();
            System.out.println(getValue("input.taskname"));
            String name = scanner.nextLine();
            ToDoDTO task = repo.deleteTask(name);
            if(task!=null){
                System.out.println(task +"\n removed");
            }else{
                System.out.println("Task not found");
            }
        }catch (IOException e) {
            e.printStackTrace();
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }

    }
    static void updateTask(){
        try{
            ToDoRepo repo = ToDoRepo.getInstance();
            System.out.println(getValue("input.taskid"));
            int id = scanner.nextInt();
            System.out.println(repo.updateTask(id)?"Task "+ id +" updated successfully":"");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    static void searchTask(){
        try{
            ToDoRepo repo = ToDoRepo.getInstance();
            System.out.println(getValue("input.taskname"));
            String name = scanner.nextLine();
            ToDoDTO task = repo.searchTask(name);
            if(task!=null){
                System.out.println(task);
            }else {
                System.out.println("Task not in the list");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    public static void main(String[] args) {

        outer:
        while (true){
        System.out.println(getValue("addtask"));
        System.out.println(getValue("deletetask"));
        System.out.println(getValue("updatetask"));
        System.out.println(getValue("searchtask"));
        System.out.println(getValue("printtask"));
        System.out.println(getValue("exittask"));
        System.out.println(getValue("choice"));
        int choice = scanner.nextInt();
        switch (choice){
            case ADD_TASK:
                addTask();
                break;
            case DELETE_TASK:
                scanner.nextLine();
                deleteTask();
                break;
            case UPDATE_TASK:
                scanner.nextLine();
                updateTask();
                break;
            case SEARCH_TASK:
                scanner.nextLine();
                searchTask();
                break;
            case PRINT_TASK: printAllTask();
                break;
            case EXIT:
                break outer;

        }

    }
        scanner.close();

}
}
