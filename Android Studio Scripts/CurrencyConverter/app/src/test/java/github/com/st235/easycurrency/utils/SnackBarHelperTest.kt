package github.com.st235.easycurrency.utils

import android.app.Activity
import android.view.View
import com.google.android.material.snackbar.Snackbar
import com.nhaarman.mockitokotlin2.*
import org.junit.Test
import org.junit.runner.RunWith
import org.robolectric.RobolectricTestRunner

typealias ActionCallback = (View) -> Unit

@RunWith(RobolectricTestRunner::class)
class SnackBarHelperTest {
    companion object {
        private const val TIME_EXPIRED = 1
    }

    private val snackbarActionsCallbackFactor
            = argumentCaptor<ActionCallback>()

    private val rootView = mock<View>()
    private val snackBar = mock<Snackbar>()
    private val activity = mock<Activity> {
        on { findViewById<View>(any()) } doReturn rootView
    }
    private val snackBarFactory = mock<SnackBarFactory> {
        on { createRatesExpiresSnackBar(any(), any(), any(),
            snackbarActionsCallbackFactor.capture()) } doReturn snackBar
    }

    private val helper = spy(SnackBarHelper(activity, snackBarFactory))

    @Test
    fun `checks snack bar should appears if data expired`() {
        helper.showDialogIfNeeded(TIME_EXPIRED, true)
        verify(snackBar).show()
    }

    @Test
    fun `checks snack bar should appears once if calls more then one time, but values still the same`() {
        showSnackbar(TIME_EXPIRED, true)
        for (i in 1..9) {
            helper.showDialogIfNeeded(TIME_EXPIRED, true)
        }
        verify(snackBar).show()
    }

    @Test
    fun `checks snack bar should appears each time it calls, if values are different`() {
        showSnackbar(0, true)
        showSnackbar(1, true)
        showSnackbar(2, true)
        verify(snackBar, times(3)).show()
    }

    @Test
    fun `checks snack bar does not appear when data not expired`() {
        showSnackbar(TIME_EXPIRED, false)
        verify(snackBar, never()).show()
    }

    @Test
    fun `checks snack bar hides when there is new not outdated values`() {
        showSnackbar(TIME_EXPIRED, true)
        verify(snackBar).show()
        helper.showDialogIfNeeded(TIME_EXPIRED, false)
        verify(snackBar).dismiss()
    }

    @Test
    fun `checks snack bar does not shows when user dismiss it`() {
        showSnackbar(TIME_EXPIRED, true)
        verify(snackBar).show()
        val callback = snackbarActionsCallbackFactor.firstValue
        callback.invoke(rootView)
        verify(snackBar).dismiss()

        for (i in 0..9) {
            helper.showDialogIfNeeded(TIME_EXPIRED, true)
        }
    }

    private fun showSnackbar(hoursDelta: Int, isExpired: Boolean) {
        helper.showDialogIfNeeded(hoursDelta, isExpired)
        madeVisible(true)
    }

    private fun madeVisible(isVisible: Boolean) {
        whenever(snackBar.isShownOrQueued).thenReturn(isVisible)
    }
}
