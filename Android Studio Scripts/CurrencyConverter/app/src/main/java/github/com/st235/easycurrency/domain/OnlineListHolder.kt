package github.com.st235.easycurrency.domain

import androidx.annotation.WorkerThread
import github.com.st235.easycurrency.data.net.CurrencyRateResponse
import github.com.st235.easycurrency.utils.CurrencyUtils
import github.com.st235.easycurrency.utils.debug.ThreadUtils
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext
import timber.log.Timber

/**
 * Online strategy to maintain currencies list
 */
open class OnlineListHolder: CurrencyListHolder() {
    private var updateTimestamp: Long = 0L

    override fun onUpdateCurrencies(response: CurrencyRateResponse) {
        updateTimestamp = response.unixTimestamp

        ThreadUtils.assertOnBackgroundThread()
        if (currencies.isEmpty()) {
            createCurrencies(response)
        } else {
            updateCurrencies(response)
        }

        GlobalScope.launch(context = Dispatchers.Main) {
            notifyObservers(getCurrencies(updateTimestamp))
        }
    }

    override fun onChangeBaseCurrency(newCurrency: Currency) {
        GlobalScope.launch {
            changeBaseCurrencyInternal(newCurrency)
        }
    }

    override fun onTypedNewValue(newBaseValue: Double) {
        //TODO(st235): to think about synchronization
        GlobalScope.launch {
            baseCurrency.value = newBaseValue
            updateCurrenciesValues()
            withContext(context = Dispatchers.Main) {
                notifyObservers(getCurrencies(updateTimestamp))
            }
        }
    }

    @Synchronized
    private fun changeBaseCurrencyInternal(newCurrency: Currency) {
        baseCurrency = newCurrency
        currencies[0].isBase = false
        currencies.find { it.id == newCurrency.id }?.isBase = true
        sortCurrencies()
    }

    @WorkerThread
    private fun createCurrencies(response: CurrencyRateResponse) {
        baseCurrency = Currency(response.base, CurrencyUtils.getCurrencyTitleBy(response.base), true)

        for (entry in response.rates) {
            val isBase = entry.key == response.base

            if (isBase) {
                currencies.add(baseCurrency)
                continue
            }

            val currencyForEntry = Currency(entry.key, CurrencyUtils.getCurrencyTitleBy(entry.key), isBase)
            currencyForEntry.rate = entry.value
            currencies.add(currencyForEntry)
        }

        updateCurrenciesValues()
        sortCurrencies()
    }

    @WorkerThread
    private fun updateCurrencies(response: CurrencyRateResponse) {
        if (response.base != baseCurrency.id) {
            Timber.tag(TAG).w("Update was dropped cause base currency is different")
            return
        }

        for (i in 0 until currencies.size) {
            val currency = currencies[i]
            val newRate = response.rates[currency.id]!!
            currencies[i] = Currency.copy(currency, newRate, newRate * baseCurrency.value)
        }
    }

    @WorkerThread
    protected fun updateCurrenciesValues() {
        for (i in 0 until currencies.size) {
            val currency = currencies[i]
            currencies[i] = Currency.copyWithNewValue(currency, baseCurrency.value * currency.rate)
        }
    }

    @Synchronized
    protected fun sortCurrencies() {
        currencies.sortWith(compareBy({ !it.isBase }, { it.title }))
    }
}
