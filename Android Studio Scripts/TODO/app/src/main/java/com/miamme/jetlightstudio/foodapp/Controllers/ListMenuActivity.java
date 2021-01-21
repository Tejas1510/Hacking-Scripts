package com.miamme.jetlightstudio.foodapp.Controllers;

import android.content.Intent;
import android.graphics.drawable.Drawable;
import android.support.v4.content.ContextCompat;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.ImageButton;
import android.widget.ListView;
import android.widget.RelativeLayout;
import android.widget.TextView;

import com.miamme.jetlightstudio.foodapp.Model.TodoList;
import com.miamme.jetlightstudio.foodapp.R;

import java.util.ArrayList;

public class ListMenuActivity extends AppCompatActivity {
    ListView listView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_list_menu);
        listView = (ListView) findViewById(R.id.listMenu);
        ArrayList<TodoList> lists = new ArrayList<>();
        lists.add(new TodoList("Home", "blue"));
        lists.add(new TodoList("Work", "green"));
        lists.add(new TodoList("School", "violet"));
        CustumAdapter custumAdapter = new CustumAdapter(lists);
        listView.setAdapter(custumAdapter);
    }

    public class CustumAdapter extends BaseAdapter {
        ArrayList<TodoList> lists;

        public CustumAdapter(ArrayList lists) {
            this.lists = lists;
        }

        @Override
        public int getCount() {
            return lists.size();
        }

        @Override
        public Object getItem(int i) {
            return null;
        }

        @Override
        public long getItemId(int i) {
            return i;
        }

        @Override
        public View getView(int i, View view, ViewGroup viewGroup) {
            view = getLayoutInflater().inflate(R.layout.task_menu_item, null);

            //region setting background color
            RelativeLayout layout = view.findViewById(R.id.itemBackground);
            final String color = lists.get(i).getColor();
            if (color.matches("blue"))
                layout.setBackground(ContextCompat.getDrawable(getApplicationContext(), R.drawable.list_item_background_blue));
            else if (color.matches("green"))
                layout.setBackground(ContextCompat.getDrawable(getApplicationContext(), R.drawable.list_item_background_green));
            else
                layout.setBackground(ContextCompat.getDrawable(getApplicationContext(), R.drawable.list_item_background_violet));
            //endregion

            final TextView title = view.findViewById(R.id.listName);
            title.setText(lists.get(i).getName());
            ImageButton button = view.findViewById(R.id.selectList);
            button.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    listSelected(title.getText().toString(), color);
                }
            });

            return view;
        }

        void listSelected(String listName, String listColor) {
            Intent intent = new Intent(getApplicationContext(), ToDoListActivity.class);
            intent.putExtra("listName", listName);
            intent.putExtra("listColor", listColor);
            startActivity(intent);
        }
    }
}
