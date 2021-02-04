package github.com.st235.easycurrency.utils

import android.annotation.TargetApi
import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent
import android.content.IntentFilter
import android.net.ConnectivityManager
import android.net.Network
import android.net.NetworkCapabilities
import android.net.NetworkRequest
import android.os.Build
import androidx.lifecycle.Lifecycle
import androidx.lifecycle.LifecycleObserver
import androidx.lifecycle.OnLifecycleEvent
import timber.log.Timber

/**
 * Dispatches current network state and fires if
 * state has been changed
 * Hides all version-dependent logic
 * between new and old Android
 */
class NetworkStateDispatcher(private val context: Context,
                             applicationLifecycle: Lifecycle): LifecycleObserver {
    companion object {
        private const val TAG = "[NetworkState]"
    }

    private var networkState: Boolean
    private val connectivityManager: ConnectivityManager
    private val observerModel = ObservableModel<Boolean>()

    private var networkCallback: Any? = null

    init {
        connectivityManager = context.getSystemService(Context.CONNECTIVITY_SERVICE) as ConnectivityManager
        networkState = isOnline()
        applicationLifecycle.addObserver(this)
    }

    /**
     * Starts listen network state from system
     */
    @OnLifecycleEvent(Lifecycle.Event.ON_RESUME)
    fun registerNetworkCallback() {
        Timber.tag(TAG).v("Register network callbacks")

        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
            registerNetworkCallbackForM()
            return
        }
        registerNetworkCallbackForPreM()
    }

    private fun registerNetworkCallbackForPreM() {
        networkCallback = object: BroadcastReceiver() {
            override fun onReceive(context: Context?, intent: Intent?) {
                onStateChanged(isOnline())
            }
        }

        context.registerReceiver(networkCallback as BroadcastReceiver,
            IntentFilter(ConnectivityManager.CONNECTIVITY_ACTION))
    }

    @TargetApi(Build.VERSION_CODES.M)
    private fun registerNetworkCallbackForM() {
        networkCallback = object: ConnectivityManager.NetworkCallback() {
            override fun onAvailable(network: Network?) {
                onStateChanged(true)
            }

            override fun onLost(network: Network?) {
                onStateChanged(false)
            }
        }

        val networkRequest = NetworkRequest.Builder()
            .addTransportType(NetworkCapabilities.TRANSPORT_CELLULAR)
            .addTransportType(NetworkCapabilities.TRANSPORT_WIFI).build()

        connectivityManager.registerNetworkCallback(networkRequest,
            networkCallback as ConnectivityManager.NetworkCallback)
    }

    /**
     * Stops listen network state from system
     */
    @OnLifecycleEvent(Lifecycle.Event.ON_PAUSE)
    fun unregisterNetworkCallback() {
        Timber.tag(TAG).v("Unregister network callbacks")

        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
            unregisterNetworkCallbackForM()
            return
        }
        unregisterNetworkCallbackForPreM()
    }

    private fun unregisterNetworkCallbackForPreM() {
        context.unregisterReceiver(networkCallback as BroadcastReceiver)
    }


    @TargetApi(Build.VERSION_CODES.M)
    private fun unregisterNetworkCallbackForM() {
        connectivityManager.unregisterNetworkCallback(networkCallback as ConnectivityManager.NetworkCallback)
    }

    /**
     * Adds observer to listen network state changes
     */
    fun addObserver(observer: Observer<Boolean>) {
        observerModel.addObserver(observer)
    }

    /**
     * Removes observer from network state changes listening
     */
    fun removeObserver(observer: Observer<Boolean>) {
        observerModel.removeObserver(observer)
    }

    /**
     * Checks if device is online or not
     * Online means connected by wifi or cellular
     */
    fun isOnline(): Boolean {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
            return isOnlineForM()
        }

        return isOnlineForPreM()
    }

    private fun isOnlineForPreM(): Boolean {
        val info = connectivityManager.activeNetworkInfo
        return info.type == ConnectivityManager.TYPE_WIFI ||
                info.type == ConnectivityManager.TYPE_MOBILE
    }

    @TargetApi(Build.VERSION_CODES.M)
    private fun isOnlineForM(): Boolean {
        val network = connectivityManager.activeNetwork
        val capabilities = connectivityManager.getNetworkCapabilities(network) ?: return false
        return capabilities.hasTransport(NetworkCapabilities.TRANSPORT_WIFI) ||
                capabilities.hasTransport(NetworkCapabilities.TRANSPORT_CELLULAR)
    }

    private fun onStateChanged(newState: Boolean) {
        Timber.tag(TAG).v("Network state changed: $newState")
        if (newState != networkState) {
            networkState = newState
            observerModel.notifyObservers(networkState)
        }
    }
}
