package github.com.st235.easycurrency.utils

typealias Observer<T> = (response: T) -> Unit

/**
 * Model to create observer pattern
 * Allows to subscribe and unsibscribe from data source
 * May be used as parent for a class or observers list field,
 * if inheritance is prohibited
 */
open class ObservableModel<T> {

    private val observersList: MutableList<Observer<T>> = mutableListOf()

    /**
     * Add observer to monitor model changes
     *
     * @param observer - smth that would listen updated
     */
    open fun addObserver(observer: Observer<T>) {
        observersList.add(observer)
    }

    /**
     * Remove observer from list to stop
     * listen model changed and prevent leaks
     *
     * @param observer - smth have listened updated yet
     */
    open fun removeObserver(observer: Observer<T>) {
        observersList.remove(observer)
    }

    /**
     * Notifies all the observers from list
     * that something have happened with result
     *
     * @param result - result of operation
     */
    fun notifyObservers(result: T) {
        for (observer in observersList) {
            observer(result)
        }
    }
}
