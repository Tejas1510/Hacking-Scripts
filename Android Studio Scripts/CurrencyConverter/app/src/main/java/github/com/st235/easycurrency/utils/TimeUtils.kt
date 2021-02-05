package github.com.st235.easycurrency.utils

import github.com.st235.easycurrency.BuildConfig
import java.util.concurrent.TimeUnit

const val MILLIS_TO_UNIX_TIMESTAMP = 1000L

/**
 * A set of utility methods for working
 * with unix-timestamp
 */
object TimeUtils {
    /**
     * Get current time as a unix-timestamp
     */
    fun getTimestamp() = System.currentTimeMillis() / MILLIS_TO_UNIX_TIMESTAMP

    /**
     * Calculate time in hours between current time and passed timestamp
     *
     * @param timestamp - one of calculated time interval
     * @return unix timestamp
     */
    fun getHours(timestamp: Long): Int {
        val timestampDelta = Math.abs(timestamp - getTimestamp())
        return TimeUnit.MILLISECONDS.toHours(timestampDelta * MILLIS_TO_UNIX_TIMESTAMP).toInt()
    }

    /**
     * Checks if current date inside of predetermined time interval {timestamp, timestamp+hoursToExpire}
     *
     * @param timestamp - one of calculated time interval
     * @param hoursToExpire - the predetermined length of passed interval {timestamp, currentTime}
     *
     * @return true if current date inside interval and false otherwise
     */
    fun isTimestampExpired(timestamp: Long,
                           hoursToExpire: Long = BuildConfig.RATES_EXPIRES_HOURS): Boolean {
        val timestampDelta = Math.abs(timestamp - getTimestamp())
        return TimeUnit.MILLISECONDS.toHours(timestampDelta * MILLIS_TO_UNIX_TIMESTAMP) >= hoursToExpire
    }
}
