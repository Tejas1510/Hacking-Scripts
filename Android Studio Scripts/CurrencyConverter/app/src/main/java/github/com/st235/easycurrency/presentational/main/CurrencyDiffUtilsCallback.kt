package github.com.st235.easycurrency.presentational.main

import androidx.annotation.WorkerThread
import androidx.recyclerview.widget.DiffUtil
import github.com.st235.easycurrency.domain.Currency
import github.com.st235.easycurrency.utils.CurrencyUtils

@WorkerThread
class CurrencyDiffUtilsCallback(
        private val oldCurrenciesList: List<Currency>,
        private val newCurrenciesList: List<Currency>
): DiffUtil.Callback() {
    override fun areItemsTheSame(oldItemPosition: Int, newItemPosition: Int): Boolean {
        return oldCurrenciesList[oldItemPosition].id ==
                newCurrenciesList[newItemPosition].id
    }

    override fun areContentsTheSame(oldItemPosition: Int, newItemPosition: Int): Boolean {
        val oldCurrency = oldCurrenciesList[oldItemPosition]
        val newCurrency = newCurrenciesList[newItemPosition]

        return CurrencyUtils.getCurrencyOutputText(oldCurrency.value) ==
                CurrencyUtils.getCurrencyOutputText(newCurrency.value)
    }

    override fun getChangePayload(oldItemPosition: Int, newItemPosition: Int): Any? {
        return newCurrenciesList[newItemPosition].value
    }

    override fun getOldListSize() = oldCurrenciesList.size

    override fun getNewListSize() = newCurrenciesList.size
}
