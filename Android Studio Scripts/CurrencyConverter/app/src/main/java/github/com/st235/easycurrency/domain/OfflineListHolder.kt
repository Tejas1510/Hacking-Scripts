package github.com.st235.easycurrency.domain

import androidx.annotation.WorkerThread
import github.com.st235.easycurrency.utils.CurrencyUtils
import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.launch

/**
 * Offline strategy to maintain currencies,
 * because we have not abile to switch base currency rates,
 * cause we have not internet connection
 */
class OfflineListHolder: OnlineListHolder() {
    override fun onChangeBaseCurrency(newCurrency: Currency) {
        GlobalScope.launch {
            changeBaseCurrencyInternal(newCurrency)
        }
    }

    /**
     * We should not update real [baseCurrency], because we have not
     * another one mapping for that, so we should use existing one
     */
    @Synchronized
    @WorkerThread
    private fun changeBaseCurrencyInternal(newCurrency: Currency) {
        val oldBaseValue = currencies[0]
        val newBaseValue = currencies.find { it.id == newCurrency.id } ?: return

        oldBaseValue.isBase = false
        newBaseValue.isBase = true

        baseCurrency.value = CurrencyUtils.calculateBaseValue(newCurrency.value, newCurrency)

        updateCurrenciesValues()
        sortCurrencies()
    }
}
