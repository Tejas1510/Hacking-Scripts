package github.com.st235.easycurrency.utils

import android.app.Activity
import android.view.View
import com.google.android.material.snackbar.BaseTransientBottomBar
import com.google.android.material.snackbar.Snackbar

/**
 * Helps to control snack bar appearance and disappearance
 * including the management of states which info bars strictly prohibited
 */
class SnackBarHelper(activity: Activity,
                     private val snackBarFactory: SnackBarFactory) {
    private val rootView: View = activity.findViewById(android.R.id.content)
    private val snackBarCallback = object: BaseTransientBottomBar.BaseCallback<Snackbar>() {
        override fun onDismissed(transientBottomBar: Snackbar?, event: Int) {
            snackBar?.removeCallback(this)
            snackBar = null
        }
    }

    private var snackBar: Snackbar? = null

    private var isDismissedByUser = false
    private var lastKnownHoursDelta: Int = -1

    /**
     * Show snack bar if it have been allowed to display
     *
     * @param hoursDelta - time since last update
     * @param isExpired - flag, true if data is fresh and false otherwise
     */
    fun showDialogIfNeeded(hoursDelta: Int,
                           isExpired: Boolean) {
        if (isDismissedByUser) {
            return
        }

        val notVisibleAndHaveFreshData = !isVisible() && !isExpired
        val visibleAndHaveFreshData = isVisible() && !isExpired
        val visibleAndHaveExpiredData = isVisible() && isExpired

        val isDataTheSame = hoursDelta == lastKnownHoursDelta

        if (notVisibleAndHaveFreshData ||
            (visibleAndHaveExpiredData && isDataTheSame)) {
            return
        }

        if (visibleAndHaveFreshData) {
            dismissDialog(false)
            return
        }

        if (visibleAndHaveExpiredData && !isDataTheSame) {
            dismissDialog(false)
        }

        showDialog(hoursDelta)
    }

    private fun showDialog(hoursDelta: Int) {
        snackBar = snackBarFactory.createRatesExpiresSnackBar(rootView, hoursDelta, snackBarCallback) {
            dismissDialog(true)
        }

        lastKnownHoursDelta = hoursDelta
        snackBar!!.show()
    }

    private fun isVisible(): Boolean {
        if (snackBar == null) {
            return false
        }

        return snackBar!!.isShownOrQueued
    }

    private fun dismissDialog(isDismissedByUser: Boolean) {
        this.isDismissedByUser = isDismissedByUser
        snackBar?.removeCallback(snackBarCallback)
        snackBar?.dismiss()
        snackBar = null
    }
}
