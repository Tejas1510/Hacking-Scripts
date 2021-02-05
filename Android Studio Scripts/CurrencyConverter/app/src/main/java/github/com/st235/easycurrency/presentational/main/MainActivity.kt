package github.com.st235.easycurrency.presentational.main

import android.os.Bundle
import android.view.View
import android.widget.ProgressBar
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import androidx.swiperefreshlayout.widget.SwipeRefreshLayout
import github.com.st235.easycurrency.R
import github.com.st235.easycurrency.domain.Currency
import github.com.st235.easycurrency.presentational.base.BaseActivity
import github.com.st235.easycurrency.utils.KeyboardHelper
import github.com.st235.easycurrency.utils.SnackBarFactory
import github.com.st235.easycurrency.utils.SnackBarHelper
import github.com.st235.easycurrency.utils.events.CurrencyListScrollListener
import github.com.st235.easycurrency.utils.events.OnItemClickListener
import github.com.st235.easycurrency.utils.events.OnItemValueChangedListener
import org.koin.android.ext.android.inject

class MainActivity : BaseActivity(), MainView {
    private val presenter: MainPresenter by inject()
    private val adapter: CurrencyAdapter by inject()
    private val snackBarFactory: SnackBarFactory by inject()

    private val onItemValueChangedListener = object:
        OnItemValueChangedListener<Double, Currency> {
        override fun onItemValueChanged(value: Double, item: Currency, position: Int) {
            presenter.onTypeValue(value, item)
        }
    }

    private val onItemClickListener = object: OnItemClickListener<Currency> {
        override fun onItemClick(item: Currency, position: Int) {
            presenter.onClickCurrency(item)
        }
    }

    private val onScrollToTopListener = {
        currenciesRecyclerView.scrollToPosition(0)
    }

    private val swipeToRefreshListener = {
        presenter.onSwipeToRefresh()
    }

    private lateinit var keyboardHelper: KeyboardHelper
    private lateinit var snackBarHelper: SnackBarHelper
    private lateinit var currenciesProgressBar: ProgressBar
    private lateinit var currenciesRecyclerView: RecyclerView
    private lateinit var currenciesSwipeRefreshLayout: SwipeRefreshLayout

    override fun getLayout() = R.layout.activity_main

    override fun onInitViews() {
        keyboardHelper = KeyboardHelper(this)
        snackBarHelper = SnackBarHelper(this, snackBarFactory)
        currenciesRecyclerView = findViewById(R.id.currenciesList)
        currenciesProgressBar = findViewById(R.id.currenciesProgressBar)
        currenciesSwipeRefreshLayout = findViewById(R.id.currenciesSwipeContainer)

        currenciesSwipeRefreshLayout.setProgressBackgroundColorSchemeResource(
                R.color.swipeRefreshBackground
        )
        currenciesSwipeRefreshLayout.setColorSchemeResources(
                R.color.swipeRefreshProgressOne,
                R.color.swipeRefreshProgressTwo,
                R.color.swipeRefreshProgressThree
        )
        currenciesSwipeRefreshLayout.setOnRefreshListener(swipeToRefreshListener)

        adapter.itemClickListener = onItemClickListener
        adapter.onScrollToTopListener = onScrollToTopListener
        adapter.valueChangedListener = onItemValueChangedListener

        currenciesRecyclerView.setHasFixedSize(true)
        currenciesRecyclerView.addOnScrollListener(CurrencyListScrollListener(keyboardHelper, adapter))
        currenciesRecyclerView.layoutManager = LinearLayoutManager(this)
        currenciesRecyclerView.adapter = adapter
    }

    override fun onViewsInitialized(savedInstanceState: Bundle?) {
        presenter.attachView(this)
    }

    override fun showRatesExpiredDialogIfNeeded(hoursDelta: Int,
                                                isExpired: Boolean) {
        snackBarHelper.showDialogIfNeeded(hoursDelta, isExpired)
    }

    override fun updateCurrenciesData(currencies: List<Currency>) {
        if (currenciesProgressBar.isShown) {
            currenciesProgressBar.visibility = View.GONE
        }

        if (currenciesSwipeRefreshLayout.isRefreshing) {
            currenciesSwipeRefreshLayout.isRefreshing = false
        }

        adapter.onCurrenciesUpdated(currencies)
    }

    override fun onDestroy() {
        presenter.detachView()
        super.onDestroy()
    }


}
