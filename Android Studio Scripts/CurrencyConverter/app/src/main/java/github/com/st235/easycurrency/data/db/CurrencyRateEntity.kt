package github.com.st235.easycurrency.data.db

import androidx.room.ColumnInfo
import androidx.room.Entity
import androidx.room.Index
import androidx.room.PrimaryKey

@Entity(tableName = "rates", indices = [Index(value = ["currency"], unique = true)])
data class CurrencyRateEntity(
    @PrimaryKey(autoGenerate = true) var id: Long? = null,
    @ColumnInfo(name = "currency") var currency: String,
    @ColumnInfo(name = "rate") var rate: Double
)
