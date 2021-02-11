package github.com.st235.easycurrency.utils.events

/**
 * Fires when item inside list have been clicked
 */
interface OnItemClickListener<in R> {
    fun onItemClick(item: R, position: Int)
}
