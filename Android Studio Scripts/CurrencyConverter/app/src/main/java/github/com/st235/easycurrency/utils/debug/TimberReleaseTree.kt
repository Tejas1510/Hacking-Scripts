package github.com.st235.easycurrency.utils.debug

import android.util.Log
import timber.log.Timber

/**
 * Helps drop all the log, exclude warning and error messages
 */
class TimberReleaseTree: Timber.Tree() {
    override fun log(priority: Int, tag: String?, message: String, t: Throwable?) {
        if (priority != Log.WARN ||
                priority != Log.ERROR) {
            return
        }

        super.log(priority, tag, message, t)
    }
}
