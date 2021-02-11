package github.com.st235.easycurrency.presentational.main

import github.com.st235.easycurrency.domain.CurrenciesList
import github.com.st235.easycurrency.domain.Currency
import github.com.st235.easycurrency.domain.CurrencyListHolder
import github.com.st235.easycurrency.presentational.base.BasePresenter
import github.com.st235.easycurrency.utils.CurrencyUtils
import github.com.st235.easycurrency.utils.Observer
import github.com.st235.easycurrency.utils.TimeUtils

class
MainPresenter(private val currenciesHolder: CurrencyListHolder): BasePresenter<MainView>() {

    private val currenciesChangeObserver: Observer<CurrenciesList>
            = { currencies: CurrenciesList ->
        val hoursLeftBehind = TimeUtils.getHours(currencies.first)
        view?.showRatesExpiredDialogIfNeeded(hoursLeftBehind, TimeUtils.isTimestampExpired(currencies.first))
        view?.updateCurrenciesData(currencies.second)
    }

    override fun onAttachView(v: MainView) {
        super.onAttachView(v)
        currenciesHolder.addObserver(currenciesChangeObserver)
    }

    fun onTypeValue(newValue: Double, currency: Currency) {
        currenciesHolder.onTypedNewValue(CurrencyUtils.calculateBaseValue(newValue, currency))
    }

    fun onClickCurrency(newBaseCurrency: Currency) {
        currenciesHolder.onChangeBaseCurrency(newBaseCurrency)
    }

    fun onSwipeToRefresh() {
        currenciesHolder.updateCurrencies()
    }

    override fun onDetachView(v: MainView?) {
        currenciesHolder.removeObserver(currenciesChangeObserver)
        super.onDetachView(v)
    }
}
