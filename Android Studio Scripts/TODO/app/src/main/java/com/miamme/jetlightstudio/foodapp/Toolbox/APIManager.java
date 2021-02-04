package com.miamme.jetlightstudio.foodapp.Toolbox;

import android.content.Context;
import android.net.ConnectivityManager;
import android.net.NetworkInfo;
import android.os.AsyncTask;
import android.util.Log;

import com.miamme.jetlightstudio.foodapp.Model.TodoItem;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedOutputStream;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.ProtocolException;
import java.net.URL;
import java.util.ArrayList;

public class APIManager extends AsyncTask<String, Void, String> {
    String data = "";

    @Override
    protected String doInBackground(String... strings) {
        data = "";
        if (strings[0].matches("GET")) {
            Log.e("operation", "sending GET");
            GETTodoItems(strings[1], strings[2]);
        } else if (strings[0].matches("POST")) {
            Log.e("operation", "sending POST");
            POSTTodoItem(strings[1], strings[2], strings[3]);
        } else if (strings[0].matches("PUT")) {
            Log.e("operation", "sending PUT");
            PUTTodoItem(strings[1], strings[2], strings[3]);
        } else if (strings[0].matches("DELETE")) {
            Log.e("operation", "sending DELETE");
            DELETETodoItem(strings[1], strings[2], strings[3]);
        }
        return data;
    }

    @Override
    protected void onPostExecute(String s) {
        super.onPostExecute(s);
    }

    public ArrayList<TodoItem> getTodoItemsList(String data) {
        ArrayList<TodoItem> todoItems = new ArrayList<>();
        try {
            JSONArray jsonArray = new JSONArray(data);
            for (int i = 0; i < jsonArray.length(); i++) {
                JSONObject json = (JSONObject) jsonArray.get(i);
                todoItems.add(new TodoItem(json.getInt("id"), json.getString("task"), json.getBoolean("status"), json.getString("color")));
            }
        } catch (JSONException e) {
            e.printStackTrace();
        }
        return todoItems;
    }

    public static boolean isNetworkAvailable(Context context) {
        ConnectivityManager connectivityManager = (ConnectivityManager) context.getSystemService(Context.CONNECTIVITY_SERVICE);
        NetworkInfo activeNetworkInfo = connectivityManager.getActiveNetworkInfo();
        return activeNetworkInfo != null && activeNetworkInfo.isConnected();
    }

    void GETTodoItems(String path, String endpoint) {
        try {
            URL url = new URL(path + endpoint);
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            InputStream inputStream = connection.getInputStream();
            BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(inputStream));
            String s = "";
            while (s != null) {
                s = bufferedReader.readLine();
                if (s != null && data != null) data = data.concat(s);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    void POSTTodoItem(String path, String endpoint, String data) {

        try {
            URL obj = new URL(path + endpoint);
            HttpURLConnection con = (HttpURLConnection) obj.openConnection();
            con.setRequestMethod("POST");
            con.setRequestProperty("Content-Type", "application/json");
            con.setDoOutput(true);
            OutputStream os = con.getOutputStream();
            BufferedWriter writer = new BufferedWriter(
                    new OutputStreamWriter(os, "UTF-8"));
            Log.e("Result", "Post data:" + data);
            writer.write(data);
            writer.flush();
            writer.close();
            os.close();
            int responseCode = con.getResponseCode();
            Log.e("Result", "Post Response Code :: " + responseCode);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    void PUTTodoItem(String path, String endpoint, String data) {

        try {
            URL obj = new URL(path + endpoint);
            HttpURLConnection con = (HttpURLConnection) obj.openConnection();
            con.setRequestMethod("PUT");
            con.setRequestProperty("Content-Type", "application/json");
            con.setDoOutput(true);
            OutputStream os = con.getOutputStream();
            BufferedWriter writer = new BufferedWriter(
                    new OutputStreamWriter(os, "UTF-8"));
            Log.e("Result", "PUT data:" + data);
            writer.write(data);
            writer.flush();
            writer.close();
            os.close();
            int responseCode = con.getResponseCode();
            Log.e("Result", "Put Response Code :: " + responseCode);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    void DELETETodoItem(String path, String endpoint, String data) {

        try {
            URL obj = new URL(path + endpoint);
            HttpURLConnection con = (HttpURLConnection) obj.openConnection();
            con.setRequestMethod("DELETE");
            con.setRequestProperty("Content-Type", "application/json");
            con.setDoOutput(true);
            OutputStream os = con.getOutputStream();
            BufferedWriter writer = new BufferedWriter(
                    new OutputStreamWriter(os, "UTF-8"));
            Log.e("Result", "DELETE data:" + data);
            writer.write(data);
            writer.flush();
            writer.close();
            os.close();
            int responseCode = con.getResponseCode();
            Log.e("Result", "Delete Response Code :: " + responseCode);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static JSONObject itemToJSON(int id, boolean status, String taskName, String taskColor) {
        JSONObject json = new JSONObject();
        try {
            json.put("id", id);
            json.put("status", status);
            json.put("task", taskName);
            json.put("color", taskColor);
        } catch (JSONException e) {
            e.printStackTrace();
        }
        return json;
    }
}
