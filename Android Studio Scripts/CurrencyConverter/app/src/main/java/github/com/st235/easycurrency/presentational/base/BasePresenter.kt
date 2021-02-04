package github.com.st235.easycurrency.presentational.base

/**
 * Base presenter to follow MVP pattern
 */
open class BasePresenter<View> {
    protected var view: View? = null
    private set

    /**
     * Should calls when view visible and ready
     * to get events
     *
     * @param v - current view
     */
    fun attachView(v: View) {
        view = v
        onAttachView(v)
    }

    protected open fun onAttachView(v: View) {}

    /**
     * Should calls when view invisible and soon
     * will be unavailable to handle requests
     */
    fun detachView() {
        onDetachView(view)
        view = null
    }

    protected open fun onDetachView(v: View?) {}
}
