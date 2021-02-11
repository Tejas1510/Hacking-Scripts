package github.com.st235.easycurrency.data.db

import androidx.room.Database
import androidx.room.RoomDatabase
import github.com.st235.easycurrency.BuildConfig

@Database(entities = [CurrencyRateEntity::class], version = BuildConfig.DATABASE_VERSION)
abstract class CurrencyRateDatabase: RoomDatabase() {
    abstract fun ratesDataDao(): CurrencyRateDataDao
}
