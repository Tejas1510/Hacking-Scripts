package github.com.st235.easycurrency.domain

import androidx.annotation.WorkerThread
import github.com.st235.easycurrency.data.net.CurrencyRateResponse
import github.com.st235.easycurrency.utils.ObservableModel

typealias CurrenciesList = Pair<Long, List<Currency>>

/**
 * Interface which presenter communicate with database or network
 * We should not think about the data source and performed operations
 * only about the commands we could send and data we can observe
 */
abstract class CurrencyListHolder: ObservableModel<CurrenciesList>() {
    companion object {
        const val TAG = "[CurrencyListHolder]"
    }

    protected lateinit var baseCurrency: Currency
    protected val currencies: MutableList<Currency> = mutableListOf()

    /**
     * Should be performed only from data sources and only
     * in a background thread.
     */
    @WorkerThread
    abstract fun onUpdateCurrencies(response: CurrencyRateResponse)

    /**
     * Allows to clients change base currency
     * Note: Client should call this operation when interacts with data model
     */
    abstract fun onChangeBaseCurrency(newCurrency: Currency)

    /**
     * Allows to clients change base value to recalculate all the values
     * Note: Client should call this operation when interacts with data model
     */
    abstract fun onTypedNewValue(newBaseValue: Double)

    open fun updateCurrencies() {
    }

    protected fun getCurrencies(time: Long): CurrenciesList {
        return time to currencies.map { i -> i }
    }
}
