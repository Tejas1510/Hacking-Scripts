package github.com.st235.easycurrency.data.db

import android.content.Context
import androidx.room.Room
import androidx.room.RoomDatabase
import github.com.st235.easycurrency.BuildConfig

object RoomDatabaseFactory {
    inline fun<reified T: RoomDatabase> create(context: Context): T = Room.databaseBuilder(
        context.applicationContext, T::class.java, BuildConfig.DATABASE_NAME
    ).build()
}
