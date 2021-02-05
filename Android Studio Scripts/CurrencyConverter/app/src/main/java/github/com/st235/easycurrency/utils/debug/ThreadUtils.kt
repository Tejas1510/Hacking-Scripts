package github.com.st235.easycurrency.utils.debug

import android.os.Looper
import androidx.annotation.AnyThread
import androidx.annotation.MainThread
import androidx.annotation.WorkerThread
import github.com.st235.easycurrency.BuildConfig
import timber.log.Timber

/**
 * Helps with thread detection and possible
 * long operation prevention on main and background thread
 * Not fires in production code, but still fires in debug
 */
object ThreadUtils {
    /**
     * Checks that operation should be performed on main thread
     *
     * @throws IllegalStateException if current thread is not main
     */
    @MainThread
    fun assertOnMainThread() {
        assertThat(
            Looper.getMainLooper().thread == Thread.currentThread(),
            "Does not on main thread! Thread: ${Thread.currentThread().name}"
        )
        Timber.v("Thread name: ${Thread.currentThread().name}")
    }

    /**
     * Checks that operation should be performed on background thread
     *
     * @throws IllegalStateException if current thread is not background
     */
    @WorkerThread
    fun assertOnBackgroundThread() {
        assertThat(
            Looper.getMainLooper().thread != Thread.currentThread(),
            "Does not on background thread! Thread: ${Thread.currentThread().name}"
        )
        Timber.v("Thread name: ${Thread.currentThread().name}")
    }

    @AnyThread
    private fun assertThat(condition: Boolean,
                           message: String) {
        if (condition || !BuildConfig.DEBUG) {
            return
        }

        throw IllegalStateException(message)
    }
}
