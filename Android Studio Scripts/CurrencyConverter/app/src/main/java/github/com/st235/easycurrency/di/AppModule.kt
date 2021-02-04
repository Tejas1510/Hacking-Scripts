package github.com.st235.easycurrency.di

import androidx.lifecycle.ProcessLifecycleOwner
import github.com.st235.easycurrency.BuildConfig
import github.com.st235.easycurrency.data.CurrencyRateRepository
import github.com.st235.easycurrency.data.CurrencyRateStorageHelper
import github.com.st235.easycurrency.data.db.CurrencyRateDatabase
import github.com.st235.easycurrency.data.db.RoomDatabaseFactory
import github.com.st235.easycurrency.data.inmemory.CurrencyRateInMemoryModel
import github.com.st235.easycurrency.data.net.CurrencyRateApi
import github.com.st235.easycurrency.data.net.CurrencyRateApiWrapper
import github.com.st235.easycurrency.data.net.RetrofitFactory
import github.com.st235.easycurrency.data.prefs.CurrencyRatePrefs
import github.com.st235.easycurrency.domain.CurrenciesListHolderWrapper
import github.com.st235.easycurrency.domain.CurrencyListHolder
import github.com.st235.easycurrency.presentational.main.CurrencyAdapter
import github.com.st235.easycurrency.presentational.main.MainPresenter
import github.com.st235.easycurrency.utils.NetworkStateDispatcher
import github.com.st235.easycurrency.utils.SnackBarFactory
import github.com.st235.easycurrency.utils.UpdateTimer
import org.koin.android.ext.koin.androidContext
import org.koin.dsl.module.module

private val mainModule = module {
    /**
     * net stage
     */
    single { RetrofitFactory.createApiWrapper<CurrencyRateApi>(BuildConfig.CURRENCIES_RATES_BASE_URL) }
    single { CurrencyRateApiWrapper(get()) }

    /**
     * database stage
     */
    single { RoomDatabaseFactory.create<CurrencyRateDatabase>(androidContext()) }

    /**
     * prefs stage
     */
    single { CurrencyRatePrefs(androidContext()) }

    /**
     * data layer stage
     */
    single { CurrencyRateInMemoryModel(get()) }
    single { CurrencyRateStorageHelper(get(), get()) }
    single { CurrencyRateRepository(get(), get(), get(), get(), get()) }

    /**
     * utils stage
     */
    single { UpdateTimer() }
    single { NetworkStateDispatcher(androidContext(), get()) }
    single { ProcessLifecycleOwner.get().lifecycle }
    single { SnackBarFactory(androidContext()) }

    /**
     * domain stage
     */
    single { CurrenciesListHolderWrapper(get(), get(), get()) } bind CurrencyListHolder::class

    /**
     * presentation stage
     */
    single { MainPresenter(get()) }
    single { CurrencyAdapter() }
}

val appModules = listOf(mainModule)
