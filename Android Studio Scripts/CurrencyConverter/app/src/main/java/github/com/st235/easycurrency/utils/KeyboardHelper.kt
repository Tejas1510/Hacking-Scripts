package github.com.st235.easycurrency.utils

import android.app.Activity
import android.view.View
import android.view.inputmethod.InputMethodManager

/**
 * Helps to interact with keyboard
 */
class KeyboardHelper(private val activity: Activity) {
    private val inputMethodManager =
        activity.getSystemService(Activity.INPUT_METHOD_SERVICE) as InputMethodManager

    /**
     * Closes soft keyboard
     */
    fun hideKeyboard() {
        var view = activity.currentFocus
        if (view == null) {
            view = View(activity)
        }
        inputMethodManager.hideSoftInputFromWindow(view.windowToken, 0)
    }
}
