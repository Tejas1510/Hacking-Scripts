package github.com.st235.easycurrency.data

import androidx.annotation.WorkerThread
import github.com.st235.easycurrency.data.db.CurrencyRateDatabase
import github.com.st235.easycurrency.data.db.CurrencyRateEntity
import github.com.st235.easycurrency.data.net.CurrencyRateResponse
import github.com.st235.easycurrency.data.net.RatesMap
import github.com.st235.easycurrency.data.prefs.CurrencyRatePrefs
import github.com.st235.easycurrency.utils.debug.ThreadUtils
import timber.log.Timber

/**
 * Helps convert data from network models to
 * database internal models and vice versa.
 * Also, helps to read/write data
 * from different sources to create entire model
 */
class CurrencyRateStorageHelper(private val database: CurrencyRateDatabase,
                                private val prefs: CurrencyRatePrefs) {
    companion object {
        private const val TAG = "[RateStorageHelper]"
    }

    @WorkerThread
    fun read(): CurrencyRateResponse? {
        Timber.tag(TAG).v("Reading values from storage")
        ThreadUtils.assertOnBackgroundThread()

        val rates = readDb()
        if (rates.isEmpty()) {
            return null
        }

        val base = prefs.baseCurrency
        val unixTimestamp = prefs.updateDate

        return CurrencyRateResponse.createWithTimestamp(base, "", rates, unixTimestamp)
    }

    @WorkerThread
    private fun readDb(): RatesMap {
        ThreadUtils.assertOnBackgroundThread()

        val rates = mutableMapOf<String, Double>()
        val dbRates = database.ratesDataDao().getAll()

        for (dbRate in dbRates) {
            rates[dbRate.currency] = dbRate.rate
        }

        return rates
    }

    @WorkerThread
    fun write(ratesResponse: CurrencyRateResponse) {
        Timber.tag(TAG).v("Writing values to storage")
        ThreadUtils.assertOnBackgroundThread()
        writeToDb(ratesResponse)
        writePrefs(ratesResponse)
    }

    @WorkerThread
    private fun writeToDb(ratesResponse: CurrencyRateResponse) {
        ThreadUtils.assertOnBackgroundThread()
        Timber.tag(TAG).d("Perform to update database")

        val dbRatesEntities = mutableListOf<CurrencyRateEntity>()
        for (currencyRatePair in ratesResponse.rates) {
            dbRatesEntities.add(
                CurrencyRateEntity(
                    currency = currencyRatePair.key,
                    rate = currencyRatePair.value
                )
            )
        }
        database.ratesDataDao().insertAll(dbRatesEntities)
    }

    @WorkerThread
    private fun writePrefs(ratesResponse: CurrencyRateResponse) {
        ThreadUtils.assertOnBackgroundThread()
        Timber.tag(TAG).d("Perform to update prefs")
        prefs.updateDate = ratesResponse.unixTimestamp
    }
}
