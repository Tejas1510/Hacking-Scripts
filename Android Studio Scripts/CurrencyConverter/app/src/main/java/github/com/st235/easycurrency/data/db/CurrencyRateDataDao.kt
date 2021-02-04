package github.com.st235.easycurrency.data.db

import androidx.annotation.WorkerThread
import androidx.room.Dao
import androidx.room.Insert
import androidx.room.OnConflictStrategy
import androidx.room.Query

@Dao
interface CurrencyRateDataDao {
    @WorkerThread
    @Query("SELECT * FROM rates")
    fun getAll(): List<CurrencyRateEntity>

    @WorkerThread
    @Insert(onConflict = OnConflictStrategy.REPLACE)
    fun insertAll(rates: List<CurrencyRateEntity>)
}
