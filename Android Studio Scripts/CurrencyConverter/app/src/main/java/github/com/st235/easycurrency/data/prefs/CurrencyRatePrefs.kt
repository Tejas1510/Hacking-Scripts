package github.com.st235.easycurrency.data.prefs

import android.content.Context
import androidx.annotation.WorkerThread
import github.com.st235.easycurrency.utils.debug.ThreadUtils

private const val APP_PREFS = "currency_rate.prefs"
private const val BASE_CURRENCY_VALUE = "base_currency"
private const val UPDATE_DATA_VALUE = "update_data"

@WorkerThread
class CurrencyRatePrefs(context: Context) {

    private val sharedPrefs = context.getSharedPreferences(APP_PREFS, Context.MODE_PRIVATE)

    var baseCurrency: String
    get() {
        ThreadUtils.assertOnBackgroundThread()
        return sharedPrefs.getString(BASE_CURRENCY_VALUE, "EUR")!!
    }
    set(value) {
        ThreadUtils.assertOnBackgroundThread()
        with(sharedPrefs.edit()) {
            putString(BASE_CURRENCY_VALUE, value)
            apply()
        }
    }

    var updateDate: Long
    get() {
        ThreadUtils.assertOnBackgroundThread()
        return sharedPrefs.getLong(UPDATE_DATA_VALUE, 0L)
    }
    set(value) {
        ThreadUtils.assertOnBackgroundThread()
        with(sharedPrefs.edit()) {
            putLong(UPDATE_DATA_VALUE, value)
            apply()
        }
    }
}
