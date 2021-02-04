package github.com.st235.easycurrency.presentational.main

import github.com.st235.easycurrency.domain.Currency

interface MainView {
    fun updateCurrenciesData(currencies: List<Currency>)
    fun showRatesExpiredDialogIfNeeded(hoursDelta: Int, isExpired: Boolean)
}
