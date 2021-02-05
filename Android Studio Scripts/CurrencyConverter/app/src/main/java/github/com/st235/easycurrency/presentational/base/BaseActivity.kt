package github.com.st235.easycurrency.presentational.base

import android.os.Bundle
import androidx.annotation.LayoutRes
import androidx.appcompat.app.AppCompatActivity

/**
 * Base parent for all activities at the screen
 */
abstract class BaseActivity: AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        onBeforeInit()

        super.onCreate(savedInstanceState)
        setContentView(getLayout())

        onInitViews()
        onViewsInitialized(savedInstanceState)
    }

    @LayoutRes
    protected abstract fun getLayout(): Int

    /***
     * Calls before all checks
     * Note: use it for important checks (splash screen, for example)
     */
    protected open fun onBeforeInit() {}

    /***
     * Calls before any another methods call.
     * Needs to bind views variables and layout representation
     */
    protected open fun onInitViews() {}

    /**
     * Calls when views initialized to setup
     * @param savedInstanceState state
     */
    protected open fun onViewsInitialized(savedInstanceState: Bundle?) {}
}
