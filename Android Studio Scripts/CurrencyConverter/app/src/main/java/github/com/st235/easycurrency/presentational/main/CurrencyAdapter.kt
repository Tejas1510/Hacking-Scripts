package github.com.st235.easycurrency.presentational.main

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.DiffUtil
import androidx.recyclerview.widget.RecyclerView
import github.com.st235.easycurrency.R
import github.com.st235.easycurrency.components.CurrencyEditText
import github.com.st235.easycurrency.domain.Currency
import github.com.st235.easycurrency.utils.events.CurrencyTextWatcher
import github.com.st235.easycurrency.utils.CurrencyUtils
import github.com.st235.easycurrency.utils.events.OnItemClickListener
import github.com.st235.easycurrency.utils.events.OnItemValueChangedListener
import github.com.st235.easycurrency.utils.events.ScrollableAdapter
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext
import timber.log.Timber

typealias OnScrollToTopListener = () -> Unit

class CurrencyAdapter
    : RecyclerView.Adapter<CurrencyAdapter.CurrenciesViewHolder>(),
    ScrollableAdapter {
    private companion object {
        private const val TAG = "[CurrencyAdapter]"

        private const val NO_POSITION = -1

        private const val BASE = 0
        private const val ORDINARY = 1
    }

    private var currentlyFocusedItem = NO_POSITION
    private var currencies: List<Currency> = emptyList()

    override var isScrolling = false
    private var needToBeScrolled = false

    var itemClickListener: OnItemClickListener<Currency>? = null
    var valueChangedListener: OnItemValueChangedListener<Double, Currency>? = null
    var onScrollToTopListener: OnScrollToTopListener? = null

    inner class CurrenciesViewHolder(itemView: View): RecyclerView.ViewHolder(itemView) {
        private val currencyItemRoot: View = itemView.findViewById(R.id.currencyItemRoot)
        private val currencyValue: CurrencyEditText = itemView.findViewById(R.id.currencyInputValue)
        private val currencyCode: TextView = itemView.findViewById(R.id.currencyIsoCode)
        private val currencyTitle: TextView = itemView.findViewById(R.id.currencyTitle)
        private val currencyAvatar: TextView = itemView.findViewById(R.id.currencyAvatar)

        private val onFocusChangeListener = View.OnFocusChangeListener { _, hasFocus ->
            val adapterPosition = adapterPosition
            if (hasFocus) {
                currentlyFocusedItem = adapterPosition
            }
        }

        private val onTextWatcher: CurrencyTextWatcher = object: CurrencyTextWatcher() {
            override fun onValueChanged(newValue: Double) {
                val position = adapterPosition
                valueChangedListener?.onItemValueChanged(newValue,
                        currencies[position], position)
            }
        }

        init {
            currencyItemRoot.setOnClickListener {
                needToBeScrolled = true
                val position = adapterPosition
                itemClickListener?.onItemClick(currencies[position], position)
            }

            currencyValue.onFocusChangeListener = onFocusChangeListener
        }

        fun bind(currency: Currency) {
            currencyValue.removeTextWatcher(onTextWatcher)

            currencyValue.changeInputText(CurrencyUtils.getCurrencyOutputText(currency.value))
            currencyValue.setSign(CurrencyUtils.getCurrencySignBy(currency.id))
            currencyCode.text = currency.id
            currencyTitle.text = currency.title
            currencyAvatar.text = CurrencyUtils.getCurrencyFlagEmojiBy(currency.id)

            currencyValue.addTextWatcher(onTextWatcher)
        }

        fun bindWithPayload(value: Double) {
            currencyValue.removeTextWatcher(onTextWatcher)
            currencyValue.changeInputText(CurrencyUtils.getCurrencyOutputText(value))
            currencyValue.addTextWatcher(onTextWatcher)
        }
    }

    fun onCurrenciesUpdated(newCurrencies: List<Currency>) {
        if (isScrolling) {
            Timber.tag(TAG).v("Not updated")
            return
        }

        onNewCurrencies(newCurrencies)
    }

    private fun onNewCurrencies(newCurrencies: List<Currency>) {
        GlobalScope.launch {
            val diffUtilsCallback = CurrencyDiffUtilsCallback(currencies, newCurrencies)
            val diffUtilsResult = DiffUtil.calculateDiff(diffUtilsCallback, true)
            withContext(Dispatchers.Main) {
                diffUtilsResult.dispatchUpdatesTo(this@CurrencyAdapter)
                currencies = newCurrencies
                if (needToBeScrolled) {
                    needToBeScrolled = false
                    onScrollToTopListener?.invoke()
                }
            }
        }
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): CurrenciesViewHolder {
        val context = parent.context
        val layoutId = if (viewType == BASE) R.layout.item_base_currency else R.layout.item_ordinary_currency
        val view = LayoutInflater.from(context).inflate(layoutId, parent, false)
        return CurrenciesViewHolder(view)
    }

    override fun onBindViewHolder(holder: CurrenciesViewHolder, position: Int) {
        holder.bind(currencies[position])
    }

    override fun onBindViewHolder(holder: CurrenciesViewHolder, position: Int, payloads: MutableList<Any>) {
        if (payloads.isEmpty()) {
            onBindViewHolder(holder, position)
            return
        }

        if (position == currentlyFocusedItem) {
            return
        }

        val newValue = payloads[0] as Double
        holder.bindWithPayload(newValue)
    }

    override fun getItemViewType(position: Int) = if (currencies[position].isBase) BASE else ORDINARY

    override fun getItemCount() = currencies.size
}
