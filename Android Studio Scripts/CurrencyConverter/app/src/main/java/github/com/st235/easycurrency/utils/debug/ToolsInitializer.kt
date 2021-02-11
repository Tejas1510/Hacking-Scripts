package github.com.st235.easycurrency.utils.debug

import android.content.Context
import com.facebook.stetho.Stetho
import timber.log.Timber

/**
 * Helps initialize all debug tools and skip
 * in release configuration
 */
sealed class ToolsInitializer {
    abstract fun init(androidContext: Context)

    companion object {
        fun init(androidContext: Context,
                 isDebug: Boolean) {
            val toolsInitializer: ToolsInitializer =
                    if (isDebug) DebugInitializer else ReleaseInitializer
            toolsInitializer.init(androidContext)
        }
    }
}

/**
 * Init tools connected with debug mode
 */
object DebugInitializer : ToolsInitializer() {
    override fun init(androidContext: Context) {
        Timber.plant(Timber.DebugTree())
        Stetho.initializeWithDefaults(androidContext)
    }
}

/**
 * Init tools connected with release mode
 */
object ReleaseInitializer : ToolsInitializer() {
    override fun init(androidContext: Context) {
        Timber.plant(TimberReleaseTree())
    }
}
