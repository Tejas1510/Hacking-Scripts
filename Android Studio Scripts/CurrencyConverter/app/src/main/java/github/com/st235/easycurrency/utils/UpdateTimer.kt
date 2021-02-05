package github.com.st235.easycurrency.utils

import github.com.st235.easycurrency.BuildConfig
import java.util.*
import java.util.concurrent.TimeUnit

typealias UpdateCallback = () -> Unit

/**
 * Timer to create a periodic task
 */
class UpdateTimer {
    private val timer = Timer()
    private val timerTask = object: TimerTask() {
        override fun run() {
            updateCallback?.invoke()
        }
    }

    /**
     * Callback which would be fires every time period
     */
    private var updateCallback: UpdateCallback? = null

    init {
        timer.schedule(timerTask,
            0, TimeUnit.MINUTES.toMillis(BuildConfig.FOREGROUND_UPDATE_TIME_IN_MINUTES))
    }

    /**
     * Add callback to timer updates
     */
    fun addCallback(callback: UpdateCallback) {
        updateCallback = callback
        callback()
    }

    /**
     * Removes callback to release reference
     * and prevent leaks
     */
    fun removeCallback() {
        updateCallback = null
    }
}
