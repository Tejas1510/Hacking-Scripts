package com.miamme.jetlightstudio.foodapp.Toolbox;

import android.content.Context;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

/**
 * Created by oussama on 22/02/2018.
 */

public class SQLiteManager extends SQLiteOpenHelper {

    private static final int dbVersion = 1;
    private static final String dbName = "task.db";
    public static String dbTableName = "task";
    public static final String dbColumnId = "id";
    public static final String dbColumnStatus = "status";
    public static final String dbColumnName = "taskName";
    public static final String dbColumnColor = "color";

    public SQLiteManager(Context context) {
        super(context, dbName, null, dbVersion);
    }

    @Override
    public void onCreate(SQLiteDatabase sqLiteDatabase) {
        String query = "Create Table IF NOT EXISTS " + dbTableName +
                " ("
                + dbColumnId + " Integer, "
                + dbColumnStatus + " Boolean, "
                + dbColumnName + " Text, "
                + dbColumnColor + " Text "
                + ");";


        sqLiteDatabase.execSQL(query);
    }

    @Override
    public void onUpgrade(SQLiteDatabase sqLiteDatabase, int i, int i1) {
        sqLiteDatabase.execSQL("DROP TABLE IF EXISTS " + dbTableName);
        onCreate(sqLiteDatabase);
    }
}
