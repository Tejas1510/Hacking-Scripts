package github.com.st235.easycurrency.domain

import androidx.lifecycle.Lifecycle
import androidx.lifecycle.LifecycleObserver
import androidx.lifecycle.OnLifecycleEvent
import github.com.st235.easycurrency.data.CurrencyRateRepository
import github.com.st235.easycurrency.data.net.CurrencyRateResponse
import github.com.st235.easycurrency.utils.NetworkStateDispatcher
import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.launch
import timber.log.Timber

/**
 * Holds currencies list and switches between
 * offline and online strategies when its needed
 */
class CurrenciesListHolderWrapper(private val currencyRateRepository: CurrencyRateRepository,
                                  private val networkStateDispatcher: NetworkStateDispatcher,
                                  applicationLifecycle: Lifecycle): CurrencyListHolder(), LifecycleObserver {
    private var currentListHolder: CurrencyListHolder

    private val currenciesObserver = this::notifyObservers
    private val updateCurrenciesObserver = this::onUpdateCurrencies

    private val networkChangeObserver = { state: Boolean ->
        changeHolders(state)
    }

    init {
        currentListHolder = createNewHolder(networkStateDispatcher.isOnline())
        applicationLifecycle.addObserver(this)
    }

    @OnLifecycleEvent(Lifecycle.Event.ON_RESUME)
    fun registerCallbacks() {
        networkStateDispatcher.addObserver(networkChangeObserver)
        currentListHolder.addObserver(currenciesObserver)
        currencyRateRepository.addObserver(updateCurrenciesObserver)
    }

    @OnLifecycleEvent(Lifecycle.Event.ON_PAUSE)
    fun unregisterCallbacks() {
        networkStateDispatcher.removeObserver(networkChangeObserver)
        currentListHolder.removeObserver(currenciesObserver)
        currencyRateRepository.removeObserver(updateCurrenciesObserver)
    }

    override fun updateCurrencies() {
        currencyRateRepository.update()
    }

    override fun onUpdateCurrencies(response: CurrencyRateResponse) {
        Timber.tag(TAG).v("Update currencies ${response.unixTimestamp}")
        currentListHolder.onUpdateCurrencies(response)
    }

    override fun onChangeBaseCurrency(newCurrency: Currency) {
        GlobalScope.launch {
            currencyRateRepository.changeBaseCurrency(newCurrency.id)
        }
        currentListHolder.onChangeBaseCurrency(newCurrency)
    }

    override fun onTypedNewValue(newBaseValue: Double) {
        currentListHolder.onTypedNewValue(newBaseValue)
    }

    private fun createNewHolder(isOnline: Boolean): CurrencyListHolder {
        if (isOnline) {
            Timber.tag(TAG).v("Created online list observer")
            return OnlineListHolder()
        }

        Timber.tag(TAG).v("Created offline list observer")
        return OfflineListHolder()
    }

    private fun changeHolders(isOnline: Boolean) {
        currentListHolder.removeObserver(currenciesObserver)
        currentListHolder = createNewHolder(isOnline)
        currentListHolder.addObserver(currenciesObserver)
    }
}
