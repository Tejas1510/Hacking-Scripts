package github.com.st235.easycurrency.background

import android.content.Context
import androidx.annotation.WorkerThread
import androidx.work.Worker
import androidx.work.WorkerParameters
import github.com.st235.easycurrency.BuildConfig
import github.com.st235.easycurrency.data.BASE_TO_BASE_CONVERT_RATIO
import github.com.st235.easycurrency.data.CurrencyRateStorageHelper
import github.com.st235.easycurrency.data.net.CurrencyRateApiWrapper
import github.com.st235.easycurrency.data.prefs.CurrencyRatePrefs
import github.com.st235.easycurrency.utils.debug.ThreadUtils
import kotlinx.coroutines.runBlocking
import org.koin.standalone.KoinComponent
import org.koin.standalone.inject
import timber.log.Timber

/**
 * Background task to update currencies rates
 */
class BackgroundUpdateWorker(context: Context,
                             params: WorkerParameters):
    Worker(context, params), KoinComponent {
    companion object {
        private const val TAG = "[BackgroundWorker]"
    }

    private val prefs: CurrencyRatePrefs by inject()
    private val apiWrapper: CurrencyRateApiWrapper by inject()
    private val storageHelper: CurrencyRateStorageHelper by inject()

    @WorkerThread
    override fun doWork(): Result {
        ThreadUtils.assertOnBackgroundThread()

        var result = Result.failure()
        Timber.d("background task: start periodic task")

        if (apiWrapper.isInUsage()) {
            Timber.tag(TAG).v("rate api is in usage")
            return Result.success()
        }

        runBlocking {
            try {
                val appId = BuildConfig.CURRENCIES_RATES_APP_ID
                val response = apiWrapper.getRates(appId, prefs.baseCurrency).await()
                response.rates[response.base] = BASE_TO_BASE_CONVERT_RATIO
                storageHelper.write(response)
                result = Result.success()
                Timber.d("background task: update finished")
            } catch (throwable: Throwable) {
                Timber.w(throwable, "background task: failed with an exception")
            }
        }

        return result
    }
}
