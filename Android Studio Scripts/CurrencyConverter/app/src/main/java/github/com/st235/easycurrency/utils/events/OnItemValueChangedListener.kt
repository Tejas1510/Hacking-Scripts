package github.com.st235.easycurrency.utils.events

/**
 * Fires when value in some input have been changed
 */
interface OnItemValueChangedListener<in V, in R> {
    fun onItemValueChanged(value: V, item: R, position: Int)
}
